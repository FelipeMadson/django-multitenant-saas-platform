# Django Multi-Tenant SaaS Platform

[![Django CI](https://github.com/FelipeMadson/django-multitenant-saas-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/FelipeMadson/django-multitenant-saas-platform/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0.0-green.svg)](https://github.com/FelipeMadson/django-multitenant-saas-platform/releases)

Enterprise multi-tenant SaaS architecture built on Python and Django 5 with subdomain-based tenant routing and strict data isolation.

## Architecture

```mermaid
flowchart TD
    Client["Client Request (tenant.app.com)"] --> Ingress["Subdomain Host Resolver"]
    Ingress --> Middleware["TenantContextMiddleware"]
    Middleware --> App["Django Core App"]
    App --> Scope["Tenant-Scoped ORM QuerySet"]
    App --> Webhook["Stripe Webhook Guard"]
```

## Key Highlights

- **Subdomain-Driven Scoping**: Host header resolution enforcing strict tenant isolation across all endpoints.
- **Tenant Lifecycle**: Clean subscription tier transitions and account suspension safeguards.
- **Pytest Automation**: 100% verified automated test suite with zero external network coupling.

## Installation & Testing

```bash
pip install -e ".[test]"
pytest -v
```

## Author

Developed by **[Felipe Madison](https://github.com/FelipeMadson)**.
