---
code: CKS
title: "Certified Kubernetes Security Specialist"
credential: "Certified Kubernetes Security Specialist (CKS)"
provider: linux-foundation
tracks: [security, cloud]
clouds: [neutral]
level: intermediate
tier: core
stage: "4"
progress: planned
official_url: https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/
study_guide_url: https://github.com/cncf/curriculum/blob/master/CKS_Curriculum%20v1.34.pdf
outline_version: "v1.34"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: [cka]
prerequisites_any: []
prerequisite_note: "You must have taken and passed the CKA exam before attempting CKS."
replaces: ""
replaced_by: ""
counterparts: [sc-500, scs-c03]
objectives:
  - { id: "1", title: "Cluster Setup", weight: "15%" }
  - { id: "1.1", title: "Use network security policies to restrict cluster-level access" }
  - { id: "1.2", title: "Use the CIS benchmark to review the security configuration of Kubernetes components (etcd, kubelet, kubedns, kubeapi)" }
  - { id: "1.3", title: "Properly set up Ingress objects with TLS" }
  - { id: "1.4", title: "Protect node metadata and endpoints" }
  - { id: "1.5", title: "Verify platform binaries before deploying" }
  - { id: "2", title: "Cluster Hardening", weight: "15%" }
  - { id: "2.1", title: "Use role-based access controls to minimize exposure" }
  - { id: "2.2", title: "Exercise caution with service accounts (disable defaults, minimize permissions on new ones)" }
  - { id: "2.3", title: "Restrict access to the Kubernetes API" }
  - { id: "2.4", title: "Upgrade Kubernetes to avoid vulnerabilities" }
  - { id: "3", title: "System Hardening", weight: "10%" }
  - { id: "3.1", title: "Minimize host OS footprint (reduce attack surface)" }
  - { id: "3.2", title: "Use least-privilege identity and access management" }
  - { id: "3.3", title: "Minimize external access to the network" }
  - { id: "3.4", title: "Appropriately use kernel hardening tools such as AppArmor and seccomp" }
  - { id: "4", title: "Minimize Microservice Vulnerabilities", weight: "20%" }
  - { id: "4.1", title: "Use appropriate Pod Security Standards" }
  - { id: "4.2", title: "Manage Kubernetes Secrets" }
  - { id: "4.3", title: "Understand and implement isolation techniques (multi-tenancy, sandboxed containers, etc.)" }
  - { id: "4.4", title: "Implement Pod-to-Pod encryption (Cilium, Istio)" }
  - { id: "5", title: "Supply Chain Security", weight: "20%" }
  - { id: "5.1", title: "Minimize base image footprint" }
  - { id: "5.2", title: "Understand your supply chain (SBOM, CI/CD, artifact repositories)" }
  - { id: "5.3", title: "Secure your supply chain (permitted registries, sign and validate artifacts, etc.)" }
  - { id: "5.4", title: "Perform static analysis of user workloads and container images (Kubesec, KubeLinter)" }
  - { id: "6", title: "Monitoring, Logging and Runtime Security", weight: "20%" }
  - { id: "6.1", title: "Perform behavioral analytics to detect malicious activities" }
  - { id: "6.2", title: "Detect threats within physical infrastructure, apps, networks, data, users and workloads" }
  - { id: "6.3", title: "Investigate and identify phases of attack and bad actors within the environment" }
  - { id: "6.4", title: "Ensure immutability of containers at runtime" }
  - { id: "6.5", title: "Use Kubernetes audit logs to monitor access" }
---
## Exam format

All facts below are as of 2026-10-24, from the [CKS exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/), the Linux Foundation [CKA, CKAD and CKS FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks) and the [CKS important instructions](https://docs.linuxfoundation.org/tc-docs/certification/important-instructions-cks).

- **Question type:** performance-based only, solved at a command line on live clusters and scored automatically.
- **Number of tasks:** 15 to 20 performance-based tasks (important instructions). The simulator has 17 questions per attempt.
- **Duration:** 2 hours.
- **Passing score:** 67% or above (FAQ), one point higher than CKA and CKAD.
- **Kubernetes version:** the exam page and FAQ say v1.35, while the curriculum PDF that the exam page links, and the newest one in the [CNCF curriculum repository](https://github.com/cncf/curriculum), is labelled v1.34. The objectives above are transcribed from that v1.34 document, which is the current published outline. CKS trails CKA and CKAD (v1.37) by two minor versions.
- **Prerequisite:** you must have taken and passed CKA before attempting CKS.
- **Price:** USD 445 for the exam alone, USD 625 with a THRIVE-ONE annual subscription, USD 645 with the LFS260 course. One free retake is included.
- **Simulator:** two Killer.sh attempts, each open for 36 hours, each with a different 17-question set and graded results. Not included in CKS-SINGLE registrations.
- **Languages:** English, Japanese and Simplified Chinese. You can switch language during the exam.
- **Delivery:** online, remotely proctored through PSI Bridge and the PSI Secure Browser. Results by email within about 24 hours.
- **Allowed documentation:** kubernetes.io/docs and /blog, falco.org/docs, the Kubernetes SIG `bom` CLI reference, etcd.io/docs, the ingress-nginx configuration guide, docs.cilium.io and istio.io/latest/docs ([Resources Allowed](https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed)).
- **Eligibility and renewal:** 12 months to schedule and sit after purchase. Valid for 2 years, and you renew by passing the exam again before it expires. Under the Linux Foundation CARE programme, passing CKS also renews a KCSA ([multiple-choice FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-mc)), and earning or renewing CKS on or after 2026-06-18 extends your CKA expiry date to match the new CKS date (CKA, CKAD and CKS FAQ).

Confirm version, price and allowed resources before booking. The allowed-resources list in particular tells you which tools may appear.

## What the exam really tests

CKS asks you to secure a cluster that already works, using the cluster's own controls plus a small set of open-source tools. The scope runs from the node's kernel to the image pipeline to runtime detection.

- **Cluster setup (15%).** Default-deny NetworkPolicies and policies that allow only what is needed; running `kube-bench` and fixing the findings in API server, kubelet and etcd configuration; TLS on Ingress using a Secret; blocking Pods from reaching the cloud metadata endpoint (169.254.169.254) with a NetworkPolicy; checking binary checksums before installing.
- **Cluster hardening (15%).** Least-privilege RBAC; turning off `automountServiceAccountToken` and not using the `default` ServiceAccount; closing anonymous access and insecure options on the API server; upgrading the cluster (a CKA skill reused).
- **System hardening (10%).** Removing unneeded packages and services from nodes, limiting open ports, and loading and applying AppArmor profiles and seccomp profiles to Pods through `securityContext`.
- **Minimize microservice vulnerabilities (20%).** Pod Security Admission with the Privileged, Baseline and Restricted standards set by namespace labels; Secrets handling, including encryption at rest in etcd with an `EncryptionConfiguration`; sandboxed runtimes through a RuntimeClass (for example gVisor's `runsc`); and Pod-to-Pod encryption with Cilium or Istio mutual TLS.
- **Supply chain security (20%).** Smaller base images and multi-stage builds; SBOMs (generated with `bom` or similar); restricting registries with an admission policy (ValidatingAdmissionPolicy or a webhook); image signing and verification; static analysis of manifests and images with Kubesec, KubeLinter and an image scanner such as Trivy.
- **Monitoring, logging and runtime security (20%).** Writing and reading Falco rules and output; configuring an audit policy on the API server and finding who did what in the audit log; making containers immutable with `readOnlyRootFilesystem` and no shell or package manager; spotting a compromised Pod and stopping it.

Where candidates lose points: API server edits that break the control plane (audit logging and admission settings need both flags and volume mounts in the static Pod manifest); slow navigation of unfamiliar tool output under time pressure; and AppArmor profiles that are applied to a Pod but never loaded on the node where it runs. Many find CKS the hardest of the three because each task touches several layers at once.

## Study strategy

1. **Keep CKA skills fresh first.** CKS assumes fluent kubeadm, static Pod manifests, etcd and RBAC. Taking CKS soon after CKA saves a refresh.
2. **Then study by layer, outward from the host:** Linux hardening (AppArmor, seccomp, users, services), then cluster hardening (API server flags, RBAC, ServiceAccounts, upgrades), then workload controls (Pod Security Admission, SecurityContext, RuntimeClass, Secrets encryption), then network controls (NetworkPolicy, Ingress TLS, mTLS), then supply chain (images, SBOM, scanning, admission), then runtime (Falco and audit logs).
3. **Hands-on is everything.** On a kubeadm lab cluster, enable an audit policy, enable etcd encryption, install Falco and write a custom rule, load an AppArmor profile on a worker and apply it, run kube-bench and fix three findings, scan an image with Trivy and rebuild it smaller.
4. **Learn the allowed documentation sites.** Falco's rule syntax and the Kubernetes audit and encryption pages are where you will copy from during the exam.
5. **Simulator twice**, as with the other Kubernetes exams.

Official learning resources on the exam page: *Kubernetes Security Essentials* (LFS260, self-paced), *Kubernetes Security Fundamentals* (LFS460, instructor-led), the CKS learning-path PDF, free Cloud & Containers courses and THRIVE-ONE. KCSA is a useful conceptual warm-up.

How your background helps or misleads:

- **CKAD preparation** already covered SecurityContext, capabilities, ServiceAccounts and NetworkPolicies, which is the base layer of CKS.
- **AZ-900 and Azure security concepts** (Defender for Cloud, Azure Policy, Key Vault) are useful analogies: Azure Policy for AKS is built on Gatekeeper admission control, and Key Vault resembles an external secret store. But CKS never uses a cloud service. Every control is in the cluster or on the node.
- **.NET background** helps with supply-chain thinking (signed packages, dependency scanning in a build pipeline) but not with the Linux kernel tools.

## Differences from related exams

- **CKS vs CKA.** CKA builds and repairs the cluster. CKS assumes that and adds the security controls on top. The skills overlap in RBAC, NetworkPolicy and upgrades, but CKS adds AppArmor, seccomp, Falco, audit logging, Pod Security Admission, RuntimeClass, etcd encryption and image supply chain.
- **CKS vs KCSA.** Both use the same security themes (the 4Cs, threat models, Pod Security Standards, supply chain). KCSA is a 90-minute multiple-choice exam that tests whether you understand them. CKS is a 2-hour hands-on exam that tests whether you can implement them under time pressure.
- **CKS vs SC-500 (Microsoft Cloud and AI Security Engineer Associate).** SC-500 replaced AZ-500, which retired on 2026-08-31. It secures Azure and hybrid estates: identity with Microsoft Entra ID and Key Vault, governance with Azure Policy, storage, databases and networking, compute including AI workloads, and posture management with Microsoft Defender for Cloud, Microsoft Sentinel and Security Copilot. Kubernetes appears only as a few items on AKS, Azure Container Registry and Defender for Containers. CKS goes much deeper on a single platform and uses only open-source tools.
- **CKS vs SCS-C03 (AWS Security – Specialty).** The AWS exam covers detection, incident response, IAM, data protection and infrastructure security across AWS, in scenario-based questions. Container security there means services such as Amazon Inspector and GuardDuty for EKS. CKS has you write the Falco rule and the audit policy yourself.
- **CKS vs CCSK and CCSP.** Those are cloud-security knowledge exams about governance, architecture and shared responsibility. CKS is an operator's exam.

## Exam-day notes

- **Time:** 15 to 20 tasks in 2 hours is about 6 to 8 minutes per task, but tasks vary more than on CKA. Do the quick wins first (RBAC, ServiceAccount, NetworkPolicy, SecurityContext) and leave multi-step API server changes until you have banked points.
- **Before editing the API server manifest, copy it.** After the edit, wait for the API server to return (`crictl ps` on the control-plane node) before moving on. For audit logging and encryption config, remember the `volumes` and `volumeMounts` so the files are visible inside the static Pod.
- **SSH to the right host.** Each task's infobox names the host to `ssh` into. Return to the base system with `exit` afterwards, because nested `ssh` is not supported. AppArmor profiles must be loaded (`apparmor_parser`) on the node where the Pod is scheduled. seccomp profiles live under the kubelet's seccomp directory on that node.
- **Falco tasks:** read the existing rule and output format carefully. Tasks often ask you to change the output fields or write the findings to a file in a specific format.
- **Traps:** Pod Security Admission labels go on the namespace, not the Pod; `enforce` rejects Pods while `warn` and `audit` do not; encryption at rest only covers Secrets written after you enable it, so existing ones must be rewritten; deleting a compromised Pod that belongs to a Deployment does nothing unless you scale the Deployment down.
