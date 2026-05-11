#!/usr/bin/env python3
"""edu 选题去重器 - 检查新选题是否与现有文章重复"""
import argparse
from pathlib import Path
import re

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not available. Run: pip3 install PyYAML")
    exit(1)

CONTENT_DIR = Path("/home/ubuntu/web3webedu/src/content")

def get_all_titles():
    titles = []
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        try:
            content = md_file.read_text(errors="ignore")
            if not content.startswith("---"):
                continue
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1]) or {}
                if "title" in fm and "slug" in fm:
                    titles.append((fm["title"], fm.get("slug", ""), str(md_file)))
        except Exception:
            pass
    return titles

def similarity(a, b):
    a_words = set(a.lower().replace("/", " ").replace("-", " ").split())
    b_words = set(b.lower().replace("/", " ").replace("-", " ").split())
    if not a_words or not b_words:
        return 0
    inter = a_words & b_words
    return len(inter) / min(len(a_words), len(b_words))

def quality_score(title):
    score = 50
    reasons = []
    if len(title) < 10:
        score -= 15
        reasons.append("标题过短")
    elif len(title) > 50:
        score -= 10
        reasons.append("标题过长")
    tech_terms = ["DNS","USDT","KYC","CBDC","ENS","WHOIS","GDPR","FATF","ICANN","BIS","DNSSEC","区块链","隐私","合规","NFT","Web3"]
    if any(t in title for t in tech_terms):
        score += 15
    else:
        score -= 10
        reasons.append("缺少技术术语")
    if re.search(r'[0-9]', title):
        score += 10
    if any(w in title for w in ["vs","对比","区别","如何","是否","why","how","what","difference"]):
        score += 10
    score = max(0, min(100, score))
    return score, reasons

def main():
    p = argparse.ArgumentParser(description="edu topic checker")
    p.add_argument("--title", required=True, help="Proposed article title")
    p.add_argument("--terse", action="store_true", help="Only output PASS/FAIL")
    a = p.parse_args()
    existing = get_all_titles()
    dupes = []
    for t, sl, path in existing:
        sim = similarity(a.title, t)
        if sim > 0.5 or t == a.title:
            dupes.append((t, sim, sl, path))
    score, reasons = quality_score(a.title)
    if a.terse:
        print("PASS" if not dupes and score >= 50 else "FAIL")
        return
    if dupes:
        print(f"FAIL: 检测到 {len(dupes)} 个相似选题")
        for t, sim, sl, path in sorted(dupes, key=lambda x: -x[1])[:5]:
            print(f"  相似({sim:.0%}): {t}  [/{sl}/]")
    else:
        print("PASS: 无重复选题")
    print(f"\n标题质量评分: {score}/100")
    if reasons:
        print(f"  注意: {', '.join(reasons)}")
    print(f"当前共 {len(existing)} 篇文章")

if __name__ == "__main__":
    main()
