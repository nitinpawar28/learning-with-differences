---
code: CKAD
title: "Certified Kubernetes Application Developer"
credential: "Certified Kubernetes Application Developer (CKAD)"
provider: linux-foundation
tracks: [cloud]
clouds: [neutral]
level: intermediate
tier: core
stage: "1"
progress: planned
official_url: https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/
study_guide_url: https://github.com/cncf/curriculum/blob/master/CKAD_Curriculum_v1.37.pdf
outline_version: "v1.37"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. The Linux Foundation rates the exam as intermediate and assumes you can already build container images and work at a Linux shell."
replaces: ""
replaced_by: ""
counterparts: [ai-200, dva-c03]
objectives:
  - { id: "1", title: "Application Design and Build", weight: "20%" }
  - { id: "1.1", title: "Define, build and modify container images" }
  - { id: "1.2", title: "Choose and use the right workload resource (Deployment, DaemonSet, CronJob, etc.)" }
  - { id: "1.3", title: "Understand multi-container Pod design patterns (sidecar, init and others)" }
  - { id: "1.4", title: "Use persistent and ephemeral volumes" }
  - { id: "2", title: "Application Deployment", weight: "20%" }
  - { id: "2.1", title: "Use Kubernetes primitives for common deployment strategies (blue/green, canary)" }
  - { id: "2.2", title: "Understand Deployments and how to perform rolling updates" }
  - { id: "2.3", title: "Use the Helm package manager to deploy existing packages" }
  - { id: "2.4", title: "Kustomize" }
  - { id: "3", title: "Application Observability and Maintenance", weight: "15%" }
  - { id: "3.1", title: "Understand API deprecations" }
  - { id: "3.2", title: "Implement probes and health checks" }
  - { id: "3.3", title: "Use built-in CLI tools to monitor Kubernetes applications" }
  - { id: "3.4", title: "Use container logs" }
  - { id: "3.5", title: "Debugging in Kubernetes" }
  - { id: "4", title: "Application Environment, Configuration and Security", weight: "25%" }
  - { id: "4.1", title: "Discover and use resources that extend Kubernetes (CRDs, Operators)" }
  - { id: "4.2", title: "Understand authentication, authorization and admission control" }
  - { id: "4.3", title: "Understand requests, limits and quotas" }
  - { id: "4.4", title: "Define resource requirements" }
  - { id: "4.5", title: "Understand ConfigMaps" }
  - { id: "4.6", title: "Create and consume Secrets" }
  - { id: "4.7", title: "Understand ServiceAccounts" }
  - { id: "4.8", title: "Understand application security (SecurityContexts, capabilities, etc.)" }
  - { id: "5", title: "Services and Networking", weight: "20%" }
  - { id: "5.1", title: "Demonstrate basic understanding of NetworkPolicies" }
  - { id: "5.2", title: "Provide and troubleshoot access to applications via Services" }
  - { id: "5.3", title: "Use Ingress rules to expose applications" }
---
## Exam format

All facts below are as of 2026-10-24, taken from the [CKAD exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/), the Linux Foundation [CKA, CKAD and CKS FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks) and the [CKA and CKAD exam tips](https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad).

- **Question type:** performance-based only. There are no multiple-choice questions. You get a set of tasks and solve each one at a command line against live Kubernetes clusters, and the result is scored automatically.
- **Number of tasks:** 15 to 20 performance-based tasks (exam tips). The included simulator has 17 questions per attempt.
- **Duration:** 2 hours.
- **Passing score:** 66% or above (FAQ).
- **Kubernetes version:** v1.37. The Linux Foundation says the exam environment moves to the latest Kubernetes minor release within about 4 to 8 weeks of that release.
- **Price:** USD 445 for the exam alone. Bundles are USD 625 with a THRIVE-ONE annual subscription and USD 645 with the LFD259 course. One free retake is included.
- **Simulator:** two Killer.sh attempts, each open for 36 hours from activation, each with a different 17-question set and graded results. The FAQ says the simulator is not included in CKAD-SINGLE registrations.
- **Languages:** English, Japanese and Simplified Chinese. You can switch language from inside the exam.
- **Delivery:** online, remotely proctored through PSI's Bridge platform and the PSI Secure Browser, with webcam, microphone and screen sharing. Only one active monitor is allowed. Results are emailed within about 24 hours.
- **Open book, within limits:** you may use kubernetes.io/docs, kubernetes.io/blog and helm.sh/docs inside the exam browser, plus links in each task's Quick Reference box ([Resources Allowed](https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed)). You may not open external search results.
- **Eligibility and renewal:** you have 12 months from purchase to schedule and sit the exam. The certification is valid for 2 years, and you renew by passing the then-current exam again.

Prices, the Kubernetes version and the simulator terms change often. Confirm them on the official page before you book.

## What the exam really tests

CKAD checks one thing: can you take an application and make it run correctly on Kubernetes, quickly, using `kubectl` and YAML? It is not about cluster installation (that is CKA) or about hardening (that is CKS). Everything happens inside namespaces you are given, on clusters that already work.

The themes behind the five domains:

- **Pod and workload design (20%).** Choosing between a Deployment, a DaemonSet, a Job and a CronJob, and writing them correctly. Multi-container Pods matter: init containers that must finish first, and sidecars, which since Kubernetes 1.29 can be declared as init containers with `restartPolicy: Always`. Volumes come in here too: `emptyDir` for scratch space shared between containers, and PersistentVolumeClaims for data that must outlive a Pod. Building or changing a container image with a Dockerfile (or Podman) is also in scope.
- **Release mechanics (20%).** Rolling updates with `maxSurge` and `maxUnavailable`, `kubectl rollout status`, `history` and `undo`. Blue/green and canary are not built-in objects. You build them from plain primitives: two Deployments, label selectors and a Service that you point at one set of labels or at both. Helm appears at the level of installing, upgrading and rolling back an existing chart with values. Kustomize appears at the level of bases, overlays and `kubectl apply -k`.
- **Observability and maintenance (15%).** Liveness, readiness and startup probes, and knowing which one fixes which symptom. `kubectl logs` (including `--previous` and `-c` for a specific container), `kubectl top`, `kubectl describe`, events, and `kubectl debug`. API deprecations mean recognising when a manifest uses a removed `apiVersion` and fixing it.
- **Configuration and security (25%, the largest domain).** ConfigMaps and Secrets consumed as environment variables and as mounted files. Resource requests and limits, ResourceQuota and LimitRange (and why a Pod is rejected in a namespace that has a quota but no defaults). ServiceAccounts and how a Pod uses one. SecurityContext settings: `runAsUser`, `runAsNonRoot`, `readOnlyRootFilesystem`, `allowPrivilegeEscalation`, and adding or dropping Linux capabilities. Authentication, authorization (RBAC) and admission are tested at the level of understanding why a request was refused and creating a Role and RoleBinding. CRDs and Operators mean using a custom resource that already exists in the cluster, not writing a controller.
- **Services and networking (20%).** ClusterIP, NodePort and LoadBalancer Services, selectors that do or do not match, `targetPort` versus `port`, and checking Endpoints/EndpointSlices when traffic goes nowhere. Ingress rules with path and host routing. NetworkPolicies at a basic level: default deny, then allowing traffic by Pod label, namespace label and port.

Where candidates lose points:

- **Wrong host or namespace.** Each task tells you which host to `ssh` into, and often which namespace to use. Work done in the wrong place earns nothing even when it is perfect.
- **Speed.** Most people who fail knew the material but ran out of time. Writing YAML from scratch is too slow. Generate it with `kubectl create ... --dry-run=client -o yaml` or `kubectl run`, then edit.
- **Small YAML errors.** Indentation, a label in a selector that does not match the template, a probe on the wrong port, `command` versus `args`.
- **Not checking the result.** A Deployment that is applied but whose Pods are in CrashLoopBackOff earns little.

## Study strategy

The reader prepared for this exam before but never sat it. Kubernetes has moved several minor versions since then, so start with a refresh, not a re-read.

1. **Foundations first.** Containers and images (Dockerfile layers, tags, registries), then the core objects: Pod, ReplicaSet, Deployment, Service, Namespace, labels and selectors. If any of this feels shaky, the free Linux Foundation course *Introduction to Kubernetes* (LFS158) is enough.
2. **Daily `kubectl` practice.** Set up a local cluster (kind, minikube or k3d) and practise until imperative commands are reflexive: `kubectl run`, `create deployment`, `expose`, `create configmap`, `create secret generic`, `create job`, `create cronjob`, `set image`, `scale`, `rollout`. Practise with the `k` alias and Bash completion, which the exam hosts already have set up, and get fast in vim, the editor the exam tips describe.
3. **Domain by domain, in this order:** configuration and security (the largest), then workloads and multi-container Pods, then deployment strategies, Helm and Kustomize, then Services, Ingress and NetworkPolicy, then probes and debugging.
4. **Learn to search kubernetes.io/docs fast.** It is open during the exam. Know where the examples for probes, NetworkPolicy, SecurityContext, PersistentVolumeClaim and Ingress live so you can copy and adapt them.
5. **Use the simulator twice.** Do the first Killer.sh attempt about two weeks out, study what you missed, and do the second a few days before the exam.

Official learning resources (all on the exam page): *Kubernetes for Developers* (LFD259, self-paced), *Kubernetes for App Developers* (instructor-led), the THRIVE-ONE subscription, free Cloud & Containers courses and the CKAD learning-path PDF. The [CNCF curriculum](https://github.com/cncf/curriculum) is the authoritative list of what is examined.

How your background helps or misleads:

- **AZ-204 preparation** helps with images and registries (Azure Container Registry), containers as an app-hosting option and the idea of managed identity. It misleads in one way: Azure Container Apps and App Service hide Kubernetes objects. CKAD wants the raw Deployment, Service and Ingress YAML that those platforms generate for you.
- **AZ-900** gives the vocabulary of scaling and availability, but nothing in this exam is Azure-specific. AKS is never mentioned.
- **.NET and Angular** experience helps you reason about application concerns: health endpoints map to probes, `appsettings.json` and environment variables map to ConfigMaps, and connection strings map to Secrets. The trap is assuming a web framework detail matters. The exam only cares about the container's port, command and environment.
- **Basic AWS** knowledge of ECS is close in concept, but the vocabulary differs (task definition versus Pod spec, service versus Deployment plus Service).

## Differences from related exams

- **CKAD vs CKA.** They share the same format, price, environment and much of the YAML. CKAD stays inside namespaces and is about the application: workloads, configuration, probes, Helm and Kustomize as a consumer, Services and Ingress. CKA adds the cluster itself: kubeadm installation and upgrades, etcd, control-plane troubleshooting (30% of CKA is troubleshooting), storage classes, the Gateway API, CoreDNS and the extension interfaces (CNI, CSI, CRI). Many people take CKAD first because the workload skills transfer directly into CKA.
- **CKAD vs CKS.** CKS requires CKA, and it goes deep into security tooling: AppArmor, seccomp, Falco, audit logs, image scanning and signing. The SecurityContext, ServiceAccount and NetworkPolicy items in CKAD are the gentle start of that same material.
- **CKAD vs KCNA and KCSA.** Those are multiple-choice associate exams about concepts. CKAD is entirely hands-on. Knowing what a NetworkPolicy is will pass a KCNA question but not a CKAD task.
- **CKAD vs AI-200 (Azure AI Cloud Developer Associate).** AI-200, the successor of AZ-204, includes AKS manifests and container hosting as one area among several Azure services, and it is a multiple-choice style Microsoft exam. CKAD is vendor-neutral and goes much deeper into Kubernetes objects, but it covers nothing about cloud services, SDKs or AI.
- **CKAD vs DVA-C03 (AWS Developer – Associate).** The AWS exam tests application development across AWS services (Lambda, DynamoDB, API Gateway, SQS, deployment pipelines) in scenario questions. Containers appear only through AWS services such as ECS, EKS and ECR. CKAD tests one platform, hands-on, with no cloud vendor in sight.

## Exam-day notes

- **Budget time.** Two hours for 15 to 20 tasks is about 6 to 8 minutes each. Skip a slow task, flag it and come back.
- **Go to the right host for every task.** The infobox at the start of each task tells you which host to `ssh` into. Do the work there, then `exit` back to the base system (hostname `base`) before the next task. Nested `ssh` is not supported, and the base system has no `kubectl`. Add `-n <namespace>` whenever the task names a namespace.
- **Generate, do not type.** `--dry-run=client -o yaml > file.yaml`, edit, apply. Use `kubectl explain <resource>.spec --recursive` when you forget a field name.
- **Verify before moving on.** `kubectl get`, `describe`, and a quick `kubectl exec` or temporary Pod with `wget` or `curl` to test a Service or NetworkPolicy.
- **Know the environment.** The exam runs in a remote Linux desktop in the PSI Secure Browser. In the terminal, copy is Ctrl+Shift+C and paste is Ctrl+Shift+V. Use Ctrl+Alt+W instead of Ctrl+W, which would close the browser tab. The Insert key is blocked, so press `i` to enter insert mode in vim. Try all of this in the simulator first.
- **Traps:** a Secret's `data` field needs base64 values while `stringData` does not; a readiness probe failing removes the Pod from the Service but does not restart it; a NetworkPolicy that selects a Pod blocks everything not explicitly allowed for that direction, including DNS egress if you add an egress policy.
