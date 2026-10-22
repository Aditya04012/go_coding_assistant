
import base64
import requests

from dotenv import load_dotenv
import os

from langchain_core.tools import tool

load_dotenv()

GITHUB_API = "https://api.github.com"

token_url=os.getenv("GITHUB_TOKEN")
@tool
def github_code_search(query: str) -> str:
    """Search public GitHub Go source code and retrieve matching file contents.
    Use for Go implementations, handlers, middleware, APIs, and examples.
    """
    token=token_url

    if not token:
        return "Missing GITHUB_TOKEN in your .env file."

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    try:
        # Step 1: Search Go source files
        response = requests.get(
            f"{GITHUB_API}/search/code",
            headers=headers,
            params={
                "q": f"{query} language:go",
                "per_page": 3,
            },
            timeout=15,
        )
        response.raise_for_status()

        files = response.json().get("items", [])

        if not files:
            return "No matching Go source files found."

        results = []

        # Step 2: Fetch the contents of each matching file
        for item in files:
            repo = item["repository"]["full_name"]
            path = item["path"]

            file_response = requests.get(
                f"{GITHUB_API}/repos/{repo}/contents/{path}",
                headers=headers,
                timeout=15,
            )
            file_response.raise_for_status()

            data = file_response.json()

            if data.get("encoding") != "base64":
                continue

            content = base64.b64decode(
                data["content"]
            ).decode("utf-8", errors="replace")

            # Keep the response manageable
            content = content[:10000]

            results.append(
                f"Repository: {repo}\n"
                f"File: {path}\n"
                f"URL: {item['html_url']}\n"
                f"Source code:\n{content}"
            )

        return "\n\n" + ("\n\n" + "=" * 60 + "\n\n").join(results) \
            if results else "No readable source files found."

    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 401:
            return "GitHub token is invalid or unauthorized."
        if exc.response is not None and exc.response.status_code == 403:
            return "GitHub API access denied or rate limit exceeded."
        return f"GitHub API error: {exc}"

    except (requests.RequestException, ValueError) as exc:
        return f"GitHub search failed: {exc}"
