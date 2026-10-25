---
title: "Principle of Least Privilege (PoLP)"
summary: "The design rule that every user, program and workload should operate with the smallest set of permissions its current task needs, and hold them for the shortest time, so that mistakes and compromises do the least possible damage."
acronyms: [PoLP]
aliases: ["Least privilege"]
formerly: []
tracks: [security]
domain: security-foundations
cloud: neutral
level: foundation
status: complete
last_verified: 2026-10-24
differs_from:
  - { term: zero-trust, note: "Zero trust is an architecture that decides each request dynamically; least privilege is one of the principles it enforces, and it applies just as much inside a perimeter-based design." }
  - { term: rbac, note: "RBAC is a mechanism that grants permissions through roles; least privilege is the standard a role's permission set is measured against, and a role can easily violate it." }
  - { term: capability-based-authorization, note: "Capabilities make least privilege cheap by letting any holder attenuate a token; the principle itself says nothing about how permissions are represented." }
  - { term: wasm-sandboxing, note: "A Wasm sandbox enforces least privilege on one module's imports at run time; the principle also governs people, roles and cloud identities that no sandbox ever sees." }
  - { term: container-isolation, note: "Container isolation is a kernel boundary around a process; least privilege decides what the process inside it, and the identity it runs as, may do, and a container with default capabilities and a cloud role still violates it." }
related: [workload-identity, secrets-rotation, api-key, container-isolation, oauth-client-credentials-flow]
covers:
  - "cissp:3.1.2"
  - { ref: "cissp:7.4.1", depth: partial }
  - { ref: "cissp:5.2.8", depth: partial }
  - { ref: "cks:3.2", depth: partial }
  - { ref: "cks:2.2", depth: partial }
  - { ref: "scs-c03:4.2.3", depth: partial }
  - "csslp:1.2.1"
  - "csslp:7.5.2"
  - { ref: "issap:4.3.1", depth: partial }
  - { ref: "sy0-801:1.1.1", depth: partial }
  - { ref: "sy0-801:3.2.4", depth: partial }
  - { ref: "sc-500:1.3.7", depth: partial }
  - "clf-c02:2.3.3"
  - "sap-c03:3.2.4"
  - { ref: "saa-c03:1.1.4", depth: partial }
sources:
  - { title: "The Protection of Information in Computer Systems", url: "http://web.mit.edu/Saltzer/www/publications/protection/", publisher: "Saltzer and Schroeder, Proceedings of the IEEE 63(9), 1975" }
  - { title: "NIST Computer Security Resource Center glossary: least privilege", url: "https://csrc.nist.gov/glossary/term/least_privilege", publisher: "NIST" }
  - { title: "NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations", url: "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final", publisher: "NIST" }
  - { title: "Security best practices in IAM", url: "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html", publisher: "AWS" }
  - { title: "What is Privileged Identity Management?", url: "https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure", publisher: "Microsoft" }
---

## Explanation

Least privilege is the oldest rule in the access-control canon still in daily use. Saltzer and Schroeder stated it in 1975 as one of eight design principles for protection mechanisms: every program and every user should operate using the least set of privileges necessary to complete the job. They observed that its main benefit is limiting the damage from an accident or error, and that the military "need-to-know" rule is the same idea applied to people. NIST's current definitions say the same thing in control language: each entity is granted the minimum system resources and authorizations needed to perform its function, and SP 800-53 turns that into control AC-6 with enhancements covering privileged accounts, periodic review of user privileges, logging the use of privileged functions and separating security functions from everyday work.

The principle has three dimensions, and most violations come from forgetting one of them:

1. **Scope**: which resources. A service that reads one storage container should not be able to list the whole account.
2. **Rights**: which actions. A reporting job needs `SELECT`, never `DROP`.
3. **Time**: how long. Standing administrator rights are the classic failure; just-in-time (JIT) elevation and short-lived credentials shrink the window in which a stolen credential is useful.

It applies to four kinds of subject. **People** get job-function roles, separate administrator accounts and JIT activation. **Workloads** get a [workload identity](workload-identity.md) with a narrowly scoped role instead of an [API key](api-key.md) that unlocks everything. **Processes** get kernel-level restrictions: a container that drops all Linux capabilities, runs as non-root with a read-only root filesystem, or a module running in a [Wasm sandbox](wasm-sandboxing.md) that can only touch the directories it was handed. **AI agents** get tool allow-lists and tokens scoped to the current step; the MCP authorization specification asks servers to advertise the minimal scopes an operation needs and clients to request only those, stepping up when a later operation demands more.

Least privilege is also a *process*, because the right set of permissions is rarely known up front. Both big clouds now ship the loop as a product: AWS recommends starting from managed policies, observing actual use in CloudTrail, generating a fine-grained policy with IAM Access Analyzer, and removing unused roles, keys and permissions flagged by its unused-access findings; Azure recommends narrow scopes and groups, PIM-eligible rather than permanent assignments, access reviews, and conditions that filter a role assignment down to specific blobs or tags. Guardrails sit above the loop: AWS permissions boundaries and service control policies, and in Azure a role assignment condition on the Role Based Access Control Administrator role (limiting which roles and principal types a delegated administrator may assign) plus Azure Policy, cap what a delegated administrator can ever grant.

In the reader's stack the principle shows up at every layer: a Redis Streams consumer whose ACL user may only `XREADGROUP` and `XACK` on its own stream, a TimescaleDB ingest role that may insert into one hypertable but not read customer tables, an Angular single-page app that asks the identity provider for the one scope the current screen needs, and a Docker Compose service with `cap_drop: [ALL]`, `read_only: true` and a non-root `user`. [Zero trust](zero-trust.md) depends on it directly: NIST SP 800-207 defines the paradigm around *least privilege per-request access decisions*, which is least privilege re-evaluated on every call rather than granted once at provisioning time.

```mermaid
flowchart LR
    A[Grant a starting role\nor managed policy] --> B[Observe real use\nCloudTrail / activity logs]
    B --> C[Generate or hand-write\na narrow policy]
    C --> D[Review: unused permissions,\nlast-accessed, access reviews]
    D --> E[Remove standing rights\nmake the rest eligible / JIT]
    E --> B
```

## How it differs

| Neighbour | What it is | The decisive difference | How to choose |
| --- | --- | --- | --- |
| [Zero trust](zero-trust.md) | An architecture: policy engine, enforcement points, continuous evaluation | Zero trust decides *when and how* access is checked; least privilege decides *how much* is granted | You need both; least privilege is the content of zero trust policies |
| [RBAC](rbac.md) | Permissions bundled into roles assigned to users | A mechanism that can honour or violate the principle; broad roles at broad scopes are RBAC without least privilege | Use RBAC to administer, measure each role against least privilege |
| [Capability-based authorization](capability-based-authorization.md) | Scoped, attenuable tokens that carry authority | A representation that makes narrowing cheap; the principle is the reason to narrow | Use capabilities where delegation and intermediaries make RBAC leaky |
| [Wasm sandboxing](wasm-sandboxing.md) | A runtime that grants a module only explicit imports | Enforces least privilege for code at the VM boundary only | Use it for untrusted code; still apply the principle to identities above it |
| [Container isolation](container-isolation.md) | Namespaces, cgroups, seccomp and capabilities around a process | A boundary, not a permission set; what runs inside still has whatever capabilities and cloud roles you left it | Always harden the container, then narrow the identity it runs as |

**Versus zero trust.** A perimeter network with a tightly scoped service account is practising least privilege without zero trust; a zero trust deployment that grants every verified user the Contributor role is doing the opposite. Zero trust adds dynamic, per-request, context-aware decisions and continuous re-evaluation; least privilege is the standard those decisions should converge on. Microsoft's three zero trust principles list "use least privilege access" explicitly alongside "verify explicitly" and "assume breach".

**Versus RBAC.** Roles are a way of writing permissions down. Sandhu and colleagues noted in 1996 that RBAC *supports* least privilege, because a role can be configured with only the permissions its tasks need, but cannot *enforce* it, because a security officer can configure roles that violate it. In practice the violation is usually scope rather than rights: a role that is reasonable at resource-group scope becomes excessive at subscription scope, and Azure RBAC is additive, so the broader assignment wins.

**Versus capabilities.** Capabilities answer the "how" with attenuation: whoever holds a token narrows it before passing it on, so the last link in a chain holds the least. The principle does not care whether you reached that state with a caveat, a session policy, a role at a narrow scope or a database grant; it only asks that the final permission set match the task.

**Versus Wasm sandboxing.** The sandbox is least privilege for *code*: no file, socket or clock unless the host hands one over. It does nothing about the cloud identity the host process runs under, which is where most real excess lives.

**Versus container isolation.** A container is a boundary that limits what a process can see of the host; least privilege is about what the process may *do* within and beyond that boundary. Docker still grants a default set of Linux capabilities and runs as root unless told otherwise, and the container's workload identity carries whatever cloud role you assigned, so an isolated container can be wildly over-privileged. Treat the container flags (`cap_drop`, non-root `user`, `read_only`) and the identity's role assignments as two separate applications of the same principle.

## Examples

=== "C#"

    ```csharp
    // ASP.NET Core (.NET 9): the API only accepts tokens scoped to what this endpoint does,
    // and connects to TimescaleDB as a role that can only read the reporting schema.
    using Npgsql;

    var builder = WebApplication.CreateBuilder(args);

    builder.Services.AddAuthentication().AddJwtBearer(o => o.MapInboundClaims = false); // Authority/Audience from configuration
    builder.Services.AddAuthorizationBuilder()
        .AddPolicy("reports.read", p => p.RequireAuthenticatedUser().RequireAssertion(ctx =>
            // "scope" is one space-separated string, so RequireClaim("scope", "reports.read") would miss multi-scope tokens
            ctx.User.FindFirst("scope")?.Value.Split(' ').Contains("reports.read") == true));

    // Connection string names a least-privilege login, not the owner:
    //   CREATE ROLE reports_reader LOGIN PASSWORD '...';
    //   GRANT USAGE ON SCHEMA market TO reports_reader;
    //   GRANT SELECT ON market.daily_bars TO reports_reader;   -- a continuous aggregate, not the raw hypertable
    builder.Services.AddNpgsqlDataSource(builder.Configuration.GetConnectionString("ReportsReader")!);

    var app = builder.Build();

    app.MapGet("/reports/{symbol}", async (string symbol, NpgsqlDataSource db) =>
    {
        await using var cmd = db.CreateCommand("SELECT bucket, close FROM market.daily_bars WHERE symbol = $1 ORDER BY bucket DESC LIMIT 30");
        cmd.Parameters.AddWithValue(symbol);
        await using var reader = await cmd.ExecuteReaderAsync();
        var rows = new List<object>();
        while (await reader.ReadAsync()) rows.Add(new { bucket = reader.GetDateTime(0), close = reader.GetDecimal(1) });
        return Results.Ok(rows);
    }).RequireAuthorization("reports.read");

    app.Run();
    ```

=== "Python"

    ```python
    # FastAPI equivalent: scope check per endpoint, read-only database role.
    import jwt, psycopg
    from fastapi import Depends, FastAPI, HTTPException, Request

    app = FastAPI()
    DSN = "postgresql://reports_reader:...@timescale:5432/market"   # SELECT-only role

    def require_scope(required: str):
        def dep(request: Request) -> dict:
            token = request.headers.get("authorization", "").removeprefix("Bearer ").strip()
            try:
                claims = jwt.decode(token, options={"verify_signature": False})  # verify with your IdP's JWKS in production
            except jwt.PyJWTError:
                raise HTTPException(401) from None
            if required not in claims.get("scope", "").split():
                raise HTTPException(403, f"scope {required} required")
            return claims
        return dep

    @app.get("/reports/{symbol}")
    def report(symbol: str, _: dict = Depends(require_scope("reports.read"))):
        with psycopg.connect(DSN) as conn:
            rows = conn.execute(
                "SELECT bucket, close FROM market.daily_bars WHERE symbol = %s ORDER BY bucket DESC LIMIT 30",
                (symbol,),
            ).fetchall()
        return [{"bucket": b, "close": c} for b, c in rows]
    ```

=== "Containers"

    ```yaml
    # docker-compose.yml: the process can only do what the image needs
    services:
      ingest:
        image: ghcr.io/example/ingest:1.4
        user: "10001:10001"                 # not root
        read_only: true                     # immutable root filesystem
        tmpfs: [/tmp]
        cap_drop: [ALL]                     # drop even Docker's default capability set
        security_opt:
          - no-new-privileges:true          # setuid binaries cannot escalate
    ```

    The Kubernetes equivalent is the Pod Security Standards *Restricted* profile: `allowPrivilegeEscalation: false`, `capabilities.drop: [ALL]` (only `NET_BIND_SERVICE` may be added back), `runAsNonRoot: true` and a `RuntimeDefault` or `Localhost` seccomp profile, enforced per namespace with the `pod-security.kubernetes.io/enforce: restricted` label.

=== "Azure"

    ```bash
    # Narrow scope: the ingest identity reads one storage account, nothing else in the subscription
    az role assignment create \
      --assignee-object-id "$INGEST_MI_OBJECT_ID" --assignee-principal-type ServicePrincipal \
      --role "Storage Blob Data Reader" \
      --scope "/subscriptions/$SUB/resourceGroups/rg-market/providers/Microsoft.Storage/storageAccounts/stmarket"
    ```

    For people, make privileged assignments *eligible* in Microsoft Entra Privileged Identity Management rather than *active*: the user activates for a bounded duration, with MFA, a justification and optionally an approval, and access reviews confirm the eligibility is still needed. Azure's own best-practice guidance adds: at most three subscription owners, roles assigned to groups rather than users, no wildcards in custom roles, and role assignment conditions (Azure ABAC) when a role is still too broad for the data it reaches.

=== "AWS"

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::market-reports/acme/*",
        "Condition": { "Bool": { "aws:SecureTransport": "true" } }
      }]
    }
    ```

    Attach that as a customer managed policy to the workload's IAM role (temporary credentials, never long-term access keys), and set a permissions boundary when developers may create their own roles so the boundary caps whatever they grant. Then run the reduction loop: `aws accessanalyzer create-analyzer --analyzer-name unused-access --type ACCOUNT_UNUSED_ACCESS` surfaces unused roles, keys, passwords and permissions; last-accessed information and Access Analyzer policy generation from CloudTrail produce the narrower policy; service control policies and resource control policies hold the organisation-wide ceiling.

## Misconceptions

- **"Least privilege means read-only."** It means *task-sufficient*. A deployment pipeline legitimately needs write and delete on its own resources; what it should not have is the same rights on everything else, or standing rights between deployments.
- **"We use RBAC, so we have least privilege."** Roles are containers; an over-broad built-in role at subscription scope, or `cluster-admin` bound cluster-wide, is RBAC and the opposite of least privilege. Measure each assignment's scope, rights and duration.
- **"Permissions boundaries and SCPs grant least privilege."** They grant nothing; they are ceilings. Effective permission is the intersection of what the identity policy allows and what the boundary permits, so you still need a narrow identity policy underneath.
- **"Service accounts are exempt because nobody logs in with them."** Non-person entities are the subjects attackers prefer: NIST SP 800-207 warns that software agents often authenticate with weaker factors than humans, and an agent with broad rights is an ideal confused deputy.
- **"Least privilege is a one-time provisioning task."** Permissions drift as systems change; without last-accessed data, access reviews and unused-access findings, every system grows toward "everything, forever".

## Exam notes

Every security exam in this library tests the principle, usually by hiding it inside a scenario. Security+ and CISSP ask for the name when a scenario limits damage from a compromised account, and pair it with separation of duties and need-to-know; the trap is choosing "defence in depth" when the question is about the *amount* of access. SC-900, SC-300, AZ-104, AZ-305 and AZ-500 express it through Azure RBAC scope selection (resource group over subscription), PIM eligible assignments with JIT activation, access reviews, and Azure ABAC conditions, and the wrong answers are usually a broader built-in role or a permanent assignment. SAA-C03, SAP-C03, DVA-C03 and SCS-C03 express it through IAM: temporary credentials via roles, customer managed policies narrower than AWS managed ones, permissions boundaries for delegated administration, Access Analyzer unused-access findings and policy generation, and SCPs as guardrails rather than grants. CKAD, CKS and KCSA test the container form: `securityContext` with dropped capabilities and non-root users, Pod Security Standards levels, and namespaced Roles over ClusterRoles. CCSP and CAS-005 expect you to connect the principle to zero trust and to the shared-responsibility model, and the MCPA certification tests scope minimisation and step-up authorization for agent tools.

## Self-check

??? question "A data-science team's role has had Contributor on the whole subscription for a year. They say they only touch two storage accounts and one AKS cluster. What is the least-privilege remediation, in order?"
    First, observe rather than guess: review activity logs and Defender for Cloud recommendations to confirm which resources and operations the role actually used. Second, replace the subscription-scope Contributor assignment with job-function roles at the narrowest scope that matches that usage, for example Storage Blob Data Contributor on the two accounts and Azure Kubernetes Service Cluster User Role on the cluster (plus a Kubernetes or Azure RBAC for Kubernetes role for what they do inside it), assigned to a group rather than individuals. Third, make anything administrative eligible in PIM with time-bound activation and an approval, and schedule an access review. Finally, remove the old assignment only after the new ones have been exercised, so the change does not become an outage.

??? question "An AWS Lambda function assumes a role with AmazonS3FullAccess. It reads from one bucket and writes to one prefix in another. How do you get to least privilege without breaking it?"
    Keep the function running while you measure: use IAM Access Analyzer policy generation on the role's CloudTrail activity to produce a policy listing the actions and resources it actually used, then hand-check it against the design (GetObject on the source bucket, PutObject on the destination prefix, plus any KMS actions the buckets' encryption requires). Attach the generated customer managed policy, remove the AWS managed policy, and confirm with last-accessed data after a full business cycle that nothing else is needed. If other teams create roles in the account, add a permissions boundary so the ceiling stays fixed even if someone later edits the policy.

??? question "Your orchestrator gives every MCP tool the same bearer token with all scopes, because requesting scopes per tool is awkward. Why is this a least-privilege problem rather than merely untidy, and what does the MCP specification suggest instead?"
    A token with every scope turns any single tool into a confused deputy: a prompt-injected or buggy tool can exercise the orchestrator's entire authority, and audit logs cannot attribute actions to the step that should have performed them. The MCP authorization specification has servers announce the minimal scopes in the `WWW-Authenticate` challenge and asks clients to request only those, then to step up with the union of previously granted and newly challenged scopes when an operation needs more. Combining that with a short-lived, audience-bound token per tool invocation gives each step only the rights its task needs, for only as long as the step runs.

## Further reading

- [Workload Identity](../security/iam/workload-identity.md) and [mTLS vs. API Keys](../security/iam/mtls-vs-api-keys.md): the identity layer that makes narrowly scoped permissions possible for services.
- [Capability-Based AuthZ vs. RBAC](../security/iam/capability-based-authz.md) and [Wasm Sandboxing vs. Container Isolation](../security/appsec/wasm-sandboxing.md): two mechanisms for enforcing least privilege at different layers.
- [Docker and containerization](../devops/docker-containerization.md) for process-level hardening, and [MCP tool orchestration](../ai/protocols/mcp-tool-orchestration.md) for agent tool scoping.
- Term pages: [Zero Trust Architecture](zero-trust.md), [Role-Based Access Control](rbac.md), [Capability-Based Authorization](capability-based-authorization.md), [Secrets Rotation](secrets-rotation.md).
- Primary sources: Saltzer and Schroeder's principles (<http://web.mit.edu/Saltzer/www/publications/protection/Basic.html>), Azure RBAC best practices (<https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices>), IAM Access Analyzer (<https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html>) and Kubernetes Pod Security Standards (<https://kubernetes.io/docs/concepts/security/pod-security-standards/>).
