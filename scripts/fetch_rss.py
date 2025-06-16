import feedparser
from datetime import datetime
import os
import hashlib

FEED_URL = "https://hypebeast.com/feed"
POST_DIR = "_posts"

os.makedirs(POST_DIR, exist_ok=True)

feed = feedparser.parse(FEED_URL)

for entry in feed.entries[:5]:
    if not hasattr(entry, "published_parsed"):
        continue

    title = entry.title
    date = datetime(*entry.published_parsed[:6])
    slug = hashlib.md5(entry.link.encode()).hexdigest()[:8]
    filename = f"{POST_DIR}/{date.strftime('%Y-%m-%d')}-{slug}.md"

    if os.path.exists(filename):
        continue

    content = entry.summary if hasattr(entry, "summary") else ""
    url = entry.link

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"date: {date.isoformat()}\n")
        f.write(f"layout: post\n")
        f.write(f"---\n\n")
        f.write(f"[Read original post]({url})\n\n")
        f.write(content)
