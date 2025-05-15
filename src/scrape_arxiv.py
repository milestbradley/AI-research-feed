# src/scrape_arxiv.py

import arxiv
from datetime import datetime, timedelta
from src.config import KEYWORDS

def fetch_papers(max_results=10, days_back=1):
    search_query = " OR ".join(f'all:"{kw}"' for kw in KEYWORDS)
    date_from = (datetime.now() - timedelta(days=days_back)).strftime("%Y%m%d")

    results = arxiv.Search(
        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []
    for result in results.results():
        papers.append({
            "title": result.title,
            "abstract": result.summary,
            "authors": [a.name for a in result.authors],
            "pdf_url": result.pdf_url,
            "published": result.published,
            "arxiv_id": result.entry_id.split("/")[-1],
            "source": "arXiv"
        })

    return papers
