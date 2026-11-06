"""Daily news discovery; not a verified Pokémon GO battle-data feed."""
import datetime as dt
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'data' / 'updates.json'
NOW = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
URL = 'https://news.google.com/rss/search?q=Pok%C3%A9mon+GO+raid+when%3A7d&hl=en&gl=US&ceid=US%3Aen'
previous = json.loads(DEST.read_text(encoding='utf-8')) if DEST.exists() else {'items': []}
try:
    req = urllib.request.Request(URL, headers={'User-Agent':'PokemonGORaidDex/1.0 (news aggregator)'})
    with urllib.request.urlopen(req, timeout=20) as response:
        body = response.read(2_000_000)
    root = ET.fromstring(body)
    items = []
    for node in root.findall('./channel/item')[:15]:
        title = (node.findtext('title') or '').strip()
        link = (node.findtext('link') or '').strip()
        if not title or not link.startswith('https://'):
            continue
        items.append({'title': title[:250], 'url': link, 'published': (node.findtext('pubDate') or '')[:40]})
    if not items:
        raise ValueError('No usable RSS entries')
    payload = {'checked_at': NOW, 'status': 'ok', 'items': items, 'source': 'Google News RSS search; headlines are unverified'}
except Exception as exc:
    print('Fetch failed:', type(exc).__name__, str(exc)[:200])
    payload = {'checked_at': NOW, 'status': 'fetch_failed', 'items': previous.get('items', []), 'source': 'Previous cached search results; unverified'}
DEST.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
