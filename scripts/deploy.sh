#!/bin/bash
# edu 一键部署脚本
# 用法: ./scripts/deploy.sh [--dry-run]
set -e

WORK_DIR="/home/ubuntu/web3webedu"
PM2_NAME="web3edu"
cd "$WORK_DIR"

# Dry run
if [ "$1" == "--dry-run" ]; then
    echo "Dry-run: validate → build → restart PM2 → verify"
    echo "  npm run validate"
    echo "  SITE_URL=https://www.miamioh.edu.pl npm run build"
    echo "  npx pm2 restart $PM2_NAME"
    exit 0
fi

echo "=== Step 1/4: 验证 ==="
npm run validate 2>&1 | tail -20

echo "=== Step 2/4: 构建 ==="
SITE_URL=https://www.miamioh.edu.pl npm run build 2>&1 | tail -10

echo "=== Step 3/4: 重启 PM2 ==="
npx pm2 restart "$PM2_NAME"

echo "=== Step 4/4: 验证线上 ==="
sleep 3
for path in "/library/buy-domain-with-usdt/" "/research/web3-domain-identity/"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://www.miamioh.edu.pl$path")
    echo "  $path -> HTTP $status"
done

echo ""
echo "✅ 部署完成"
