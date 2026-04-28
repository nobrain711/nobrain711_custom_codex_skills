---
name: k8s
description: Create, review, or improve Kubernetes manifests and deployment workflows. Use when Codex works on Deployments, Services, Ingress, ConfigMaps, Secrets references, probes, resources, namespaces, Helm-style values, Kustomize overlays, kubectl commands, or Kubernetes operational documentation.
---

# K8s

## Goal

Create Kubernetes configuration that is explicit, reviewable, and safe to apply.

## Rules

- Inspect existing manifests before adding new resource patterns.
- Include labels and selectors consistently; ensure Services match Pod labels.
- Add readiness and liveness probes when the application has a meaningful health endpoint or command.
- Specify resource requests and limits for deployable workloads unless the project intentionally omits them.
- Do not place raw secret values in manifests. Reference Kubernetes Secrets or external secret systems instead.
- Keep environment-specific differences in overlays, values files, or clearly named manifests.
- Prefer `kubectl diff` or dry-run guidance before apply commands when changing live resources.
- Do not assume a namespace, ingress class, storage class, or cluster provider unless it is present in the project.

## Documentation Style

Write manifest comments in Korean only when they clarify operational intent or non-obvious constraints.

When giving commands, prefer review-first examples:

```powershell
kubectl diff -f k8s/
kubectl apply -f k8s/
```
