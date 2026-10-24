---
code: CKA
title: "Certified Kubernetes Administrator"
credential: "Certified Kubernetes Administrator (CKA)"
provider: linux-foundation
tracks: [cloud, architect]
clouds: [neutral]
level: intermediate
tier: core
stage: "4"
progress: planned
official_url: https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/
study_guide_url: https://github.com/cncf/curriculum/blob/master/CKA_Curriculum_v1.37.pdf
outline_version: "v1.37"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. The Linux Foundation rates the exam as intermediate; comfort with Linux administration (systemd, networking, file permissions) is assumed."
replaces: ""
replaced_by: ""
counterparts: [az-104, soa-c03]
objectives:
  - { id: "1", title: "Cluster Architecture, Installation and Configuration", weight: "25%" }
  - { id: "1.1", title: "Manage role-based access control (RBAC)" }
  - { id: "1.2", title: "Prepare underlying infrastructure for installing a Kubernetes cluster" }
  - { id: "1.3", title: "Create and manage Kubernetes clusters using kubeadm" }
  - { id: "1.4", title: "Manage the lifecycle of Kubernetes clusters" }
  - { id: "1.5", title: "Implement and configure a highly-available control plane" }
  - { id: "1.6", title: "Use Helm and Kustomize to install cluster components" }
  - { id: "1.7", title: "Understand extension interfaces (CNI, CSI, CRI, etc.)" }
  - { id: "1.8", title: "Understand CRDs, install and configure operators" }
  - { id: "2", title: "Workloads and Scheduling", weight: "15%" }
  - { id: "2.1", title: "Understand application deployments and perform rolling updates and rollbacks" }
  - { id: "2.2", title: "Use ConfigMaps and Secrets to configure applications" }
  - { id: "2.3", title: "Configure workload autoscaling" }
  - { id: "2.4", title: "Understand the primitives for robust, self-healing application deployments" }
  - { id: "2.5", title: "Configure Pod admission and scheduling (limits, node affinity, etc.)" }
  - { id: "3", title: "Services and Networking", weight: "20%" }
  - { id: "3.1", title: "Understand connectivity between Pods" }
  - { id: "3.2", title: "Define and enforce Network Policies" }
  - { id: "3.3", title: "Use ClusterIP, NodePort and LoadBalancer service types and endpoints" }
  - { id: "3.4", title: "Use the Gateway API to manage Ingress traffic" }
  - { id: "3.5", title: "Know how to use Ingress controllers and Ingress resources" }
  - { id: "3.6", title: "Understand and use CoreDNS" }
  - { id: "4", title: "Storage", weight: "10%" }
  - { id: "4.1", title: "Implement storage classes and dynamic volume provisioning" }
  - { id: "4.2", title: "Configure volume types, access modes and reclaim policies" }
  - { id: "4.3", title: "Manage persistent volumes and persistent volume claims" }
  - { id: "5", title: "Troubleshooting", weight: "30%" }
  - { id: "5.1", title: "Troubleshoot clusters and nodes" }
  - { id: "5.2", title: "Troubleshoot cluster components" }
  - { id: "5.3", title: "Monitor cluster and application resource usage" }
  - { id: "5.4", title: "Manage and evaluate container output streams" }
  - { id: "5.5", title: "Troubleshoot services and networking" }
---
## Exam format

All facts below are as of 2026-10-24, from the [CKA exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/), the Linux Foundation [CKA, CKAD and CKS FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks) and the [CKA and CKAD exam tips](https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad).

- **Question type:** performance-based only. You solve tasks at a command line on live clusters, and the exam is scored automatically.
- **Number of tasks:** 15 to 20 performance-based tasks (exam tips). The included simulator has 17 questions per attempt.
- **Duration:** 2 hours.
- **Passing score:** 66% or above (FAQ).
- **Kubernetes version:** v1.37, following the latest minor release within about 4 to 8 weeks. (On 2026-10-24 the exam page still links a v1.35 curriculum PDF, which has moved to the `old-versions` folder of the [CNCF curriculum repository](https://github.com/cncf/curriculum). The repository root now holds v1.37. The text of the two PDFs is identical.)
- **Price:** USD 445 for the exam alone, USD 625 with a THRIVE-ONE annual subscription, USD 645 with the LFS258 course. One free retake is included.
- **Simulator:** two Killer.sh attempts, each open for 36 hours, each with a different 17-question set and graded results. Not included in CKA-SINGLE registrations.
- **Languages:** English, Japanese and Simplified Chinese. You can switch language during the exam.
- **Delivery:** online, remotely proctored through PSI Bridge and the PSI Secure Browser. One active monitor only. Results arrive by email within about 24 hours.
- **Allowed documentation:** kubernetes.io/docs, kubernetes.io/blog, helm.sh/docs and, for CKA only, gateway-api.sigs.k8s.io, plus links in each task's Quick Reference box ([Resources Allowed](https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed)).
- **Eligibility and renewal:** 12 months to schedule and sit after purchase. The certification is valid for 2 years, and you renew by passing the exam again before it expires. Under the Linux Foundation CARE programme, earning or renewing CKS on or after 2026-06-18 extends your CKA expiry date to match the new CKS date, and passing CKA renews KCNA. CKA is also the prerequisite for CKS.

Confirm price, version and the simulator terms on the official page before you book.

## What the exam really tests

CKA tests whether you can run a cluster, not just deploy to one. You are expected to install and upgrade it, keep its control plane healthy, give people the right access, wire up networking and storage, and, above all, find out why something is broken and fix it.

- **Troubleshooting (30%, the largest domain).** Nodes that are `NotReady` because the kubelet is stopped or misconfigured; static Pod manifests in `/etc/kubernetes/manifests` with a wrong flag or path; a scheduler or controller manager that is down, so Pods stay `Pending` or ReplicaSets do not scale; Services with no endpoints; DNS lookups that fail. You will use `systemctl`, `journalctl -u kubelet`, `crictl ps` and `crictl logs` on nodes as well as `kubectl`. Monitoring means `kubectl top` (with metrics-server) and reading container output streams.
- **Cluster architecture, installation and configuration (25%).** `kubeadm init`, `kubeadm join` and token handling; preparing a node (container runtime, kernel modules, sysctl settings, swap); upgrading a control plane and then worker nodes one minor version at a time with drain and uncordon; backing up and restoring etcd with `etcdctl snapshot`; the shape of a highly available control plane (stacked versus external etcd, a load balancer in front of API servers). RBAC with Roles, ClusterRoles, bindings and `kubectl auth can-i`. Installing components with Helm and Kustomize. Knowing what CNI, CSI and CRI plug-ins do. Installing and configuring an operator from its CRDs.
- **Services and networking (20%).** The flat Pod network model, Service types and EndpointSlices, NetworkPolicies, CoreDNS configuration and Service DNS names, Ingress controllers and Ingress resources, and the Gateway API (GatewayClass, Gateway and HTTPRoute). The Gateway API is the newer item and the one older study material lacks.
- **Workloads and scheduling (15%).** Deployments, rollouts and rollbacks, ConfigMaps and Secrets, the Horizontal Pod Autoscaler, and scheduling controls: requests and limits, node selectors, node affinity, taints and tolerations, and Pod priority.
- **Storage (10%).** StorageClasses and dynamic provisioning, PersistentVolumes and claims, access modes (ReadWriteOnce, ReadOnlyMany, ReadWriteMany, ReadWriteOncePod) and reclaim policies (Retain, Delete).

Where candidates lose points: not knowing their way around a node's file system and services under time pressure; editing a static Pod manifest and breaking the API server with a typo, so every later step fails; doing an upgrade out of order; restoring etcd without pointing the etcd static Pod at the restored data directory; and, as in CKAD, working on the wrong host.

## Study strategy

1. **Linux foundations first.** systemd units, `journalctl`, file permissions, `ip` and `ss`, and certificate files. If these are new, practise them before Kubernetes administration.
2. **Build clusters by hand.** Use two or three VMs (Hyper-V, VirtualBox, or cloud VMs on Azure or AWS) and install with kubeadm several times, including a CNI plug-in. Then upgrade the cluster by one minor version, back up and restore etcd, and join and remove a worker. Managed clusters (AKS, EKS) hide exactly the parts this exam tests, so they are not enough.
3. **Break things on purpose.** Stop the kubelet, edit a flag in `kube-apiserver.yaml`, delete a CoreDNS Pod, remove a Service selector, and practise finding the fault from symptoms alone.
4. **Reuse CKAD material for the workload and networking domains**, then add the Gateway API, CoreDNS, StorageClasses and the HPA.
5. **Simulator twice**, about two weeks and a few days before the exam.

Official learning resources on the exam page: *Kubernetes Fundamentals* (LFS258, self-paced), *Kubernetes Administration* (instructor-led), the THRIVE-ONE subscription, free Cloud & Containers courses and the CKA learning-path PDF. The [CNCF curriculum](https://github.com/cncf/curriculum) is the authoritative scope.

How your background helps or misleads:

- **CKAD preparation** covers most of workloads, Services, Ingress, NetworkPolicies, ConfigMaps and Secrets. What it does not cover is the node and control-plane level.
- **AZ-900 and AZ-104-style Azure knowledge** maps loosely: RBAC role assignments resemble RoleBindings, and availability zones resemble spreading control-plane nodes. The trap is AKS thinking. On AKS, Microsoft runs the control plane, etcd and upgrades, so you never touch them. On CKA they are the point.
- **AWS knowledge** of EKS has the same blind spot. VPC networking knowledge helps with the idea of CIDR ranges for Pods and Services.
- **.NET background** helps little here. This is an operations exam.

## Differences from related exams

- **CKA vs CKAD.** Same format, environment and price. CKAD is namespaced application work. CKA adds kubeadm, upgrades, etcd, HA control planes, node troubleshooting, storage provisioning, the Gateway API and CoreDNS. Troubleshooting alone is 30% of CKA.
- **CKA vs CKS.** CKS requires a passed CKA and assumes everything in it. It then asks you to secure the same cluster: CIS benchmarks, AppArmor and seccomp, Pod Security Standards, audit logging, Falco, image scanning and supply-chain controls.
- **CKA vs KCNA.** KCNA is a multiple-choice associate exam about what the pieces are. CKA asks you to build and fix them.
- **CKA vs AZ-104 (Azure Administrator).** AZ-104 is broad: identities, governance, storage, compute, virtual networking and monitoring across Azure. Its container items cover Azure Container Registry, Container Instances and Container Apps, and AKS is not in its outline. It tests configuration choices in Azure's portal and CLI, mostly through multiple-choice and case-style items. CKA is narrow and deep: one platform, hands-on, with no cloud provider involved.
- **CKA vs SOA-C03 (AWS CloudOps Engineer – Associate).** The AWS operations exam covers monitoring, reliability, deployment automation, security and networking across AWS services, with EKS and ECS as parts of the picture. CKA has nothing about cloud services but expects far more depth on one orchestrator.

## Exam-day notes

- **Time:** 15 to 20 tasks in 2 hours is about 6 to 8 minutes per task. Do the quick tasks first and flag long ones such as a full cluster upgrade.
- **Go to the right host for every task.** The infobox at the start of each task tells you which host to `ssh` into. Work there, then `exit` back to the base system (hostname `base`). Nested `ssh` is not supported, and the base system has no `kubectl`. Use `sudo -i` on a host when you need root. Never reboot the base system.
- **Back up before editing static Pod manifests.** Copy the file before you change it. If the API server does not come back within a minute or two, check `crictl ps -a` and the kubelet log, and restore the copy if needed.
- **etcd tasks:** read the certificate paths from the etcd static Pod manifest instead of guessing them, and pass `--endpoints`, `--cacert`, `--cert` and `--key` to `etcdctl`.
- **Upgrade tasks:** upgrade kubeadm first, then `kubeadm upgrade plan` and `apply` on the first control-plane node, then the kubelet and kubectl, then each worker after draining it. Uncordon at the end.
- **Traps:** `kubectl drain` needs `--ignore-daemonsets` (and sometimes `--delete-emptydir-data`); a PVC stays `Pending` when no StorageClass matches or its access mode cannot be satisfied; a ClusterRole bound with a RoleBinding only grants rights in that binding's namespace.
