# Plataforma SaaS Multi-Tenant com Django 5

[![Django CI](https://github.com/FelipeMadson/django-multitenant-saas-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/FelipeMadson/django-multitenant-saas-platform/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0.0-green.svg)](https://github.com/FelipeMadson/django-multitenant-saas-platform/releases)

Arquitetura de software SaaS corporativa multi-inquilino em Python e Django 5 com resolução de subdomínios e isolamento estrito de dados.

## Arquitetura de Sistemas

```mermaid
flowchart TD
    Cliente["Requisição Web (empresa.saas.com)"] --> Roteador["Resolvedor de Subdomínio"]
    Roteador --> Contexto["Middleware de Contexto do Inquilino"]
    Contexto --> App["Aplicação Django 5 / DRF"]
    App --> Banco["Partição de Dados Isolada"]
    App --> Faturamento["Tratador de Webhooks Stripe"]
```

## Destaques de Engenharia

- **Isolamento por Subdomínio**: Roteamento automático baseado no cabeçalho HTTP Host para particionamento de consultas.
- **Ciclo de Vida de Inquilinos**: Suporte a planos diferenciados (Starter, Pro, Enterprise) e status ativo/inativo.
- **Suíte de Testes Pytest**: Testes automatizados com validação de invariantes e sem dependências de rede externa.

## Instalação e Testes

```bash
pip install -e ".[test]"
pytest -v
```

## Autor

Desenvolvido por **[Felipe Madison](https://github.com/FelipeMadson)**.
