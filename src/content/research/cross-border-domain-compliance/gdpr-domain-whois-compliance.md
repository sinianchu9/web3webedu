---
title: "GDPR对域名WHOIS数据跨境传输的合规要求分析"
description: "分析GDPR对域名WHOIS数据跨境传输的合规要求，涵盖ICANN临时规范、标准合同条款、RDAP替代机制与FATF数据本地化趋势。"
image: "/images/cross-border-domain-compliance/cross-border-domain-compliance/gdpr-domain-whois-compliance.svg"
slug: "cross-border-domain-compliance/gdpr-domain-whois-compliance"
section: "research"
cluster: "cross-border-domain-compliance"
type: "longtail"
language: "zh-CN"
publishedAt: "2026-05-08"
updatedAt: "2026-05-08"
author: "Web3 Domain Institute Editorial Team"
reviewer: "Domain Infrastructure Research Desk"
tags:
 - "GDPR"
 - "WHOIS跨境传输"
keywords:
 primary: "GDPR域名WHOIS跨境传输"
 secondary:
 - "ICANN临时规范"
 - "标准合同条款"
 - "RDAP替代"
riskLevel: "high"
index: true
audience:
 - "域名持有者"
 - "研究者"
 - "Web3创业者"
 - "技术人员"
summary: "GDPR将域名WHOIS数据中的注册人个人信息视为受保护个人数据，限制其向欧盟境外传输。ICANN 2018年临时规范要求注册商默认隐藏WHOIS个人数据，与执法机构的访问需求产生持续张力。"
faqs:
 -
  question: "域名WHOIS数据是否全部受GDPR保护？"
  answer: "并非全部。WHOIS中注册人姓名、邮箱、电话等个人信息受GDPR保护；域名本身、注册日期、到期日期等非个人数据不在GDPR保护范围内。注册商需区分处理这两类数据。"
 -
  question: "ICANN临时规范是否永久有效？"
  answer: "ICANN 2018年临时规范原定为临时措施，但至今仍在执行。ICANN社区正在推进永久性注册目录服务（RDS）政策制定，但尚未达成共识。临时规范的长期法律稳定性存在不确定性。"
references:
 -
  title: "ICANN: Registrar Accreditation Agreement"
  url: "https://www.icann.org/resources/pages/approved-with-specs-2013-09-17-en"
  source: "ICANN"
 -
  title: "FATF: Updated Guidance on Virtual Assets"
  url: "https://www.fatf-gafi.org/en/publications/Fatfgeneral/Updated-Guidance-va-vasp.html"
  source: "FATF"
 -
  title: "EUR-Lex: General Data Protection Regulation"
  url: "https://eur-lex.europa.eu/eli/reg/2016/679/oj"
  source: "EU"
related:
 -
  title: "跨境域名合规研究"
  url: "/research/cross-border-domain-compliance/"
 -
  title: "域名KYC司法管辖区比较"
  url: "/research/cross-border-domain-compliance/kyc-jurisdiction-comparison/"
 -
  title: "域名争议解决机制"
  url: "/research/cross-border-domain-compliance/domain-dispute-resolution/"
 -
  title: "域名隐私保护检查清单"
  url: "/tools/domain-privacy-checklist/"
 -
  title: "2026跨境域名合规报告"
  url: "/reports/2026-cross-border-domain-compliance-report/"
updateCadence: "weekly"
schemaType: "Article"
---

## 摘要

GDPR（通用数据保护条例）将域名WHOIS数据中包含的注册人姓名、邮箱、电话等信息定义为受保护的个人数据，严格限制其向欧盟/欧洲经济区（EEA）境外传输。2018年ICANN发布的临时规范要求注册商默认隐藏WHOIS中的个人数据，导致传统WHOIS查询系统功能大幅缩减。本页分析GDPR对域名WHOIS数据跨境传输的合规要求、ICANN的应对措施，以及RDAP替代机制的发展现状。

## 问题定义

本页聚焦的核心问题是：GDPR如何约束域名注册人个人数据的跨境传输？ICANN临时规范与GDPR的交互产生了哪些合规张力？域名注册商在同时满足ICANN RAA和GDPR要求时面临哪些实际操作困境？

本页不讨论GDPR的一般合规指南，也不涉及欧盟成员国国内法的具体差异。

## 背景知识

### WHOIS数据的个人信息属性

传统WHOIS数据库包含域名注册人的姓名、组织、地址、邮箱、电话等信息。在GDPR框架下，这些信息构成"个人数据"（Personal Data），即任何已识别或可识别的自然人的信息。即使注册人以企业名义注册域名，若WHOIS联系人字段包含自然人信息（如行政联系人、技术联系人的个人邮箱），该部分数据仍受GDPR保护。

GDPR第五章（第44—49条）确立了个人数据跨境传输的基本原则：个人数据原则上不得向未获得欧盟"充分性认定"（Adequacy Decision）的第三国传输，除非满足特定例外条件（如标准合同条款、约束性企业规则、明确同意等）。

### ICANN 2018年临时规范

2018年5月GDPR生效前夕，ICANN董事会通过了临时规范（Temporary Specification for gTLD Registration Data），要求注册商在默认情况下隐藏WHOIS输出中的注册人个人数据，仅保留注册商名称、注册日期、到期日期等非个人数据。该规范旨在帮助注册商同时遵守GDPR和ICANN RAA的数据披露义务，但引发了执法机构、知识产权持有者和安全研究者对数据访问能力受限的广泛争议。

## 核心结论

| 合规维度 | GDPR要求 | ICANN RAA要求 | 张力点 |
|---|---|---|---|
| 默认WHOIS输出 | 隐藏个人数据 | 公开注册人信息 | RAA与GDPR直接冲突 |
| 执法机构访问 | 需合法依据 | RAA要求配合披露 | 披露程序标准不一 |
| 跨境数据传输 | 需充分性认定或SCC | 注册商全球运营需要数据流动 | 数据本地化要求vs全球运营 |
| RDAP替代 | 个人数据仍需保护 | RDAP分层访问机制 | 分层访问标准尚未统一 |
| 数据留存 | 最小必要原则 | RAA要求特定留存期 | 留存期限理解分歧 |

1. **GDPR与ICANN RAA的直接冲突是当前合规困境的根源。** RAA要求注册商在WHOIS中公开注册人信息，而GDPR要求默认隐藏个人数据。ICANN临时规范通过默认隐藏+按需披露的分层模式暂时调和了这一冲突，但该规范的法律稳定性存疑。

2. **标准合同条款（SCC）是注册商跨境传输WHOIS数据的主要合法工具。** 欧盟委员会2021年修订的SCC模板为数据控制者向第三国传输个人数据提供了合同法层面的合规路径。注册商若需将欧盟注册人数据传输至EEA境外（如美国总部），通常需要签署SCC并完成传输影响评估（TIA）。

3. **欧盟—美国数据隐私框架（DPF）仅部分缓解传输压力。** 2023年生效的EU-US Data Privacy Framework为认证企业提供了从欧盟向美国传输个人数据的合法通道，但该框架的法律持久性存在争议（前两次框架均被欧盟法院否决）。

4. **RDAP分层访问机制是长期解决方案的技术基础。** ICANN正在推动从WHOIS向RDAP（Registration Data Access Protocol）的迁移，RDAP支持基于访问者身份的分层数据披露——普通公众获取脱敏数据，经验证的执法机构和知识产权持有者获取完整数据。该机制的技术实现已基本就绪，但访问授权标准仍在社区讨论中。

5. **FATF虚拟资产指引对WHOIS数据本地化的影响值得关注。** FATF要求虚拟资产服务提供商（VASP）保存可识别交易双方的信息，部分司法管辖区据此要求数据本地化存储。若注册商被认定为VASP，其WHOIS数据可能面临本地化存储要求，与GDPR的数据最小化原则形成新的张力。

## 风险与限制

| 风险项 | 影响等级 | 缓解措施 |
|---|---|---|
| ICANN临时规范被废止 | 高 | 关注ICANN RDS政策进程；准备合规调整方案 |
| SCC传输影响评估不通过 | 中 | 定期更新TIA；选择数据保护水平较高的第三国接收方 |
| DPF被欧盟法院否决 | 中 | 不依赖DFP作为唯一传输机制；备选SCC路径 |
| 数据本地化强制要求 | 中 | 评估各司法管辖区数据本地化立法动态 |
| WHOIS替代方案延迟 | 低 | 参与ICANN社区RDAP政策讨论 |

## 合规边界

本页内容仅限于GDPR对域名WHOIS数据跨境传输要求的法律分析，不构成法律合规建议。域名注册商应结合自身运营所在司法管辖区的法律要求，咨询专业法律顾问制定具体合规方案。文中关于ICANN政策的描述基于公开文件，不代表对政策最终走向的预测。

## 相关入口

- [跨境域名合规研究](/research/cross-border-domain-compliance/)：跨境域名注册合规的综合研究框架
- [域名KYC司法管辖区比较](/research/cross-border-domain-compliance/kyc-jurisdiction-comparison/)：不同司法管辖区域名注册KYC要求对比
- [域名争议解决机制](/research/cross-border-domain-compliance/domain-dispute-resolution/)：UDRP等跨境域名争议解决程序分析
- [域名隐私保护检查清单](/tools/domain-privacy-checklist/)：评估域名注册隐私保护合规状态
- [2026跨境域名合规报告](/reports/2026-cross-border-domain-compliance-report/)：跨境域名合规行业数据与政策趋势
