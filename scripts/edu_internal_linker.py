#!/usr/bin/env python3
"""edu 内链发现器 - 为新文章推荐最相关的内链"""
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not available. Run: pip3 install PyYAML")
    exit(1)

CONTENT_DIR = Path("/home/ubuntu/web3webedu/src/content")

def get_all_pages():
    pages = []
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        try:
            content = md_file.read_text(errors="ignore")
            if not content.startswith("---"):
                continue
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1]) or {}
                if "title" in fm and "slug" in fm:
                    pages.append({
                        "title": fm.get("title", ""),
                        "slug": fm.get("slug", ""),
                        "section": fm.get("section", ""),
                        "cluster": fm.get("cluster", ""),
                        "tags": fm.get("tags", []),
                        "path": str(md_file)
                    })
        except Exception:
            pass
    return pages

def score_relevance(topic, page):
    t = topic.lower()
    score = 0
    # title keywords match
    for word in t.split():
        if len(word) >= 3 and word in page.get("title", "").lower():
            score += 3
    # cluster match
    if page.get("cluster") and page["cluster"].lower() in t:
        score += 5
    # section match
    if page.get("section") and page["section"].lower() in t:
        score += 3
    # tags overlap
    for tag in page.get("tags", []):
        if tag.lower() in t:
            score += 2
    return score

def main():
    p = argparse.ArgumentParser(description="edu internal linker")
    p.add_argument("--topic", required=True, help="Article topic or title")
    p.add_argument("--n", type=int, default=5, help="Number of suggestions")
    p.add_argument("--cluster", default="", help="Filter by cluster id")
    a = p.parse_args()
    
    pages = get_all_pages()
    if a.cluster:
        pages = [p_ for p_ in pages if p_.get("cluster") == a.cluster]
    
    scored = [(p_, score_relevance(a.topic, p_)) for p_ in pages]
    scored.sort(key=lambda x: -x[1])
    
    seen = set()
    results = []
    for page, sc in scored:
        if sc > 0 and page["slug"] not in seen:
            results.append((page, sc))
            seen.add(page["slug"])
            if len(results) >= a.n:
                break
    
    print(f"edu 内链推荐: {a.topic}")
    print("-" * 60)
    for page, sc in results:
        print(f"  title  : \"{page['title']}\"")
        print(f"  url    : /{page['slug']}/")
        print(f"  cluster: {page.get('cluster', '')} | match: {sc}")
        print()

if __name__ == "__main__":
    main()
