---
title: "DoH vs DoT Protocol Comparison: Security and Deployment Analysis of Encrypted DNS Transport"
description: "DoH vs DoT encrypted DNS: technical differences, security properties, and deployment via ICANN DNS, DNSSEC, and NIST SP 800-81."
slug: "dns-security-governance/doh-dot-protocol"
section: "research"
cluster: "dns-security-governance"
type: "longtail"
language: "en"
publishedAt: "2026-05-07"
image: "/images/dns-security-governance/dns-security-governance/doh-dot-protocol.svg"
updatedAt: "2026-05-07"
author: "Web3 Domain Institute Editorial Team"
reviewer: "Domain Infrastructure Research Desk"
tags:
- "DoH DoT"
- "DNS encryption"
- "DNS security"
- "DNS over HTTPS"
- "domain governance"
keywords:
 primary: "DoH DoT"
 secondary:
   - "DNS over HTTPS"
   - "DNS over TLS"
   - "DNS security"
   - "DNS encryption protocol"
   - "domain governance"
riskLevel: "low"
index: true
audience:
- "Technical professionals"
- "Researchers"
- "Domain holders"
summary: "DNS over HTTPS (DoH) and DNS over TLS (DoT) are two mainstream DNS encryption protocols, transmitting DNS queries over HTTPS (port 443) and TLS (port 853) respectively. DoH is harder for middleboxes to detect and filter; DoT offers advantages in operational observability. Both should be used alongside ICANN DNSSEC for end-to-end DNS security."
faqs:
-
  question: "Which is more secure, DoH or DoT?"
  answer: "Both offer equivalent security at the transport encryption level, using TLS encryption. DoH is harder for middlebox interference since it mimics HTTPS traffic, but this also reduces network operational observability. DoT uses a dedicated port, making enterprise network management easier. Security depends on deployment scenario and threat model."
-
  question: "Can DoH/DoT replace DNSSEC?"
  answer: "No. DoH/DoT protect the confidentiality and integrity of the transport channel, preventing eavesdropping or tampering of queries. DNSSEC protects the origin authentication and integrity of DNS data itself. They are complementary, and ICANN recommends deploying both."
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
  title: "DNS Security and Domain Governance Research"
  url: "/research/dns-security-governance/"
-
  title: "DNS over HTTPS Research"
  url: "/research/dns-security-governance/dns-over-https/"
-
  title: "DNSSEC Deployment Analysis"
  url: "/research/dns-security-governance/dnssec/"
-
  title: "DNSSEC Check Guide"
  url: "/tools/dnssec-check-guide/"
-
  title: "2026 DNS Security and Domain Governance Report"
  url: "/reports/2026-dns-security-governance-report/"
updateCadence: "weekly"
schemaType: "Article"
---

## Summary

DNS over HTTPS (DoH, RFC 8484) and DNS over TLS (DoT, RFC 7858) are the two mainstream DNS encryption transport protocols, designed to address the eavesdropping and tampering risks inherent in traditional plaintext DNS queries. DoH encapsulates DNS messages using the HTTPS protocol (port 443), mixing with existing web traffic; DoT uses dedicated TLS connections (port 853) for DNS queries. Both are equivalent in encryption strength but differ significantly in traffic observability, network management, and deployment complexity. Per NIST SP 800-81 Rev. 3 guidance, DoH/DoT should be deployed in conjunction with ICANN DNSSEC to achieve a complete DNS security architecture.

## Problem Definition

This page examines the technical characteristics, security differences, and deployment applicability of DoH and DoT DNS encryption protocols, focusing on the differentiated impact of these two protocols on the domain security ecosystem under the ICANN DNS governance framework, and their positioning within NIST security deployment guidelines.

## Background

Traditional DNS queries are transmitted in plaintext over UDP port 53, allowing any network middlebox to read or tamper with query contents. ICANN listed DNS encryption as a key direction for DNS evolution in 2019. The IETF subsequently standardized the DoT (RFC 7858, 2016) and DoH (RFC 8484, 2018) protocols.

NIST SP 800-81 Rev. 3 (published 2024) explicitly recommends that federal agencies deploy DNS encryption protocols and incorporates DoH/DoT into the DNS security deployment baseline. ICANN DNSSEC verifies the origin authenticity and data integrity of DNS responses through digital signatures, forming a complementary security layer with transport-layer encryption (DoH/DoT).

## Core Conclusions

| Feature | DoH (RFC 8484) | DoT (RFC 7858) |
|---|---|---|
| Transport protocol | HTTPS/TLS (port 443) | TLS (port 853) |
| Traffic characteristics | Mixed with web traffic | Identifiable on dedicated port |
| Middlebox interference resistance | High | Medium |
| Operational observability | Low | High |
| Enterprise network management | Difficult | Easier |
| Deployment complexity | Medium (requires HTTP/2 stack) | Low (requires only TLS) |
| Browser support | Chrome/Firefox/Edge native | Requires system-level configuration |

1. **DoH and DoT offer equivalent encryption strength**: Both use TLS 1.2/1.3 encryption with no essential difference in data transport confidentiality and integrity.
2. **DoH's stealth is a double-edged sword**: DoH traffic mixes with regular HTTPS traffic, making it difficult for network middleboxes to detect and filter DNS queries, enhancing censorship resistance but reducing DNS observability and security monitoring capabilities in enterprise networks.
3. **DoT is more suitable for controlled network environments**: Enterprise networks and institutions typically prefer DoT because its dedicated port facilitates policy management and traffic auditing.
4. **DoH/DoT and DNSSEC are complementary**: DoH/DoT protect transport channel security; DNSSEC protects the authenticity of DNS data itself. Together they form the DNS security baseline recommended by ICANN.

## Risks and Limitations

| Risk Factor | Impact Level | Mitigation Measures |
|---|---|---|
| DoH bypassing enterprise DNS security policies | Medium | Deploy enterprise DoH policies; designate trusted resolvers |
| DoT port blocked by firewall | Low | Configure firewall to allow port 853 outbound |
| Encrypted DNS resolver centralization | Medium | Support multi-resolver deployment; avoid single-point dependency |
| DNSSEC validation skipped in encrypted tunnels | High | Ensure resolvers perform DNSSEC validation simultaneously |
| Protocol fragmentation increasing operational complexity | Low | Choose single protocol priority deployment based on scenario |

## Compliance Boundaries

This analysis is based on ICANN DNS technical standards, ICANN DNSSEC deployment guidelines, and the NIST SP 800-81 Rev. 3 security deployment framework. DoH/DoT protocol deployment should follow cybersecurity regulations in the applicable jurisdiction. Implementing DoH policies in enterprise environments requires balancing security monitoring needs with user privacy protection. This page does not constitute a recommendation for any specific DNS encryption scheme; domain holders should choose appropriate deployment solutions based on their threat model.

## Related Entries

- [DNS Security and Domain Governance Research](/research/dns-security-governance/) — Comprehensive overview of DNS security
- [DNS over HTTPS Research](/research/dns-security-governance/dns-over-https/) — In-depth DoH protocol analysis
- [DNSSEC Deployment Analysis](/research/dns-security-governance/dnssec/) — Detailed DNSSEC digital signature mechanisms
- [DNSSEC Check Guide](/tools/dnssec-check-guide/) — Verify domain DNSSEC deployment status
- [2026 DNS Security and Domain Governance Report](/reports/2026-dns-security-governance-report/) — Latest DNS security trend tracking
