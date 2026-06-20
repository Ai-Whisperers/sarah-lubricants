#!/usr/bin/env python3
"""Read GH token from config and verify."""
import yaml, urllib.request, json, os, sys

with open(os.path.expanduser("~/.config/gh/hosts.yml")) as f:
    cfg = yaml.safe_load(f)

token = cfg["github.com"]["users"]["IvanWeissVanDerPol"]["oauth_token"]
print(f"Token: {token[:10]}...{token[-4:]}  (len={len(token)})")

req = urllib.request.Request("https://api.github.com/user",
                             headers={"Authorization": f"token {token}",
                                      "User-Agent": "erebus-script"})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        d = json.loads(r.read())
        print(f"Login: {d.get('login')}")
        print(f"ID: {d.get('id')}")
        print(f"Scopes: {r.headers.get('X-OAuth-Scopes', 'none')}")
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()[:300]}")
