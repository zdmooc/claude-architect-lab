"""Synthetic read-only contract access with server-side ownership checks.

This is NOT an IAM/OIDC implementation and MUST NOT be deployed to production.
"""


class ContractAccessDenied(PermissionError):
    """Fail-closed access denial; caller must not disclose contract details."""


SYNTHETIC_CONTRACTS = {
    "SYN-C-001": {"owner": "SYN-U-1", "status": "actif", "type": "auto"},
    "SYN-C-002": {"owner": "SYN-U-2", "status": "resilie", "type": "habitation"},
}


def get_authorized_contract(*, subject_id: str, contract_id: str,
                            contracts: dict | None = None) -> dict:
    """Authorize on every call, not using any instruction from Claude."""
    store = SYNTHETIC_CONTRACTS if contracts is None else contracts
    if not isinstance(subject_id, str) or not subject_id:
        raise ContractAccessDenied("Missing authenticated subject")
    if not isinstance(contract_id, str) or not contract_id:
        raise ContractAccessDenied("Missing contract identifier")
    contract = store.get(contract_id)
    # An unknown ID and a foreign-owned ID are indistinguishable to caller.
    if not isinstance(contract, dict) or contract.get("owner") != subject_id:
        raise ContractAccessDenied("Contract is unavailable to this subject")
    # Least data: the model does not need the owner ID.
    return {"id": contract_id,
            "status": contract["status"],
            "type": contract["type"]}
