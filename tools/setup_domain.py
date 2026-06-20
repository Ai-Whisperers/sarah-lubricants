#!/usr/bin/env python3
"""Setup custom domain sarah.paragu-ai.com -> sarah-lubricants.pages.dev"""
import os, json, urllib.request, urllib.parse, urllib.error, sys

API = "https://api.cloudflare.com/client/v4"
TOKEN = open("/tmp/cf_token").read().strip()
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

def api(method, path, body=None):
    url = API + path
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"errors": [json.loads(e.read())], "status": e.code}

print("== Finding zone ==")
r = api("GET", "/zones?name=paragu-ai.com")
if not r.get("success"):
    print("ERROR finding zone:", r.get("errors"))
    sys.exit(1)
zone_id = r["result"][0]["id"]
print(f"  zone_id: {zone_id}")

print("\n== Checking existing sarah.paragu-ai.com record ==")
r = api("GET", f"/zones/{zone_id}/dns_records?name=sarah.paragu-ai.com")
existing = r.get("result", [])
print(f"  existing records: {len(existing)}")
for rec in existing:
    print(f"    {rec['type']} {rec['name']} -> {rec['content']}")

print("\n== Creating CNAME sarah.paragu-ai.com -> sarah-lubricants.pages.dev ==")
body = {
    "type": "CNAME",
    "name": "sarah",
    "content": "sarah-lubricants.pages.dev",
    "proxied": True,
    "ttl": 1,
    "comment": "Sarah's Lubricant Business strategy site",
}
if existing:
    rec_id = existing[0]["id"]
    r = api("PUT", f"/zones/{zone_id}/dns_records/{rec_id}", body)
    print(f"  Updated existing record: {'OK' if r.get('success') else r.get('errors')}")
else:
    r = api("POST", f"/zones/{zone_id}/dns_records", body)
    print(f"  Created new record: {'OK' if r.get('success') else r.get('errors')}")

print("\n== Attaching custom domain to Pages project ==")
r = api("POST", f"/accounts/{os.environ['CLOUDFLARE_ACCOUNT_ID']}/pages/projects/sarah-lubricants/domains", {
    "name": "sarah.paragu-ai.com"
})
if r.get("success"):
    print(f"  Attached: {r.get('result')}")
else:
    errs = r.get("errors", [])
    for e in errs:
        msg = e.get("message", "")
        if "already exists" in msg.lower() or "in use" in msg.lower():
            print(f"  Already attached (OK): {msg}")
        else:
            print(f"  Error: {e}")

print("\n== DNS propagation check ==")
import subprocess
out = subprocess.run(["dig", "+short", "sarah.paragu-ai.com", "CNAME"], capture_output=True, text=True, timeout=10)
print(f"  dig output: {out.stdout.strip() or '(not yet propagated)'}")
