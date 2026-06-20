#!/bin/bash
# Deploy Sarah repo to Cloudflare Pages
set -e

# Load token from file
export CLOUDFLARE_API_TOKEN
export CLOUDFLARE_ACCOUNT_ID

cd /root/sarah-lubricants
wrangler pages deploy build --project-name=sarah-lubricants --branch=main "$@"
