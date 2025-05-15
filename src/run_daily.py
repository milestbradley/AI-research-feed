# src/run_daily.py

from src.scrape_arxiv import fetch_papers
from src.summarize import summarize_abstract
from src.push_to_notion import push_paper_to_notion

def main():
    print("🔍 Fetching papers...")
    papers = fetch_papers(max_results=10)

    for paper in papers:
        print(f"\n📄 {paper['title']}")
        summary = summarize_abstract(paper["title"], paper["abstract"])
        if summary:
            push_paper_to_notion(paper, summary, score=0.75)
        else:
            print("❌ Skipped due to summarization error.")

if __name__ == "__main__":
    main()
