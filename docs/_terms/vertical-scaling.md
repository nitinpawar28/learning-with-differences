---
title: "Vertical Scaling"
summary: "Giving a single instance more CPU, memory, storage throughput or network (scale up) or less (scale down) instead of changing how many instances there are; simple and code-free, but bounded by the largest available size and usually paid for with a restart."
acronyms: []
aliases: ["Scaling up", "Scale-up", "Scale up and down"]
formerly: []
tracks: [architect, cloud]
domain: cloud-foundations
cloud: neutral
level: practitioner
status: complete
last_verified: 2026-10-24
differs_from:
  - { term: horizontal-scaling, note: "Horizontal scaling adds instances and needs the work and state to be distributable; vertical scaling changes nothing about the application but hits the ceiling of the biggest SKU and keeps a single point of failure." }
  - { term: table-partitioning, note: "A bigger box does the same amount of work faster; partitioning makes each query do less work by touching fewer rows. They compose, and partitioning often postpones the next scale-up." }
  - { term: backpressure, note: "Scaling up raises the load at which a component collapses; backpressure keeps the component below whatever its ceiling is. A scale-up without backpressure only moves the point of collapse." }
related: [hypertable, consumer-group, rolling-deployment]
covers: []
sources:
  - { title: "Autoscaling guidance", url: "https://learn.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling", publisher: "Azure Architecture Center" }
  - { title: "Resize a virtual machine", url: "https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm", publisher: "Microsoft Learn" }
  - { title: "Change the instance type for your Amazon EC2 instance", url: "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-instance-type-of-ebs-backed-instance.html", publisher: "AWS" }
  - { title: "How Aurora serverless works", url: "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html", publisher: "AWS" }
  - { title: "Resize CPU and memory resources assigned to containers", url: "https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/", publisher: "The Kubernetes Authors" }
---

## Explanation

Vertical scaling changes the capacity of one resource rather than the number of resources: a bigger VM size, a higher App Service tier, more vCores for Azure SQL, a larger RDS instance class, more CPU and memory for a container. Scaling down is the same lever in reverse, the usual way to cut cost once a workload proves over-provisioned. The Azure Architecture Center's definition carries the two facts that matter: it often requires making the system temporarily unavailable while it is redeployed, so it is rarely automated.

Its appeal is that the application does not change. A single-writer relational database, an in-memory stateful service, a legacy application that assumes one host, per-instance licensed software, a batch job with a large working set: all scale up without a redesign, whereas scaling out would mean externalising state, partitioning data or accepting eventual consistency. The Well-Architected Framework says it plainly: vertical scaling fits workloads that cannot easily be divided.

The cost is disruption and a ceiling, and both depend on the service:

- **Virtual machines.** Resizing an Azure VM restarts it, and if the new size is not on the VM's current hardware cluster it must be deallocated first, which releases dynamic IP addresses. On AWS you must stop an EBS-backed EC2 instance to change its type; it moves to new hardware and a non-Elastic public IPv4 address is replaced.
- **Platform services.** An App Service plan's tier changes in seconds and affects every app on the plan. Azure SQL Database scales online by moving the engine to a larger host, then briefly drops open connections, so retry logic is mandatory. An Amazon RDS instance class change causes downtime, now or in the maintenance window, which Multi-AZ shortens to a failover.
- **Serverless databases** remove the restart. Aurora Serverless v2 measures capacity in Aurora capacity units (ACUs) of roughly 2 GiB each, scales a writer or reader in steps as small as 0.5 ACU within a configured range (up to 256 ACUs for Aurora MySQL, 384 for Aurora PostgreSQL) while connections and transactions stay open, and can pause at zero. Azure SQL Database's serverless tier similarly autoscales vCores within a configured range and can auto-pause, although resuming from a pause takes a cold start.
- **Containers.** Kubernetes in-place pod resize, introduced in 1.27 and stable since 1.35, changes a container's CPU and memory through the pod's `resize` subresource without recreating it; the Vertical Pod Autoscaler recommends requests from observed usage. Azure Container Apps has no dynamic vertical scaling: CPU and memory belong to the revision template, so a change means a new revision.

The ceiling is the largest SKU the platform sells, and prices bend upward before it. A scaled-up instance is still one instance, a single point of failure whose restart is the service's restart, so the usual design scales stateless tiers out and reserves scaling up for what cannot be split.

For a .NET service, scaling up only pays if the process uses the box. Server garbage collection is the throughput choice on a dedicated machine, and dynamic adaptation to application sizes (DATAS), on by default from .NET 9, lets it grow and shrink its heap count with load. In a container the runtime reads the cgroup limits: `Environment.ProcessorCount` reflects the CPU quota and the GC's default heap hard limit is 75 percent of the memory limit, so a resized container changes what the process can use. Redis is the counter-example: it executes commands on a single thread, so a bigger box mostly buys memory. TimescaleDB, single-node since 2.14 removed multi-node support, scales writes this way: a larger primary, compression and chunk pruning to do less work per query, and read replicas for the rest.

## How it differs

**[Horizontal scaling](horizontal-scaling.md)** changes the count; vertical changes the size. Horizontal demands stateless instances or shared state and tolerates any instance vanishing; vertical demands nothing of the code but offers no redundancy and ends at the largest SKU. Horizontal is routinely automated by HPA, Azure Monitor autoscale, KEDA and Auto Scaling groups; vertical is automated only where the platform can resize without disruption (Aurora Serverless v2, Azure SQL serverless, in-place pod resize). The honest default for a web workload is both: scale the API out, scale the database up.

**[Table partitioning](table-partitioning.md)** attacks the same symptom, a database that is too slow, from the other side. Scaling up gives the same query more memory and cores; partitioning (and a TimescaleDB [hypertable](hypertable.md)) lets the query skip the chunks it does not need, so it does less work. Partitioning is cheaper, keeps working after the next scale-up, and frequently postpones it, which is why it comes first in the time-series articles in this library.

**[Backpressure](backpressure.md)** limits intake so that a component stays inside its capacity. Scaling up raises that capacity but does not remove the need to defend it: a bounded queue, a rate limit or a `429` protects the bigger box exactly as it protected the smaller one. Teams that scale up instead of adding backpressure find the same outage recurring at a higher load level.

| | Vertical scaling | Horizontal scaling |
| --- | --- | --- |
| What changes | Size of one instance | Number of instances |
| Code changes | None | Externalised state, idempotent work |
| Disruption | Restart or connection drop (except serverless and in-place resize) | None for existing instances |
| Ceiling | Largest SKU | Distribution of work and state |
| Failure domain | Still one instance | Spread over N |
| Automation | Rare | Standard |
| Typical targets | Databases, stateful services, licensed software | Web and API tiers, workers, consumers |

## Examples

**Making the process match the box.** A scaled-up container or VM is wasted if the runtime still behaves as though it were small. These snippets read the limits the platform actually granted and size the things that must track them.

=== "C#"

    ```csharp
    // Program.cs (.NET 9). Report what the runtime sees after a resize, and size work to it.
    using System.Runtime;

    var info = GC.GetGCMemoryInfo();
    Console.WriteLine(
        $"cores={Environment.ProcessorCount} " +                                   // honours the cgroup CPU quota
        $"gcHeapLimitMiB={info.TotalAvailableMemoryBytes / (1024 * 1024)} " +      // 75% of the container limit by default
        $"serverGc={GCSettings.IsServerGC}");

    // Parallelism that follows the instance size instead of a hard-coded number.
    var degree = Math.Max(1, Environment.ProcessorCount - 1);
    var options = new ParallelOptions { MaxDegreeOfParallelism = degree };
    await Parallel.ForEachAsync(Enumerable.Range(0, 1_000), options, async (i, ct) => await RepriceAsync(i, ct));

    static ValueTask RepriceAsync(int batch, CancellationToken ct) => ValueTask.CompletedTask;
    ```

    ```xml
    <!-- MyApi.csproj: throughput-oriented GC for a dedicated box. DATAS is on by default in .NET 9
         for server GC; the property is shown so the choice is explicit and reviewable. -->
    <PropertyGroup>
      <ServerGarbageCollection>true</ServerGarbageCollection>
      <GarbageCollectionAdaptationMode>1</GarbageCollectionAdaptationMode>
    </PropertyGroup>
    ```

=== "Python"

    ```python
    # sizing.py (Python 3.12, Linux, cgroup v2). Read the limits the container was actually given,
    # then size worker pools from them. os.cpu_count() reports the host, and os.sched_getaffinity()
    # reflects only a cpuset; a Kubernetes or Docker CPU limit is a CFS quota in cpu.max.
    import math
    import os
    from pathlib import Path

    CGROUP = Path("/sys/fs/cgroup")


    def granted_cores() -> int:
        cores = len(os.sched_getaffinity(0))
        try:
            quota, period = (CGROUP / "cpu.max").read_text().split()   # e.g. "200000 100000" = 2 CPUs
            if quota != "max":
                cores = min(cores, math.ceil(int(quota) / int(period)))
        except FileNotFoundError:
            pass                                                         # no cgroup v2 CPU controller
        return max(1, cores)


    def granted_memory_bytes() -> int | None:
        try:
            raw = (CGROUP / "memory.max").read_text().strip()           # "max" means unlimited
        except FileNotFoundError:
            return None
        return None if raw == "max" else int(raw)


    if __name__ == "__main__":
        cores, mem = granted_cores(), granted_memory_bytes()
        workers = max(1, cores)                       # e.g. uvicorn --workers, or a ProcessPoolExecutor size
        print(f"cores={cores} memory={mem} workers={workers}")
    ```

=== "Azure"

    ```bash
    # VM: check which sizes the current hardware cluster offers; a resize restarts the VM,
    # and a size not in this list needs a deallocate first.
    az vm list-vm-resize-options --resource-group rg-data --name vm-timescale --query "[].name" -o tsv
    az vm deallocate --resource-group rg-data --name vm-timescale
    az vm resize --resource-group rg-data --name vm-timescale --size Standard_E16ds_v5
    az vm start --resource-group rg-data --name vm-timescale

    # App Service: the tier belongs to the plan, so every app on it scales up together, in seconds.
    az appservice plan update --resource-group rg-app --name plan-orders --sku P2v3

    # Azure SQL Database: online move to a larger host, then a brief connection drop at the end.
    az sql db update --resource-group rg-data --server sql-orders --name orders --service-objective GP_Gen5_8

    # Container Apps: no dynamic vertical scaling; new CPU and memory values mean a new revision.
    az containerapp update --resource-group rg-app --name orders-api --cpu 2.0 --memory 4.0Gi
    ```

=== "AWS"

    ```bash
    # EC2: an EBS-backed instance must be stopped to change type; a non-Elastic public IPv4 changes.
    aws ec2 stop-instances --instance-ids i-0123456789abcdef0
    aws ec2 wait instance-stopped --instance-ids i-0123456789abcdef0
    aws ec2 modify-instance-attribute --instance-id i-0123456789abcdef0 --instance-type '{"Value":"r7i.4xlarge"}'
    aws ec2 start-instances --instance-ids i-0123456789abcdef0

    # RDS: a DB instance class change incurs downtime; choose now or the maintenance window.
    aws rds modify-db-instance --db-instance-identifier orders --db-instance-class db.r7g.2xlarge --apply-immediately

    # Aurora Serverless v2: vertical scaling without the restart, in 0.5 ACU steps within a range.
    aws rds modify-db-cluster --db-cluster-identifier orders-cluster \
      --serverless-v2-scaling-configuration MinCapacity=0.5,MaxCapacity=16
    ```

=== "Kubernetes"

    ```yaml
    # Vertical Pod Autoscaler in recommendation mode: it computes request values from observed usage,
    # and you apply them deliberately (or let a newer VPA apply them in place).
    apiVersion: autoscaling.k8s.io/v1
    kind: VerticalPodAutoscaler
    metadata:
      name: orders-api
    spec:
      targetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: orders-api
      updatePolicy:
        updateMode: "Off"
    ```

    ```bash
    # In-place pod resize (stable since Kubernetes 1.35; kubectl 1.32 or later for the flag):
    # change CPU and memory of a running container through the resize subresource, no pod recreation.
    kubectl patch pod orders-api-7d9f5b8c4-x2kql --subresource resize --patch \
      '{"spec":{"containers":[{"name":"api","resources":{"requests":{"cpu":"1","memory":"2Gi"},"limits":{"cpu":"2","memory":"2Gi"}}}]}}'
    kubectl get pod orders-api-7d9f5b8c4-x2kql -o jsonpath='{.status.containerStatuses[0].resources}'
    ```

## Misconceptions

- **"Scaling up has no downtime."** A VM resize restarts the machine, an EC2 instance must be stopped, an RDS class change incurs downtime, and even Azure SQL's online scale ends with a connection drop. The exceptions (Aurora Serverless v2, Azure SQL serverless, in-place pod resize) are notable because they are exceptions.
- **"Twice the cores means twice the speed."** Only for work that parallelises. A single-threaded hot path, a lock, a Redis instance's command thread, or a GC configured for a small box will not use the extra cores; sometimes a scale-up changes nothing but the bill.
- **"Vertical scaling is always the wrong, lazy choice."** For single-writer databases, stateful services and per-instance licences it is the correct choice, and the Well-Architected Framework says so. The mistake is scaling up the *stateless* tiers that should scale out.
- **"Autoscaling can scale vertically too."** Rarely, because most resizes are disruptive. Where the platform resizes in place, as Aurora Serverless v2 and Kubernetes in-place resize do, it can; Container Apps explicitly does not support vertical scaling.
- **"A slow database means the database needs a bigger box."** Check first whether the query does too much work; partitioning, indexing, compression and caching routinely outperform a size change, and they still help after the next one.

## Exam notes

AZ-900 and CLF-C02 test the definition and the contrast with scaling out. AZ-104 expects you to resize VMs and know when deallocation is required, to change App Service plan tiers and understand that the plan, not the app, is what scales, and to pick VM sizes by family; DP-300 covers Azure SQL service tiers, compute sizes and the serverless tier; AZ-305 asks you to choose scale up versus scale out per component. On AWS, SAA-C03 and SOA-C03 cover changing EC2 instance types (stop first, public IP change, Compute Optimizer recommendations), RDS instance class changes and the role of Multi-AZ in limiting downtime, storage scaling without downtime, and Aurora Serverless v2 as the elastic alternative; SAP-C03 adds right-sizing at fleet scale. CKA touches resource requests and limits and the autoscaler family; KCNA asks the conceptual difference between HPA and VPA.

Traps: an EC2 instance type change requires a stopped instance and will replace a non-Elastic public IPv4 address; a Windows VM on Azure cannot be resized between sizes with and without a local temp disk (Linux VMs can), and no VM can be resized from a SCSI-based size to a remote NVMe size in place; RDS allocated storage increases without downtime while class changes do not; Aurora Serverless v2 scales compute, not storage; and Container Apps has no vertical autoscaling, so the only answer there is a new revision or scaling out.

## Self-check

??? question "A nightly ETL job on a single Azure VM takes four hours. The team doubles the VM size and the job still takes four hours. CPU never exceeded 15 percent before or after. What went wrong?"
    The job was not CPU-bound, so adding cores and memory changed nothing; the bottleneck was elsewhere, most likely disk or network throughput, a single-threaded loop, or waiting on the database. Measure before scaling: check IOPS and throughput caps for the disk type and VM size, look at wait time on the database, and consider parallelising the work. A scale-up pays only when the resource that was saturated is the one that grew.

??? question "An RDS PostgreSQL instance needs a larger class before a product launch. The change is scheduled for the launch morning with apply-immediately. What should worry you, and how would you reduce the risk?"
    A DB instance class change causes downtime, so applying it on launch morning puts an outage window exactly where it hurts. Apply it in advance during a low-traffic maintenance window, use Multi-AZ so the change happens on the standby and completes with a short failover rather than a full outage, make sure the application has retry logic for the connection drop, and consider whether Aurora Serverless v2, which scales in place without disruption, fits the workload for the next launch.

??? question "Your .NET 9 API runs in a container limited to 1 CPU and 1 GiB. Operations raise the limits to 4 CPUs and 8 GiB but throughput improves only marginally. Where would you look?"
    First confirm the process sees the new limits (`Environment.ProcessorCount` and `GC.GetGCMemoryInfo().TotalAvailableMemoryBytes` after the resize; a Container Apps change creates a new revision, and an in-place Kubernetes resize needs the pod to have been resized, not just the Deployment edited). Then check whether the application can use the cores: workstation GC on a four-core box, a hard-coded thread pool minimum, synchronous I/O, or a downstream dependency such as the database connection limit that caps throughput regardless of local resources. Scaling up the container is only the first of those four changes.

## Further reading

- [Row vs columnar storage](../data/time-series/row-vs-columnar-storage.md) and [High-frequency indexing and partitioning](../data/time-series/high-frequency-indexing-partitioning.md) for the alternatives to a bigger database box.
- [.NET Core and C# runtime](../messaging/runtime/dotnet-core-csharp.md) and [Async and threading in .NET](../messaging/runtime/async-threading.md) for using the cores you paid for.
- [Bare metal, Linux and hypervisors](../devops/bare-metal-linux-hypervisors.md) for what a VM size actually maps to.
- Neighbouring terms: [Horizontal Scaling](horizontal-scaling.md), [Table Partitioning](table-partitioning.md), [Backpressure](backpressure.md), [Hypertable](hypertable.md), [Consumer Group](consumer-group.md).
- [Resize a VM](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm), [Scale up an App Service plan](https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up), [Scale Azure SQL resources](https://learn.microsoft.com/en-us/azure/azure-sql/database/scale-resources), [Change an EC2 instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-instance-type-of-ebs-backed-instance.html), [RDS instance settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Settings.html) and [Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html): the disruption facts quoted above.
- [Kubernetes in-place pod resize](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) and [.NET garbage collector settings](https://learn.microsoft.com/en-us/dotnet/core/runtime-config/garbage-collector) for DATAS and container heap limits.
