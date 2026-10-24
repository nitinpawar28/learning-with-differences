---
title: "Bare-Metal Linux Home Servers & Hypervisors"
description: Virtualization and home-lab infrastructure trade-offs.
tags:
  - devops
  - homelab
  - virtualization
---

# Bare-Metal Linux Home Servers & Hypervisors

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- Type-1 hypervisors (Proxmox, ESXi) vs. Type-2 (KVM/QEMU on a Linux host) vs. plain LXC/Docker
- Proxmox VE vs. bare Debian + libvirt for a home lab
- VMs vs. containers vs. Docker-on-VM for isolating home services
- ZFS vs. ext4/XFS for a home NAS/hypervisor host
- Networking: bridged VMs vs. VLAN-segmented services
