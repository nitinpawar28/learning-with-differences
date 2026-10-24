---
code: KCSA
title: "Kubernetes and Cloud Native Security Associate"
credential: "Kubernetes and Cloud Native Security Associate (KCSA)"
provider: linux-foundation
tracks: [security, cloud]
clouds: [neutral]
level: beginner
tier: elective
stage: "4"
progress: planned
official_url: https://training.linuxfoundation.org/certification/kubernetes-and-cloud-native-security-associate-kcsa/
study_guide_url: https://github.com/cncf/curriculum/blob/master/KCSA%20Curriculum.pdf
outline_version: "2024-06-24"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. The Linux Foundation rates the exam as beginner level."
replaces: ""
replaced_by: ""
counterparts: []
objectives:
  - { id: "1", title: "Overview of Cloud Native Security", weight: "14%" }
  - { id: "1.1", title: "The 4Cs of cloud native security" }
  - { id: "1.2", title: "Cloud provider and infrastructure security" }
  - { id: "1.3", title: "Controls and frameworks" }
  - { id: "1.4", title: "Isolation techniques" }
  - { id: "1.5", title: "Artifact repository and image security" }
  - { id: "1.6", title: "Workload and application code security" }
  - { id: "2", title: "Kubernetes Cluster Component Security", weight: "22%" }
  - { id: "2.1", title: "API server" }
  - { id: "2.2", title: "Controller manager" }
  - { id: "2.3", title: "Scheduler" }
  - { id: "2.4", title: "Kubelet" }
  - { id: "2.5", title: "Container runtime" }
  - { id: "2.6", title: "KubeProxy" }
  - { id: "2.7", title: "Pod" }
  - { id: "2.8", title: "Etcd" }
  - { id: "2.9", title: "Container networking" }
  - { id: "2.10", title: "Client security" }
  - { id: "2.11", title: "Storage" }
  - { id: "3", title: "Kubernetes Security Fundamentals", weight: "22%" }
  - { id: "3.1", title: "Pod Security Standards" }
  - { id: "3.2", title: "Pod Security Admission" }
  - { id: "3.3", title: "Authentication" }
  - { id: "3.4", title: "Authorization" }
  - { id: "3.5", title: "Secrets" }
  - { id: "3.6", title: "Isolation and segmentation" }
  - { id: "3.7", title: "Audit logging" }
  - { id: "3.8", title: "Network policy" }
  - { id: "4", title: "Kubernetes Threat Model", weight: "16%" }
  - { id: "4.1", title: "Kubernetes trust boundaries and data flow" }
  - { id: "4.2", title: "Persistence" }
  - { id: "4.3", title: "Denial of service" }
  - { id: "4.4", title: "Malicious code execution and compromised applications in containers" }
  - { id: "4.5", title: "Attacker on the network" }
  - { id: "4.6", title: "Access to sensitive data" }
  - { id: "4.7", title: "Privilege escalation" }
  - { id: "5", title: "Platform Security", weight: "16%" }
  - { id: "5.1", title: "Supply chain security" }
  - { id: "5.2", title: "Image repository" }
  - { id: "5.3", title: "Observability" }
  - { id: "5.4", title: "Service mesh" }
  - { id: "5.5", title: "PKI" }
  - { id: "5.6", title: "Connectivity" }
  - { id: "5.7", title: "Admission control" }
  - { id: "6", title: "Compliance and Security Frameworks", weight: "10%" }
  - { id: "6.1", title: "Compliance frameworks" }
  - { id: "6.2", title: "Threat modeling frameworks" }
  - { id: "6.3", title: "Supply chain compliance" }
  - { id: "6.4", title: "Automation and tooling" }
---
## Exam format

All facts below are as of 2026-10-24, from the [KCSA exam page](https://training.linuxfoundation.org/certification/kubernetes-and-cloud-native-security-associate-kcsa/) and the Linux Foundation [multiple-choice exam FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-mc).

- **Question type:** multiple choice, online.
- **Number of questions:** not published on the exam page.
- **Duration:** 90 minutes.
- **Passing score:** 75% or above (the FAQ's rule for Linux Foundation multiple-choice exams).
- **Price:** USD 250 for the exam alone, or USD 495 bundled with a THRIVE-ONE annual subscription. Two attempts are included (one free retake).
- **Languages:** English only, per the Linux Foundation [language table](https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/language).
- **Delivery:** online, remotely proctored. Results by email within about 24 hours.
- **Eligibility and renewal:** 12 months to schedule and sit after purchase. Valid for 2 years. Under the CARE programme, passing CKS automatically renews KCSA.
- **Outline:** the curriculum PDF has no version number in its name. The date used above is the last change to that file in the CNCF curriculum repository (2024-06-24). The domains, weights and topics above match the PDF, plus one topic that only the exam page lists: **Authorization** (3.4), between Authentication and Secrets in Kubernetes Security Fundamentals.

Confirm price, length and languages before booking.

## What the exam really tests

KCSA tests whether you can recognise risks and the matching controls in a Kubernetes and cloud-native setup. You do not configure anything. Questions describe a situation or ask about a component, and you pick the safest or most correct answer.

- **Cloud-native security overview (14%).** The 4Cs model (Cloud, Cluster, Container, Code) and which layer owns which control; shared responsibility with the cloud provider; isolation by namespace, node, sandbox or VM; image registries, signing and scanning; and secure application code.
- **Cluster component security (22%).** What each component does and how it can be attacked or protected: the API server (authentication, authorization, admission, TLS), the controller manager and scheduler, the kubelet (its API, anonymous auth, the read-only port), the container runtime, kube-proxy, the Pod, etcd (encryption at rest, access only from the API server), CNI networking, `kubectl` clients and kubeconfig files, and storage.
- **Security fundamentals (22%).** Pod Security Standards (Privileged, Baseline, Restricted) and Pod Security Admission modes (enforce, audit, warn); authentication methods (certificates, tokens, OIDC); authorization modes, chiefly RBAC (and Node authorization for kubelets); Secrets and their limits (base64 is not encryption); namespace isolation and segmentation; audit logging levels and stages; NetworkPolicy semantics.
- **Threat model (16%).** Trust boundaries and data flows in a cluster, and the attacker goals the Kubernetes threat model lists: persistence, denial of service, code execution in a compromised container, network attackers, access to sensitive data and privilege escalation.
- **Platform security (16%).** Supply chain (SBOM, provenance, signing), image repositories, observability for security, service meshes and mutual TLS, the cluster's PKI and certificate rotation, connectivity, and admission control (validating and mutating webhooks, ValidatingAdmissionPolicy, policy engines).
- **Compliance and frameworks (10%).** Recognising compliance frameworks (CIS Benchmarks, NIST guidance), threat-modelling frameworks (STRIDE, MITRE ATT&CK for containers), supply-chain frameworks (SLSA) and the automation tools that check them.

Where candidates lose points: questions that list several controls that all sound reasonable, where only one addresses the specific threat named; confusing Pod Security Standards (the levels) with Pod Security Admission (the enforcement controller); and the threat-model domain, which uses vocabulary that is unfamiliar if you only have operations experience.

## Study strategy

1. **Foundations first.** Kubernetes architecture: control-plane components, the kubelet, Pods, Services and namespaces. CKAD preparation covers most of this; otherwise use the free *Introduction to Kubernetes* course or *Kubernetes and Cloud Native Essentials* (LFS250), both linked from the exam page.
2. **Read the Kubernetes security documentation** on kubernetes.io: the security overview, Pod Security Standards, Pod Security Admission, RBAC, Secrets good practices, auditing, and the security checklist.
3. **Learn the threat vocabulary.** Read the threat-model pages and map each attacker goal (persistence, privilege escalation, and so on) to two or three controls that stop it.
4. **Some light hands-on helps memory.** In a kind or minikube cluster, label a namespace with `pod-security.kubernetes.io/enforce=restricted` and try to run a privileged Pod; create a default-deny NetworkPolicy; read a Secret back and decode it.
5. **Use the official Exam Preparation Handbook** and the [CNCF curriculum](https://github.com/cncf/curriculum) as the scope checklist.

How your background helps or misleads:

- **CKAD preparation** gives you SecurityContext, ServiceAccounts, Secrets and NetworkPolicies, which covers much of the fundamentals domain.
- **AZ-900** gives you the shared-responsibility model, which reappears as the Cloud layer of the 4Cs.
- **Azure security terms** such as Defender for Cloud or Azure Policy do not appear. The exam is vendor-neutral and talks about generic controls.

## Differences from related exams

- **KCSA vs CKS.** Same subject, very different style. KCSA is a 90-minute multiple-choice exam with no prerequisite that checks understanding. CKS is a 2-hour hands-on exam that requires CKA and checks implementation. Passing CKS renews KCSA, which shows how the Linux Foundation sees the relationship.
- **KCSA vs KCNA.** Both are multiple-choice associate exams. KCNA covers Kubernetes and the cloud-native landscape in general (orchestration, delivery, observability). KCSA covers only security, in more depth.
- **KCSA vs SC-900 and CLF-C02.** Those are cloud-vendor fundamentals exams. SC-900 covers Microsoft security, compliance and identity services. KCSA uses no vendor products and is specific to Kubernetes.
- **KCSA vs CCSK.** CCSK is a cloud-security knowledge certificate covering governance, risk, architecture and data security across cloud models. KCSA is narrower and closer to the platform: what the kubelet's read-only port exposes, what PSA enforces.

## Exam-day notes

- **Time:** 90 minutes is usually ample. Answer everything on a first pass, flag the uncertain ones and return.
- **Read for the threat.** When a question names an attack (for example, a stolen ServiceAccount token, or a container escaping to the node), choose the control that directly breaks that path, not a generally good practice.
- **Watch the qualifiers:** "most effective", "first", "least privilege".
- **Traps:** base64-encoded Secrets are not encrypted; NetworkPolicies need a CNI plug-in that enforces them; RBAC has no deny rules; the `Restricted` Pod Security Standard requires running as non-root and dropping all capabilities.
