#!/usr/bin/env python3
"""
批量为 edu 项目文章生成配图并更新 frontmatter
- 扫描所有缺少 image 字段的文章
- 生成专属 SVG 配图（深色科技风）
- 更新 frontmatter 添加 image 字段
- 批量 patch 文件
"""

import os
import re
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CONTENT_DIR = Path("/home/ubuntu/web3webedu/src/content")
PUBLIC_IMAGES_DIR = Path("/home/ubuntu/web3webedu/public/images")

def generate_svg_cover(title: str, cluster: str, output_path: str):
    """生成 1200x630 深色科技风配图"""
    width, height = 1200, 630
    
    # 创建图片
    img = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # 绘制渐变背景（简化版，用单色）
    draw.rectangle([0, 0, width, height], fill='#1a1a2e')
    
    # 绘制网格线
    grid_spacing = 40
    for x in range(0, width, grid_spacing):
        draw.line([(x, 0), (x, height)], fill='#2a2a4e', width=1)
    for y in range(0, height, grid_spacing):
        draw.line([(0, y), (width, y)], fill='#2a2a4e', width=1)
    
    # 对角线装饰
    draw.line([(0, 0), (width, height)], fill='#00d4ff', width=2)
    draw.line([(width, 0), (0, height)], fill='#00d4ff', width=2)
    
    # 绘制标题文字（居中）
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except:
        font = ImageFont.load_default()
    
    # 文字居中
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 40
    
    # 绘制文字阴影
    draw.text((x+2, y+2), title, fill='#000000', font=font)
    # 绘制文字主体
    draw.text((x, y), title, fill='#ffffff', font=font)
    
    # 底部网站域名
    domain_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    domain_text = "miamioh.edu.pl"
    bbox = draw.textbbox((0, 0), domain_text, font=domain_font)
    domain_x = width - (bbox[2] - bbox[0]) - 40
    domain_y = height - 60
    draw.text((domain_x, domain_y), domain_text, fill='#00d4ff', font=domain_font)
    
    # 保存图片
    img.save(output_path, 'PNG')
    print(f"  ✓ 生成配图：{output_path}")

def update_frontmatter(file_path: Path, cluster: str, slug: str):
    """为文章添加 image 字段"""
    content = file_path.read_text(encoding='utf-8')
    
    # 检查是否已有 image 字段
    if re.search(r'^image:', content, re.MULTILINE):
        return None  # 已有 image，跳过
    
    # 生成图片路径
    image_path = f"/images/{cluster}/{slug}.png"
    full_image_path = PUBLIC_IMAGES_DIR / f"{cluster}" / f"{slug}.png"
    
    # 确保目录存在
    full_image_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 提取标题
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Untitled"
    
    # 生成配图
    try:
        generate_svg_cover(title, cluster, str(full_image_path))
    except Exception as e:
        print(f"  ✗ 生成配图失败：{e}")
        return None
    
    # 在 publishedAt 后插入 image 字段
    new_content = re.sub(
        r'^(publishedAt:.*)$',
        f'\\1\nimage: "{image_path}"',
        content,
        count=1,
        flags=re.MULTILINE
    )
    
    return new_content

def main():
    print("=" * 60)
    print("edu 项目批量生成配图并更新 frontmatter")
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
        
        # 检查是否已有 image 字段
        if re.search(r'^image:', content, re.MULTILINE):
            skipped_count += 1
            continue
        
        # 提取 cluster 和 slug
        cluster_match = re.search(r'^cluster:\s*(.+)$', content, re.MULTILINE)
        slug_match = re.search(r'^slug:\s*(.+)$', content, re.MULTILINE)
        
        if not cluster_match or not slug_match:
            error_count += 1
            print(f"  ✗ 无法提取 cluster/slug: {md_file}")
            continue
        
        cluster = cluster_match.group(1).strip().strip('"\'')
        slug = slug_match.group(1).strip().strip('"\'')
        
        # 更新 frontmatter
        new_content = update_frontmatter(md_file, cluster, slug)
        
        if new_content:
            md_file.write_text(new_content, encoding='utf-8')
            print(f"  ✓ 更新：{md_file}")
            updated_count += 1
        else:
            error_count += 1
    
    print("=" * 60)
    print(f"完成：更新 {updated_count} 篇，跳过 {skipped_count} 篇，失败 {error_count} 篇")
    print("=" * 60)

if __name__ == "__main__":
    main()
