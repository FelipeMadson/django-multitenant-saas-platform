import pytest
from src.tenant import TenantManager

def test_tenant_creation_and_isolation():
    manager = TenantManager()
    t1 = manager.create_tenant("Acme Corp", "acme", "enterprise")
    t2 = manager.create_tenant("Stark Industries", "stark", "pro")

    assert t1.id != t2.id
    assert t1.subdomain == "acme"
    assert t2.subdomain == "stark"

    found = manager.get_tenant("ACME")
    assert found is not None
    assert found.id == t1.id

def test_duplicate_subdomain_conflict():
    manager = TenantManager()
    manager.create_tenant("Acme Corp", "acme")
    with pytest.raises(ValueError, match="already taken"):
        manager.create_tenant("Acme Clone", "acme")
