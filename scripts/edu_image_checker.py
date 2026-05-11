#!/usr/bin/env python3
"""edu 配图覆盖率检查 - 扫描 frontmatter image 与实际 SVG/PNG 的匹配情况"""
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not available. Run: pip3 install PyYAML")
    exit(1)

CONTENT_DIR = Path("/home/ubuntu/web3webedu/src/content")
PUBLIC_DIR = Path("/home/ubuntu/web3webedu/public")

def get_all_md_files():
    files = []
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        try:
            content = md_file.read_text(errors="ignore")
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm = yaml.safe_load(parts[1]) or {}
                    files.append((md_file, fm))
        except Exception:
            pass
    return files

def main():
    files = get_all_md_files()
    total = len(files)
    no_image = 0
    png_count = 0
    svg_count = 0
    missing_files = []
    
    for md_file, fm in files:
        img = fm.get("image", "")
        if not img:
            no_image += 1
            continue
        if ".png" in img.lower():
            png_count += 1
        elif ".svg" in img.lower():
            svg_count += 1
        if img.startswith("/images/"):
            img_path = PUBLIC_DIR / img.lstrip("/")
            if not img_path.exists():
                missing_files.append((str(md_file), img))
    
    print("=" * 60)
    print("edu 配图覆盖率检查（统一使用 SVG 格式）")
    print("=" * 60)
    print(f"文章总数：{total}")
    print(f"缺少 image 字段：{no_image}")
    print(f"使用 PNG 格式：{png_count} ⚠️ 建议转为 SVG")
    print(f"使用 SVG 格式：{svg_count} ✅")
    print(f"image 字段存在但图片缺失：{len(missing_files)}")
    existing = total - no_image - len(missing_files)
    coverage = existing / total if total > 0 else 0
    print(f"配图覆盖率：{coverage*100:.0f}% ({existing}/{total})")
    
    if coverage < 0.3:
        print("⚠️ 配图覆盖率严重偏低，需立即补充")
    elif coverage < 0.5:
        print("⚠️ 配图覆盖率低于 50%，建议生成配图")
    elif coverage < 0.8:
        print(f"配图覆盖率 {coverage*100:.0f}%，有提升空间")
    else:
        print(f"✅ 配图覆盖率达标 ({coverage*100:.0f}%)")
    
    if missing_files[:5]:
        label = "前 5" if len(missing_files) > 5 else ""
        if label:
            print(f"\n缺失图片样本 ({label}):")
        else:
            print("\n缺失图片:")
        for fpath, img in missing_files[:5]:
            print(f" - {fpath}: {img}")

if __name__ == "__main__":
    main()
