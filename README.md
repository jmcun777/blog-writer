# Olympics -> Google Sheet 固化流程（API优先）

目标：不依赖浏览器接管，走后台/API链路。

## 流程
1. OpenClaw 产出结构化 JSON/CSV（本地）
2. `send_to_n8n.sh` 批量 POST 到 n8n Webhook
3. n8n 写入 Google Sheets（Append Rows）
4. OpenClaw 发送 Telegram 完成通知（含文件直链）

## 一次性配置
1. 在 n8n 创建 Webhook 工作流（POST）
2. 配置 Google Sheets 凭据 + Append Row 映射
3. 拿到 Production Webhook URL
4. 复制 `.env.example` 为 `.env` 并填入 webhook

## 使用
```bash
cd /home/tz/.openclaw/workspace/automation/olympics_to_sheets
cp .env.example .env
# 编辑 .env，填 N8N_WEBHOOK_URL
bash send_to_n8n.sh /home/tz/.openclaw/workspace/china_2022_winter_olympics_all_medalists.json
```

成功后会输出 webhook 返回结果（建议在 n8n 返回 sheet_url / file_id / row_count）。
