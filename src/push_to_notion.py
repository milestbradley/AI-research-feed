# src/push_to_notion.py

from notion_client import Client
from datetime import datetime
from src.config import NOTION_TOKEN, NOTION_DATABASE_ID

notion = Client(auth=NOTION_TOKEN)

def push_paper_to_notion(paper, summary, score=0.7):
    try:
        notion.pages.create(parent={"database_id": NOTION_DATABASE_ID},
            properties={
                "Title": {
                    "title": [{"text": {"content": paper["title"]}}]
                },
                "Summary": {
                    "rich_text": [{"text": {"content": summary}}]
                },
                "Source": {
                    "select": {"name": paper.get("source", "arXiv")}
                },
                "Tags": {
                    "multi_select": [{"name": tag} for tag in []]  # Add tag parsing if you want
                },
                "Score": {
                    "number": score
                },
                "Date": {
                    "date": {"start": paper["published"].strftime("%Y-%m-%d")}
                },
                "Link": {
                    "url": paper["pdf_url"]
                }
            }
        )
        print(f"✅ Added: {paper['title']}")
    except Exception as e:
        print(f"❌ Failed to add paper: {paper['title']} – {e}")
