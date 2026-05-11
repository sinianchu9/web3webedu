#!/usr/bin/env python3
"""
批量为 edu 项目文章生成 SVG 格式配图（替换现有 PNG）
- 扫描所有文章
- 为每篇文章生成 SVG 格式配图
- 更新 frontmatter 中的 image 字段为 SVG 路径
"""

import os
import re
from pathlib import Path
from xml.sax.saxutils import escape

CONTENT_DIR = Path("/home/ubuntu/web3webedu/src/content")
PUBLIC_IMAGES_DIR = Path("/home/ubuntu/web3webedu/public/images")

def generate_svg(title: str, description: str, cluster: str, output_path: str):
    """生成 1200x630 深色科技风 SVG 配图"""
    
    # 清理文本，避免 SVG 特殊字符
    safe_title = escape(title[:60])
    safe_desc = escape(description[:80] + "..." if len(description) > 80 else description)
    
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1200" height="630" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景 -->
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#16213e;stop-opacity:1" />
    </linearGradient>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#2a2a4e" stroke-width="1"/>
    </pattern>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- 背景层 -->
  <rect width="1200" height="630" fill="url(#bgGradient)"/>
  <rect width="1200" height="630" fill="url(#gridPattern)"/>
  
  <!-- 加密货币图案 - 比特币 -->
  <g transform="translate(100, 100) scale(3)">
    <circle cx="0" cy="0" r="50" fill="#f7931a" opacity="0.2"/>
    <circle cx="0" cy="0" r="45" fill="none" stroke="#f7931a" stroke-width="3"/>
    <text x="0" y="18" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="#f7931a" text-anchor="middle">₿</text>
  </g>
  
  <!-- 加密货币图案 - 以太坊 -->
  <g transform="translate(1000, 530) scale(2.5)">
    <polygon points="0,-40 30,10 0,25 -30,10" fill="#627eea" opacity="0.3"/>
    <polygon points="0,-40 30,10 0,25 -30,10" fill="none" stroke="#627eea" stroke-width="2"/>
  </g>
  
  <!-- 对角线装饰 -->
  <line x1="0" y1="0" x2="1200" y2="630" stroke="#00d4ff" stroke-width="2" opacity="0.3"/>
  <line x1="1200" y1="0" x2="0" y2="630" stroke="#00d4ff" stroke-width="2" opacity="0.3"/>
  
  <!-- 标题文字（居中） -->
  <text x="600" y="280" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#ffffff" text-anchor="middle" filter="url(#glow)">
    {safe_title}
  </text>
  
  <!-- 描述文字 -->
  <text x="600" y="340" font-family="Arial, sans-serif" font-size="28" fill="#a0a0c0" text-anchor="middle">
    {safe_desc}
  </text>
  
  <!-- 关键词标签 -->
  <g transform="translate(600, 420)">
    <rect x="-120" y="-20" width="240" height="40" rx="20" fill="#00d4ff" opacity="0.2"/>
    <rect x="-120" y="-20" width="240" height="40" rx="20" fill="none" stroke="#00d4ff" stroke-width="2"/>
    <text x="0" y="8" font-family="Arial, sans-serif" font-size="20" fill="#00d4ff" text-anchor="middle">USDT 购买域名</text>
  </g>
  
  <!-- 底部网站域名 -->
  <text x="1150" y="590" font-family="Arial, sans-serif" font-size="24" fill="#00d4ff" text-anchor="end" font-weight="bold">
    miamioh.edu.pl
  </text>
  
  <!-- 角落装饰 -->
  <circle cx="1150" cy="50" r="8" fill="#00d4ff" opacity="0.6"/>
  <circle cx="50" cy="580" r="6" fill="#f7931a" opacity="0.6"/>
</svg>'''
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f" ✓ 生成 SVG: {output_path}")

def update_frontmatter_to_svg(file_path: Path, cluster: str, slug: str):
    """将文章 frontmatter 更新为 SVG 格式"""
    content = file_path.read_text(encoding='utf-8')
    
    # 检查是否已有 image 字段
    image_match = re.search(r'^image:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if not image_match:
        return None  # 没有 image 字段，跳过
    
    # 生成 SVG 图片路径
    svg_image_path = f"/images/{cluster}/{slug}.svg"
    full_svg_path = PUBLIC_IMAGES_DIR / f"{cluster}" / f"{slug}.svg"
    
    # 确保目录存在
    full_svg_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 提取标题
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Untitled"
    
    # 提取描述
    desc_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    description = desc_match.group(1) if desc_match else ""
    
    # 生成 SVG
    try:
        generate_svg(title, description, cluster, str(full_svg_path))
    except Exception as e:
        print(f" ✗ 生成 SVG 失败：{e}")
        return None
    
    # 替换 image 字段为 SVG 路径
    new_content = re.sub(
        r'^image:\s*["\']?.*?["\']?\s*$',
        f'image: "{svg_image_path}"',
        content,
        count=1,
        flags=re.MULTILINE
    )
    
    return new_content

def main():
    print("=" * 60)
    print("edu 项目批量生成 SVG 配图（替换 PNG 为 SVG 格式）")
    print("=" * 60)
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    # 遍历所有内容文件
    for md_file in CONTENT_DIR.rglob("*.md"):
        # 跳过 authors 等无 cluster 字段的内容
        if '/authors/' in str(md_file):
            skipped_count += 1
            continue
        
        content = md_file.read_text(encoding='utf-8')
        
        # 提取 cluster 和 slug
        cluster_match = re.search(r'^cluster:\s*(.+)$', content, re.MULTILINE)
        slug_match = re.search(r'^slug:\s*(.+)$', content, re.MULTILINE)
        
        if not cluster_match or not slug_match:
            error_count += 1
            print(f" ✗ 无法提取 cluster/slug: {md_file}")
            continue
        
        cluster = cluster_match.group(1).strip().strip('"\'')
        slug = slug_match.group(1).strip().strip('"\'')
        
        # 更新 frontmatter 为 SVG
        new_content = update_frontmatter_to_svg(md_file, cluster, slug)
        
        if new_content:
            md_file.write_text(new_content, encoding='utf-8')
            print(f" ✓ 更新：{md_file}")
            updated_count += 1
        else:
            error_count += 1
    
    print("=" * 60)
    print(f"完成：更新 {updated_count} 篇，跳过 {skipped_count} 篇，失败 {error_count} 篇")
    print("=" * 60)

if __name__ == "__main__":
    main()
