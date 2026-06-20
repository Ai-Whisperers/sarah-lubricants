#!/usr/bin/env python3
"""Create GitHub repo Ai-Whisperers/sarah-lubricants and push."""
import yaml, urllib.request, urllib.parse, json, os, subprocess, sys, pathlib

with open(os.path.expanduser("~/.config/gh/hosts.yml")) as f:
    cfg = yaml.safe_load(f)

token = cfg["github.com"]["users"]["IvanWeissVanDerPol"]["oauth_token"]
REPO_NAME = "sarah-lubricants"
ORG = "Ai-Whisperers"
LOCAL = pathlib.Path("/root/sarah-lubricants")

def gh_api(method, path, body=None):
    url = f"https://api.github.com{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Authorization": f"token {token}",
                                          "Accept": "application/vnd.github+json",
                                          "User-Agent": "erebus"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")

print(f"== Creating {ORG}/{REPO_NAME} ==")
status, body = gh_api("POST", f"/orgs/{ORG}/repos", {
    "name": REPO_NAME,
    "description": "Sarah's lubricant business in Paraguay — strategy, Sexitive catalog, intake questionnaire, and reusable patterns from maskarada + fun4me",
    "private": False,
    "has_issues": True,
    "has_wiki": False,
    "auto_init": False,
})
print(f"  status: {status}")
if status in (201, 422):
    if status == 422:
        msg = body.get("message", "")
        errors = body.get("errors", [])
        if any("name already exists" in str(e) for e in errors) or "name already exists" in msg:
            print(f"  -> already exists, continuing")
        else:
            print(f"  body: {body}")
            sys.exit(1)
    else:
        print(f"  -> created: {body.get('html_url')}")
else:
    print(f"  body: {body}")
    sys.exit(1)

print(f"\n== Adding remote ==")
remote_url = f"https://{token}@github.com/{ORG}/{REPO_NAME}.git"
subprocess.run(["git", "remote", "remove", "origin"], cwd=LOCAL, capture_output=True)
r = subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=LOCAL)
print(f"  remote add: rc={r.returncode}")

print(f"\n== Pushing main ==")
r = subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=LOCAL,
                   capture_output=True, text=True)
print(f"  push: rc={r.returncode}")
if r.stdout: print(f"  stdout: {r.stdout[-300:]}")
if r.stderr: print(f"  stderr: {r.stderr[-500:]}")

print(f"\n== Result ==")
print(f"  https://github.com/{ORG}/{REPO_NAME}")
