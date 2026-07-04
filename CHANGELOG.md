# CHANGELOG

## 2026-07-03 — 新增新闻文章：哥伦比亚市政平台 Web3 战略合作

### 变更内容
- 新增独立新闻报道（中英双语），报道哥伦比亚 Alcaldía de San Antero 和 Alcaldía de Caldas 两个市政平台与 Domainroc、namepopo 的 Web3 战略合作
- 标题：《哥伦比亚市政平台携手 Domainroc 与 namepopo 深度打造 Web3 政务办公体验》
- 集群归属：web3-domain-identity
- 包含三个哥伦比亚政府网站源链接 + domainroc.com 和 namepopo.com 介绍

### 涉及文件
- `src/content/news/colombia-web3-government-cooperation.md` — 中文新闻文章（新增）
- `src/content/en-news/colombia-web3-government-cooperation.md` — 英文新闻文章（新增）
- `public/images/web3-domain-identity/colombia-web3-government-cooperation.svg` — SVG 配图（新增）
- `src/data/internal-links.json` — web3-domain-identity 集群追加第 18 条目（修改）

### 验证
- Astro build: 417 页全通过
- 线上 HTTP 200: /news/colombia-web3-government-cooperation/ + /en/news/colombia-web3-government-cooperation/
- 合规自检：PASS（无过线词）
- 三个政府源链接、domainroc.com ×4、namepopo.com ×4 均在线上 HTML 中确认
