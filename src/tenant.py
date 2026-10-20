from dataclasses import dataclass
from typing import Dict, Optional, List
import uuid
from datetime import datetime

@dataclass
class Tenant:
    id: str
    name: str
    subdomain: str
    plan: str
    created_at: datetime
    is_active: bool = True

class TenantManager:
    def __init__(self):
        self._tenants: Dict[str, Tenant] = {}

    def create_tenant(self, name: str, subdomain: str, plan: str = "starter") -> Tenant:
        if not name or not subdomain:
            raise ValueError("Tenant name and subdomain are required")
        sub = subdomain.lower().strip()
        if any(t.subdomain == sub for t in self._tenants.values()):
            raise ValueError(f"Subdomain '{sub}' is already taken")
        
        tenant_id = str(uuid.uuid4())
        tenant = Tenant(
            id=tenant_id,
            name=name.strip(),
            subdomain=sub,
            plan=plan,
            created_at=datetime.utcnow()
        )
        self._tenants[tenant_id] = tenant
        return tenant

    def get_tenant(self, subdomain: str) -> Optional[Tenant]:
        sub = subdomain.lower().strip()
        for t in self._tenants.values():
            if t.subdomain == sub and t.is_active:
                return t
        return None

    def list_tenants(self) -> List[Tenant]:
        return list(self._tenants.values())
