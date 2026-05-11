---
title: "DoH与DoT协议对比：DNS加密传输的安全性与部署分析"
description: "从ICANN DNS、ICANN DNSSEC和NIST SP 800-81框架分析DNS over HTTPS与DNS over TLS两种加密DNS协议的技术差异、安全特性与部署考量。"
slug: "dns-security-governance/doh-dot-protocol"
section: "research"
cluster: "dns-security-governance"
type: "longtail"
language: "zh-CN"
publishedAt: "2026-05-07"
image: "/images/dns-security-governance/dns-security-governance/doh-dot-protocol.svg"
updatedAt: "2026-05-07"
author: "Web3 Domain Institute Editorial Team"
reviewer: "Domain Infrastructure Research Desk"
tags:
- "DoH DoT"
- "DNS加密"
- "DNS安全"
- "DNS over HTTPS"
- "域名治理"
keywords:
 primary: "DoH DoT"
 secondary:
   - "DNS over HTTPS"
   - "DNS over TLS"
   - "DNS安全"
   - "DNS加密协议"
   - "域名治理"
riskLevel: "low"
index: true
audience:
- "技术人员"
- "研究者"
- "域名持有者"
summary: "DNS over HTTPS（DoH）与DNS over TLS（DoT）是两种主流DNS加密协议，分别基于HTTPS（端口443）和TLS（端口853）传输DNS查询。DoH更难被网络中间设备检测和过滤，DoT在运维可观测性方面更具优势。两者均需与ICANN DNSSEC配合使用以实现端到端DNS安全。"
faqs:
-
  question: "DoH和DoT哪个更安全？"
  answer: "两者在数据传输加密层面安全性相当，均使用TLS加密。DoH因伪装为HTTPS流量更难被中间设备干扰，但这也降低了网络运维的可观测性；DoT使用独立端口，便于企业网络管控。安全性取决于部署场景和威胁模型。"
-
  question: "DoH/DoT是否可以替代DNSSEC？"
  answer: "不可以。DoH/DoT保护的是传输通道的机密性和完整性，防止查询被窃听或篡改；DNSSEC保护的是DNS数据本身的来源验证和完整性。两者互补，ICANN建议同时部署。"
references:
-
  title: "ICANN DNS Technical Overview"
  url: "https://www.icann.org/resources/pages/dns-101"
  source: "ICANN DNS"
-
  title: "DNSSEC – ICANN"
  url: "https://www.icann.org/resources/pages/dnssec"
  source: "ICANN DNSSEC"
-
  title: "NIST SP 800-81 Rev. 3: Secure DNS Deployment Guide"
  url: "https://csrc.nist.gov/publications/detail/sp/800-81/3/final"
  source: "NIST SP 800-81"
related:
-
  title: "DNS安全与域名治理研究"
  url: "/research/dns-security-governance/"
-
  title: "DNS over HTTPS研究"
  url: "/research/dns-security-governance/dns-over-https/"
-
  title: "DNSSEC部署分析"
  url: "/research/dns-security-governance/dnssec/"
-
  title: "DNSSEC检查指南"
  url: "/tools/dnssec-check-guide/"
-
  title: "2026 DNS安全与域名治理报告"
  url: "/reports/2026-dns-security-governance-report/"
updateCadence: "weekly"
schemaType: "Article"
---

## 摘要

DNS over HTTPS（DoH，RFC 8484）与DNS over TLS（DoT，RFC 7858）是当前两种主流的DNS加密传输协议，旨在解决传统DNS查询以明文传输带来的窃听与篡改风险。DoH利用HTTPS协议（端口443）封装DNS消息，与现有Web流量混合；DoT使用独立TLS连接（端口853）传输DNS查询。两者在加密强度上等效，但在流量可观测性、网络管控和部署复杂度方面存在显著差异。根据NIST SP 800-81 Rev. 3的指导，DoH/DoT应与ICANN DNSSEC协同部署以实现完整的DNS安全架构。

## 问题定义

本页研究DoH与DoT两种DNS加密协议的技术特性、安全差异与部署适用场景，重点分析在ICANN DNS治理框架下两种协议对域名安全生态的差异化影响，以及在NIST安全部署指南中的定位。

## 背景知识

传统DNS查询使用UDP端口53明文传输，任何网络中间设备均可读取或篡改查询内容。ICANN于2019年将DNS加密列为DNS演进的关键方向之一。IETF随后标准化了DoT（RFC 7858，2016年）和DoH（RFC 8484，2018年）协议。

NIST SP 800-81 Rev. 3（2024年发布）明确建议联邦机构部署DNS加密协议，并将DoH/DoT纳入DNS安全部署基线。ICANN DNSSEC通过数字签名验证DNS响应的来源真实性和数据完整性，与传输层加密（DoH/DoT）形成互补安全层。

## 核心结论

| 特性 | DoH（RFC 8484） | DoT（RFC 7858） |
|---|---|---|
| 传输协议 | HTTPS/TLS（端口443） | TLS（端口853） |
| 流量特征 | 与Web流量混合 | 独立端口可识别 |
| 防中间设备干扰 | 高 | 中 |
| 运维可观测性 | 低 | 高 |
| 企业网络管控 | 困难 | 较易 |
| 部署复杂度 | 中（需HTTP/2栈） | 低（仅需TLS） |
| 浏览器支持 | Chrome/Firefox/Edge原生 | 需系统级配置 |

1. **DoH与DoT加密强度等效**：两者均使用TLS 1.2/1.3加密，在数据传输机密性和完整性方面无本质差异。
2. **DoH的隐蔽性是双刃剑**：DoH流量与普通HTTPS流量混合，使网络中间设备难以检测和过滤DNS查询，增强了抗审查能力，但降低了企业网络的DNS可观测性和安全监控能力。
3. **DoT更适合受控网络环境**：企业网络和机构通常偏好DoT，因为其独立端口便于策略管控和流量审计。
4. **DoH/DoT与DNSSEC功能互补**：DoH/DoT保护传输通道安全，DNSSEC保护DNS数据本身的真实性，两者共同构成ICANN推荐的DNS安全基线。

## 风险与限制

| 风险项 | 影响等级 | 缓解措施 |
|---|---|---|
| DoH绕过企业DNS安全策略 | 中 | 部署企业DoH策略，指定可信解析器 |
| DoT端口被防火墙阻断 | 低 | 配置防火墙允许端口853出站 |
| 加密DNS解析器集中化 | 中 | 支持多解析器部署，避免单一依赖 |
| DNSSEC验证在加密通道中被跳过 | 高 | 确保解析器同时执行DNSSEC验证 |
| 协议碎片化增加运维复杂度 | 低 | 根据场景选择单一协议优先部署 |

## 合规边界

本页分析基于ICANN DNS技术标准、ICANN DNSSEC部署指南和NIST SP 800-81 Rev. 3安全部署框架。DoH/DoT协议部署应遵循所在司法管辖区的网络安全法规，企业环境中实施DoH策略时需平衡安全监控需求与用户隐私保护。本页内容不构成对任何特定DNS加密方案的推荐，域名持有者应根据自身威胁模型选择合适的部署方案。

## 相关入口

- [DNS安全与域名治理研究](/research/dns-security-governance/) — DNS安全领域全景概览
- [DNS over HTTPS研究](/research/dns-security-governance/dns-over-https/) — DoH协议深入分析
- [DNSSEC部署分析](/research/dns-security-governance/dnssec/) — DNSSEC数字签名机制详解
- [DNSSEC检查指南](/tools/dnssec-check-guide/) — 验证域名DNSSEC部署状态
- [2026 DNS安全与域名治理报告](/reports/2026-dns-security-governance-report/) — 最新DNS安全趋势追踪
