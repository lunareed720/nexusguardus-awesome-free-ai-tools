#!/usr/bin/env python3
"""Verify all tool URLs in the awesome-free-ai-tools catalog."""
import json, urllib.request, sys

def check_url(name, url):
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64)')
        resp = urllib.request.urlopen(req, timeout=15)
        if resp.status >= 400:
            return f'{name}: HTTP {resp.status} {url}'
    except Exception as e:
        return f'{name}: {str(e)[:80]} {url}'
    return None

tools = json.load(open('data/verified-tools.json'))
print(f'Checking {len(tools)} tool URLs...')
broken = [r for r in (check_url(t['name'], t['url']) for t in tools) if r]

if broken:
    print(f'\nFound {len(broken)} broken link(s):')
    for b in broken:
        print(f'  - {b}')
    sys.exit(1)
else:
    print(f'All {len(tools)} URLs OK.')
