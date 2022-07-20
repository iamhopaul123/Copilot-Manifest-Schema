import requests
import os

def retrieve_docs():
    base_gh_url = "https://api.github.com/repos/aws/copilot-cli/contents/site/content/docs"
    main_resp = requests.get(os.path.join(base_gh_url, "manifest"))
    main_docs = {}
    for resp in main_resp.json():
        if not resp["name"].endswith(".en.md"):
            continue
        r = requests.get(resp["download_url"])
        main_docs[resp["name"].rstrip(".md")] = r.text
    partial_resp = requests.get(os.path.join(base_gh_url, "include"))
    partial_docs = {}
    for resp in partial_resp.json():
        if not resp["name"].endswith(".en.md"):
            continue
        r = requests.get(resp["download_url"])
        partial_docs[resp["name"].rstrip(".md")] = r.text
    return {
        "main": main_docs,
        "partial": partial_docs
    }

# For testing purpose.
if __name__ == "__main__":
    print(retrieve_docs())