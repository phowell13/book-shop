import feedparser
from datetime import datetime
import os
import hashlib

# CONFIG
FEED_URL = "https://hypebeast.com/feed"  # You can change this
POST_DIR = "_posts"

# Ensure posts directory exists
os.makedirs(POST_DIR, exist_ok=True)

feed = feedparser.parse(FEED_URL)

for entry in feed.entries[:5]:  # limit how many per run
    title = entry.title
    date = datetime(*entry.published_parsed[:6])
    slug = hashlib.md5(entry.link.encode()).hexdigest()[:8]
    filename = f"{POST_DIR}/{date.strftime('%Y-%m-%d')}-{slug}.md"

    if os.path.exists(filename):
        continue  # skip if already added

    content = entry.summary if "summary" in entry else ""
    url = entry.link

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"date: {date.isoformat()}\n")
        f.write(f"layout: post\n")
        f.write(f"---\n\n")
        f.write(f"[Read original post]({url})\n\n")
        f.write(content)
