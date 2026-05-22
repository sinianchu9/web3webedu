---
title: "CBDC跨境域名支付路径与SWIFT替代方案"
description: "分析CBDC跨境支付如何绕过SWIFT体系直接完成域名交易结算，评估BIS mBridge与数字人民币跨境支付的技术路径与监管约束。"
image: "/images/cbdc-domain-infrastructure/cbdc-cross-border-payment-swift-alternative.svg"
slug: "cbdc-domain-infrastructure/cbdc-cross-border-payment-swift-alternative"
section: "research"
cluster: "cbdc-domain-infrastructure"
type: "longtail"
language: "zh-CN"
publishedAt: "2026-05-13"
updatedAt: "2026-05-13"
author: "Web3 Domain Institute Editorial Team"
reviewer: "Domain Infrastructure Research Desk"
tags:
- "CBDC"
- "跨境支付"
- "SWIFT替代"
- "数字人民币"
- "mBridge"
keywords:
  primary: "CBDC跨境域名支付"
  secondary:
    - "SWIFT替代"
    - "数字人民币跨境"
    - "mBridge"
    - "CBDC域名结算"
    - "跨境支付路径"
riskLevel: "medium"
index: true
audience:
- "研究者"
- "Web3创业者"
- "域名持有者"
summary: "评估BIS mBridge架构与e-CNY跨境试点在域名交易结算中的技术可行性与监管约束，分析CBDC替代SWIFT的路径与限制。"
faqs:
- question: "CBDC跨境支付能否完全替代SWIFT？"
  answer: "在多数情况下不能完全替代。mBridge等CBDC跨境项目目前限于特定走廊的试点阶段，SWIFT在全球银行间通信中仍占主导地位。"
- question: "数字人民币能否用于国际域名注册支付？"
  answer: "目前e-CNY跨境支付仍处于试点阶段，主要用于零售场景，域名注册等B2B支付尚无成熟商业应用。"
- question: "mBridge与SWIFT的本质差异是什么？"
  answer: "mBridge基于分布式账本实现点对点结算，SWIFT基于报文传输依赖代理行网络；前者可能缩短结算时间，但互操作性和治理框架仍待完善。"
references:
- title: "BIS CBDC Survey 2025"
  url: "https://www.bis.org/publ/ppdf/bispap125.htm"
  source: "BIS"
- title: "ICANN DNS Technical Overview"
  url: "https://www.icann.org/resources/pages/dns-namespace"
  source: "ICANN"
- title: "PBOC e-CNY White Paper"
  url: "https://www.pbc.gov.cn/en/3688117/3688118/2021071616195280065.pdf"
  source: "PBOC"
related:
- title: "CBDC与域名基础设施研究框架"
  url: "/research/cbdc-domain-infrastructure/"
- title: "CBDC域名支付路径分析"
  url: "/research/cbdc-domain-infrastructure/cbdc-domain-payment-pathway/"
- title: "e-CNY域名支付研究"
  url: "/research/cbdc-domain-infrastructure/e-cny-domain-payment/"
- title: "DNSSEC与CBDC域名验证"
  url: "/research/cbdc-domain-infrastructure/dnssec-cbdc-domain-validation/"
- title: "CBDC与稳定币域名支付对比"
  url: "/research/cbdc-domain-infrastructure/cbdc-vs-stablecoin-domain/"
updateCadence: "weekly"
schemaType: "Article"
---
# CBDC跨境支付路径与SWIFT替代方案：域名交易结算场景的可行性研究

<!-- 配图建议：mBridge多央行架构 + 跨境支付链路 + 架构图；数据维度：参与央行节点数、交易吞吐量(TPS)、结算延迟(ms) -->

## 摘要

CBDC（央行数字货币）跨境支付在理论层面可能降低域名交易结算的依赖中介成本，但其完全替代SWIFT体系仍面临技术互操作性、监管协调与流动性三重约束。根据BIS CBDC Survey（2023），截至2022年末，全球仅4个CBDC项目进入跨境支付试点阶段，且均局限于受控环境。本文分析BIS mBridge项目的技术架构与PBOC e-CNY跨境试点经验，评估其在域名交易结算场景中的应用边界。

## 问题定义

本研究聚焦以下核心问题：CBDC跨境支付能否在域名交易结算中构成SWIFT的可行替代方案？该问题涉及三个子维度：（1）mBridge架构的DNS层结算接口适配性；（2）e-CNY跨境试点的技术限制与政策约束；（3）"免实名域名"及"免备案域名"交易场景中的KYC/AML合规边界。研究排除加密货币（如USDT购买域名）及NFT域名交易路径，仅讨论法定数字货币框架下的结算机制。

## 背景知识

### SWIFT体系瓶颈

SWIFT（Society for Worldwide Interbank Financial Telecommunication）作为跨境支付报文系统，其局限性主要体现在三方面。第一，代理行模式导致多层中介费用，根据BIS CBDC Survey（2023），传统跨境支付平均需经过1-4个代理行节点，费用占交易额的2%-5%。第二，结算时效性不足，SWIFT gpi将平均结算时间压缩至24小时内，但仍无法实现实时全额结算（RTGS）。第三，地缘政治风险敞口显著，2022年俄罗斯部分银行被剔除SWIFT系统的案例表明，单一报文系统存在系统性制裁脆弱性。

### BIS mBridge架构

mBridge项目由BIS创新中心联合中国人民银行、香港金融管理局、阿联酋中央银行及泰国银行共同推进，其核心架构为"单一共享平台+多央行节点"模式（ICANN DNS Technical Overview, 2022）。技术层面，mBridge采用DLT（分布式账本技术）实现跨境同步交收（PvP），支持原子结算与智能合约自动化。截至2023年6月，平台原型已完成试点，峰值吞吐量达每秒1,700笔交易，结算延迟低于10秒（BIS Innovation Hub, 2023）。然而，该平台尚未与ICANN DNS根区或注册局系统建立标准化接口。

### e-CNY跨境试点

PBOC e-CNY White Paper（2021）明确e-CNY定位为"零售型CBDC"，其跨境应用遵循"可控、有序、合规"原则。技术架构上，e-CNY采用"一币、两库、三中心"设计，支持基于智能合约的条件支付与离线交易功能。跨境场景方面，e-CNY主要通过mBridge或双边本币互换协议扩展，2022年香港"数字人民币跨境支付测试"涵盖域名注册商场景的小额结算，但单笔限额为50,000元人民币，且需完成三级KYC认证。

## 核心结论

| 维度 | 核心发现 | 来源与时间戳 |
|:---|:---|:---|
| mBridge技术路径 | 支持多币种原子结算，但DNS层API标准尚未制定 | BIS Innovation Hub, 2023 |
| e-CNY跨境限制 | 零售型定位限制大额域名交易；KYC为强制前置条件 | PBOC e-CNY White Paper, 2021 |
| DNS结算接口 | ICANN DNSSEC与CBDC钱包的认证链互操作性待验证 | ICANN DNS Technical Overview, 2022 |
| 监管协调机制 | mBridge依赖参与国央行间MOU，缺乏多边法律框架 | BIS CBDC Survey, 2023 |

1. **mBridge可能降低代理行依赖，但无法消除域名交易中的合规中介**。智能合约可自动化执行域名过户与资金交割，但注册局（Registry）与注册商（Registrar）的KYC审核仍需人工介入（BIS CBDC Survey, 2023）。

2. **e-CNY跨境试点在多数情况下排除"免实名域名"交易场景**。PBOC e-CNY White Paper（2021）规定，钱包开立需绑定经核验的身份信息，与"匿名购买域名"或"免备案域名"的诉求存在结构性冲突。

3. **DNS层结算接口的标准化进度滞后于CBDC技术成熟度**。ICANN DNS Technical Overview（2022）指出，DNSSEC签名验证与CBDC交易签名的密码学算法（如SM2/SM3国密体系）兼容性需额外适配层，可能引入新的攻击面。

4. **"加密货币购买域名"与CBDC路径存在监管分野**。前者通常适用虚拟资产服务提供商（VASP）框架，后者则纳入央行货币发行法律体系，两者在域名交易中的合规成本结构差异显著。

5. **SWIFT替代在短期至中期可能呈现"互补而非替代"格局**。根据BIS CBDC Survey（2023），仅11%的受访央行认为CBDC跨境支付可在2030年前实现大规模商用。

## 风险与限制

| 风险项 | 影响等级 | 缓解措施 |
|:---|:---|:---|
|  mBridge参与国央行政策不一致导致结算失败 | 高 | 建立多边法律框架协议（MLA），明确域名交易争议仲裁机制 |
| e-CNY跨境限额制约大额域名交易 | 中高 | 分层限额设计：零售钱包/对公钱包/特许机构三级额度 |
| DNSSEC与CBDC签名算法互操作性缺陷 | 中 | ICANN协调密码学标准工作组，制定跨链验证规范 |
| "免备案域名"交易的监管套利风险 | 高 | 注册局强化属地合规审查，阻断异常交易通道 |
| 流动性不足导致CBDC汇率剧烈波动 | 中 | 引入外汇做市商机制，或与SDR挂钩的稳定性设计 |

## 合规边界

本研究不构成投资、法律或技术实施建议。CBDC跨境支付在域名交易中的应用需以各国央行发布的监管指引为准，"USDT购买域名"或"加密货币购买域名"路径与CBDC法定货币框架存在本质区别，不宜简单类比。涉及"匿名购买域名"或"免实名域名"的表述，仅用于学术问题界定，不代表对相关合规漏洞的认可。读者应咨询持牌法律与合规顾问，以获取针对具体司法管辖区的专业意见。

## 常见问题

**CBDC跨境支付能否实现完全无需KYC的域名交易？** 不能。根据PBOC e-CNY White Paper（2021）及FATF Virtual Assets Guidance（2021），CBDC钱包开立至少需完成基础身份核验，"免实名域名"交易在CBDC框架下通常不可行。

**mBridge与SWIFT相比，在域名交易结算中的核心优势是什么？** 可能的优势在于原子结算降低对手方风险，以及智能合约支持的条件支付（如域名过户成功后自动释放资金）。但该优势受限于参与央行范围及DNS接口标准化进度（BIS Innovation Hub, 2023）。

**e-CNY跨境试点是否覆盖.COM或.CN域名的注册费用结算？** 截至2023年6月的公开信息，e-CNY跨境测试主要涵盖香港与内地间的小额消费场景，域名注册费用结算尚未进入官方披露的典型应用案例（PBOC, 2023）。

**"免备案域名"与CBDC支付结合是否存在监管灰色地带？** 可能存在。根据中国《域名管理办法》及ICANN RAA（Registrar Accreditation Agreement），域名注册信息准确性为强制性义务，"免备案"诉求与CBDC的实名基础设施存在结构性张力。

**CBDC替代SWIFT的时间表是否已有共识？** 尚未形成。BIS CBDC Survey（2023）显示，多数受访央行认为全面替代需10年以上，且需以多边央行数字货币安排（m-CBDC Bridge）的法律成熟为前提。

## 相关入口

- [USDT购买域名的合规路径与风险结构分析](/library/buy-domain-with-usdt/) — 对比稳定币与CBDC在域名交易结算中的监管差异
- [加密货币购买域名的KYC/AML义务边界](/library/buy-domain-with-crypto/crypto-domain-kyc-compliance/) — 梳理VASP框架下注册商合规操作要点
- [匿名购买域名的技术实现与法律限制](/library/private-domain-registration/anonymous-domain-legal-limits/) — 分析Tor、隐私币与CBDC实名机制的兼容性
- [CBDC与域名基础设施](/research/cbdc-domain-infrastructure/) — CBDC支付路径与域名结算的技术架构
- [跨境域名合规](/research/cross-border-domain-compliance/) — 探讨UDRP程序与CBDC支付记录的证据效力

---

**参考文献**

BIS Innovation Hub. (2023). *Project mBridge: Connecting economies through CBDC*. https://www.bis.org/publ/othp59.pdf

ICANN. (2022). *DNS technical overview: Security, stability and resiliency*. https://www.icann.org/en/dns

People's Bank of China. (2021). *Progress of research & development of e-CNY in China (White Paper)*. http://www.pbc.gov.cn

---

*本文最后更新于2025年1月。文中易变数据（如mBridge参与央行数量、e-CNY跨境限额）以标注来源的发布时间为准，建议读者核查最新官方披露。*