---
title: "mBridge跨境CBDC支付中的域名命名体系与DNS基础设施风险"
description: "Analyzes the domain naming system in mBridge cross-border CBDC payments and its reliance on DNS infrastructure"
image: "/images/cbdc-domain-infrastructure/mbridge-cbdc-dns-naming-infrastructure-risk.svg"
slug: "cbdc-domain-infrastructure/mbridge-cbdc-dns-naming-infrastructure-risk"
section: "research"
cluster: "cbdc-domain-infrastructure"
type: "longtail"
language: "en"
publishedAt: "2026-06-30"
updatedAt: "2026-06-30"
author: "Web3 Domain Institute Editorial Team"
reviewer: "Domain Infrastructure Research Desk"
tags:
- "CBDC"
- "mBridge"
keywords:
  primary: "CBDC domain infrastructure"
  secondary:
  - "mBridge DNS risk"
  - "cross-border payment"
riskLevel: "medium"
index: true
audience:
- "Domain holders"
- "Researchers"
- "Web3 entrepreneurs"
- "Technical professionals"
summary: "This article analyzes the domain naming system in mBridge CBDC payments and DNS infrastructure dependencies"
faqs:
- question: "Does mBridge completely eliminate reliance on traditional DNS?"
  answer: "mBridge uses distributed ledger for core bookkeeping, but its network layer still relies on DNS for node discovery"
- question: "How do DNS infrastructure risks affect cross-border CBDC payments?"
  answer: "DNS hijacking or resolution failure may delay or redirect payment instructions, though digital signatures can detect tampering"
references:
- title: "Project mBridge: Reaching the Minimum Viable Product"
  url: "https://www.bis.org/publ/bisdb13.pdf"
  source: "BIS"
- title: "Security Architecture for Digital Fiat Currency Systems"
  url: "https://www.itu.int/pub/T-TUT-FGDC-2022"
  source: "ITU"
- title: "ICANN DNS Security and Stability"
  url: "https://www.icann.org/resources/pages/dns-security-2012-en"
  source: "ICANN"
related:
- title: "CBDC跨境支付与域名基础设施"
  url: "/research/cbdc-domain-infrastructure/cbdc-cross-border-settlement-dns-resolution-risk/"
- title: "DNSSEC协议与DNS安全"
  url: "/research/dns-security-governance/dnssec-protocol-overview/"
- title: "Domain Registration Privacy Protection Tools"
  url: "/library/private-domain-registration/"
- title: "DNS Security and Domain Governance"
  url: "/research/dns-security-governance/"
updateCadence: "weekly"
schemaType: "Article"
---

Domain Naming System and DNS Infrastructure Risks in mBridge Cross-Border CBDC Payments

The evolution of financial technology has facilitated the development of multi-central bank digital currency (mCBDC) arrangements, with Project mBridge emerging as a prominent framework for cross-border settlements. As a collaborative effort between the Bank for International Settlements (BIS) Innovation Hub and several central banks, mBridge utilizes a bespoke distributed ledger technology (DLT) to streamline international payments. However, the reliance of such systems on underlying internet protocols, particularly the Domain Naming System (DNS), introduces a layer of infrastructure risk that warrants academic scrutiny. The stability of the [network topology](/cbdc-domain-infrastructure/network-topology/) in mBridge is often dependent on the integrity of domain resolution processes, which may be susceptible to various forms of cyber interference.

The mBridge platform is designed to provide a common technical substrate for participating jurisdictions to issue and exchange their respective CBDCs. While the ledger itself may be decentralized, the communication between participating nodes and the access points for commercial banks typically rely on the standard Internet Protocol (IP) suite. In this context, DNS serves as a directory service that translates human-readable domain names into the IP addresses required for machine-to-machine communication. Because the mBridge architecture involves multiple sovereign entities, the resolution of these addresses frequently crosses jurisdictional boundaries, potentially exposing the system to [cybersecurity vulnerabilities](/cbdc-domain-infrastructure/cybersecurity-vulnerabilities/) inherent in the global DNS infrastructure.

One of the primary risks associated with DNS in the context of mBridge is the potential for DNS hijacking or cache poisoning. In such scenarios, an adversary may attempt to redirect traffic intended for a legitimate mBridge node to a malicious server. If successful, this could facilitate man-in-the-middle (MITM) attacks, where transaction data or authentication credentials might be intercepted. Although the mBridge ledger employs cryptographic signatures to verify the authenticity of transactions, the disruption of the underlying resolution process may result in significant service latency or the temporary isolation of specific nodes. The BIS has noted that the operational resilience of CBDC systems is often as critical as their cryptographic security, as outages in the communication layer can undermine public trust in the payment system (BIS, 2022).

Furthermore, the threat of Distributed Denial of Service (DDoS) attacks against DNS infrastructure remains a significant concern for cross-border payment systems. If the authoritative name servers responsible for resolving the domains of participating central banks are overwhelmed by traffic, the ability of nodes to locate each other may be compromised. Such an event could lead to a fragmentation of the mBridge network, where certain participants are unable to finalize settlements. To mitigate these risks, it is often suggested that central banks adopt [resilience protocols](/cbdc-domain-infrastructure/resilience-protocols/) that include redundant DNS providers and the use of Anycast routing to distribute traffic loads. However, the complexity of managing these configurations across multiple jurisdictions may present ongoing operational challenges.

The implementation of Domain Name System Security Extensions (DNSSEC) is frequently cited as a method to enhance the integrity of domain resolution. DNSSEC provides a mechanism for validating that the DNS data received has not been tampered with during transit. For a high-value payment system like mBridge, the adoption of [DNSSEC implementation](/cbdc-domain-infrastructure/dnssec-implementation/) may be viewed as a prudent measure to prevent spoofing attacks. Nevertheless, DNSSEC does not address availability risks and can, in some instances, increase the size of DNS responses, which might be exploited in amplification attacks. Consequently, while DNSSEC may improve the security posture of the mBridge ecosystem, it is typically regarded as one component of a broader defense-in-depth strategy rather than a comprehensive solution.

Geopolitical considerations also play a role in the DNS risk profile of mBridge. Since the management of the DNS root zone and the governance of top-level domains (TLDs) are influenced by international organizations and specific national entities, there is a theoretical risk that access to certain domains could be restricted or altered due to political tensions. For a cross-border payment system intended to enhance financial sovereignty, the reliance on a globally distributed and politically sensitive infrastructure like DNS creates a paradox. Some participants may explore the use of private naming systems or decentralized identity (DID) frameworks to reduce their dependence on the public DNS, thereby maintaining greater [sovereign control](/cbdc-domain-infrastructure/sovereign-control/) over their financial communications.

The International Monetary Fund (IMF) has emphasized that the interconnectedness of CBDC platforms increases the potential for systemic risk, where a failure in one component—such as the naming service—could propagate through the entire network (IMF, 2023). In the case of mBridge, where real-time liquidity management is a core feature, even brief interruptions in domain resolution could have cascading effects on the liquidity positions of participating banks. The coordination of incident response protocols across different time zones and legal frameworks is therefore a necessary consideration for the long-term viability of the project.

In conclusion, while Project mBridge represents a significant advancement in the efficiency of cross-border payments, the underlying DNS infrastructure introduces vulnerabilities that may impact the system's availability and integrity. The potential for cache poisoning, DDoS attacks, and geopolitical interference suggests that the reliance on traditional domain resolution methods should be carefully managed. By integrating advanced security standards like DNSSEC and exploring alternative resolution architectures, participating central banks may enhance the resilience of the mBridge platform. As the project moves toward broader adoption, the continuous assessment of infrastructure risks will likely remain a priority for maintaining the stability of the international monetary system.

References

Bank for International Settlements (BIS). (2022). *Project mBridge: Connecting economies through CBDC*. BIS Innovation Hub. Retrieved from https://www.bis.org/publ/othp59.pdf

International Monetary Fund (IMF). (2023). *Cyber Resilience in the Financial Sector: A Review of International Standards and Practices*. IMF Policy Paper. Retrieved from https://www.imf.org/en/Publications/Policy-Papers/Issues/2023/06/20/Cyber-Resilience-in-the-Financial-Sector-535012

Financial Stability Board (FSB). (2023). *Enhancing Cross-border Payments: G20 Roadmap for addressing the challenges of cost, speed, access and transparency*. FSB Reports. Retrieved from https://www.fsb.org/wp-content/uploads/P091023.pdf