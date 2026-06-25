---
title: "mBridge Cross-border CBDC Payment Domain Naming System and DNS Infrastructure Analysis"
description: "Research on domain naming and DNS infrastructure in mBridge CBDC payments, analyzing multi-CBDC platform impact on domain governance."
image: "/images/cbdc-domain-infrastructure/mbridge-cbdc-domain-naming-dns.svg"
slug: "cbdc-domain-infrastructure/mbridge-cbdc-domain-naming-dns"
section: "research"
cluster: "cbdc-domain-infrastructure"
type: "longtail"
language: "en"
publishedAt: "2026-06-25"
updatedAt: "2026-06-25"
author: "Web3 Domain Institute Editorial Team"
reviewer: "Domain Infrastructure Research Desk"
tags:
- "CBDC"
- "mBridge"
- "DNS Infrastructure"
- "Cross-border Payment"
- "Domain Governance"
keywords:
  primary: "mBridge Domain Naming System"
  secondary:
  - "CBDC Cross-border Payment"
  - "DNS Infrastructure"
  - "Domain Security"
  - "Cross-border Finance"
riskLevel: "medium"
index: true
audience:
- "Domain Holders"
- "FinTech Researchers"
- "Policy Makers"
- "Cross-border Payment Professionals"
summary: "This article analyzes the relationship between domain naming systems and DNS infrastructure in mBridge cross-border CBDC payments, exploring the potential impact of multi-CBDC platforms on domain governance and compliance boundaries."
faqs:
- question: "What is mBridge?"
  answer: "mBridge is a cross-border CBDC payment platform developed by BIS Innovation Hub, HKMA, PBOC and others, enabling real-time cross-border CBDC transfers."
- question: "What role does DNS play in CBDC payments?"
  answer: "DNS provides address resolution and service discovery for CBDC payment networks, ensuring cross-border payment instructions are routed accurately to participating nodes."
- question: "What compliance challenges does CBDC domain naming face?"
  answer: "CBDC domain naming must comply with ICANN governance frameworks while meeting FATF anti-money laundering requirements, involving complex issues of data sovereignty and cross-border regulatory coordination."
references:
- title: "BIS CBDC Framework"
  url: "https://www.bis.org/publ/bcbs_pap.htm"
  source: "BIS"
- title: "ICANN DNS Security"
  url: "https://www.icann.org/resources/pages/dns-security-2012-02-25-en"
  source: "ICANN"
- title: "PBOC e-CNY Whitepaper"
  url: "https://www.pbc.gov.cn/en/8007297/index.html"
  source: "PBOC"
related:
- title: "CBDC and Domain Infrastructure"
  url: "/research/cbdc-domain-infrastructure/"
- title: "DNS Security and Domain Governance"
  url: "/research/dns-security-governance/"
- title: "Cross-border Domain Compliance"
  url: "/research/cross-border-domain-compliance/"
updateCadence: "monthly"
schemaType: "Article"
---

**Abstract**

The evolution of the mBridge project, a multi-lateral central bank digital currency (mCBDC) platform, necessitates a robust and scalable naming infrastructure to facilitate cross-border settlements. This article analyzes the integration of domain naming systems (DNS) within the mBridge framework, exploring how central banks, including the PBOC for e-CNY, utilize specialized naming conventions to resolve ledger addresses. By aligning with ICANN DNS standards while maintaining sovereign control, mBridge should enhance the efficiency of multi-currency transactions. The analysis identifies that a decentralized naming approach may offer superior resilience compared to centralized legacy systems, provided that interoperability across diverse legal jurisdictions is maintained through a unified naming protocol.

**Problem Definition**

The primary challenge in cross-border CBDC payments involves the identification and resolution of participating entities across disparate ledgers. Traditional payment systems rely on SWIFT codes and IBANs, which often lack the granularity and programmability required for DLT-based environments. Within the mBridge ecosystem, the absence of a standardized domain naming system may lead to increased operational friction and higher risks of transaction errors. There is a critical need to bridge the gap between human-readable identifiers and cryptographic public keys without compromising the security or sovereign autonomy of participating central banks. Furthermore, the integration should align with global internet standards established by ICANN while addressing the specific regulatory requirements of the financial sector.

**Background**

The mBridge project, facilitated by the BIS Innovation Hub in collaboration with the Hong Kong Monetary Authority (HKMA), the Central Bank of the United Arab Emirates (CBUAE), the Digital Currency Institute of the People's Bank of China (PBOC), and the Bank of Thailand, represents a frontier in mCBDC infrastructure. As the platform transitions toward a Minimum Viable Product (MVP) stage, the technical architecture focuses on a bespoke blockchain—the mBridge Ledger. A significant component of this architecture involves how nodes and accounts are addressed. For instance, the PBOC e-CNY system utilizes a tiered identifier structure that should be compatible with international naming standards to allow for seamless cross-border interaction. Simultaneously, the global DNS overseen by ICANN provides the foundational logic for name resolution on the internet, offering a template for how financial domains might be structured to support secure, hierarchical, and delegated naming authorities within a multilateral financial network.

**Core Findings**

The implementation of a Domain Naming System within the mBridge platform reveals several critical technical and strategic advantages. These findings are summarized in the table below:

| Finding Category | Description | Strategic Impact |
| :--- | :--- | :--- |
| **Hierarchical Namespace** | mBridge should utilize a hierarchical naming structure (e.g., `.mbridge` or jurisdictional TLDs like `.cn.mb`) to delegate authority. | Enhances sovereign control and local administrative autonomy over national CBDC nodes. |
| **Hybrid Resolution** | Integration with ICANN DNS protocols may be combined with on-chain resolution mechanisms to reduce latency. | Supports high-frequency settlement while maintaining compatibility with standard web browsers and APIs. |
| **DNSSEC Integration** | The application of Domain Name System Security Extensions (DNSSEC) is likely to provide cryptographic proof of origin for naming data. | Reduces the risk of "man-in-the-middle" attacks and unauthorized redirection of payment instructions. |
| **Interoperable Identifiers** | Mapping e-CNY identifiers to a standardized mBridge naming format facilitates smoother cross-ledger communication. | Simplifies the user experience for commercial banks and reduces the technical barrier to entry for new participants. |

**Risks and Limitations**

Despite the benefits, the reliance on DNS-based infrastructure in a CBDC context introduces specific risks that should be carefully managed.

| Risk Factor | Description | Mitigation Potential |
| :--- | :--- | :--- |
| **Geopolitical Fragmentation** | Differences in DNS governance between participating nations could lead to "split-horizon" resolution issues. | Collaborative governance frameworks within the mBridge steering committee should align naming policies. |
| **Centralization Sensitivity** | Over-reliance on ICANN-managed root zones might be perceived as a risk to financial sovereignty by some participants. | Implementing a private or consortium-managed root zone for the mBridge network may enhance resilience. |
| **Resolution Latency** | Traditional DNS lookups may introduce delays that are incompatible with real-time gross settlement (RTGS) requirements. | Caching mechanisms and local resolution nodes within the mBridge ledger should be optimized for speed. |
| **Naming Squatting** | Unauthorized entities might attempt to register domains that mimic official central bank nodes. | A restricted registration policy and "know your customer" (KYC) requirements for domain owners should avoid such risks. |

**Compliance Boundaries**

The naming system within mBridge should operate within strict compliance boundaries to align with international AML/CFT (Anti-Money Laundering and Countering the Financing of Terrorism) standards. While naming systems simplify identification, they should avoid providing "pseudonymous" or "untraceable" transaction paths. Instead, the naming infrastructure should facilitate "traceable transparency," where domain identifiers are linked to verified legal entities within the mBridge governance framework.

Furthermore, the system should avoid attempts to "avoid reliance on KYC" protocols; rather, the DNS entries for financial institutions should serve as a pointer to verified identity credentials. Data localization requirements in jurisdictions like China mean that the resolution data for e-CNY nodes should be stored and managed in accordance with domestic data security laws. The integration of naming systems should enhance, not workaround (compliance risk), the ability of central banks to monitor cross-border flows and enforce capital controls when necessary.

In conclusion, a specialized DNS infrastructure for mBridge is a key component for the scaling of mCBDC payments. By adopting a hierarchical and secure naming convention, the platform can achieve the necessary balance between technical efficiency and sovereign oversight.

**Related Entries**

1. [Cross-border CBDC Interoperability](/cbdc-interop/)
2. [mBridge Governance Models](/mbridge-gov/)
3. [Decentralized Identifier (DID) Standards](/did-standards/)
4. [e-CNY System Architecture](/ecny-architecture/)
5. [DNSSEC in Financial Infrastructure](/dnssec-fin/)

**References**

*   Bank for International Settlements (BIS). (2022). *Project mBridge: Connecting economies through CBDC*. Retrieved from: https://www.bis.org/publ/othp59.pdf
*   ICANN. (2012). *What is the DNS?* Retrieved from: https://www.icann.org/resources/pages/dns-2012-02-25-en
*   People's Bank of China (PBOC). (2021). *Progress of Research & Development of E-CNY in China*. Retrieved from: http://www.pbc.gov.cn/en/3688110/3688172/4157443/4293696/index.html