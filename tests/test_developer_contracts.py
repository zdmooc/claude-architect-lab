"""Server-side authorization is mandatory even if prompt says otherwise."""
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "labs" / "developer_foundations"))
from contracts import get_authorized_contract, ContractAccessDenied


def test_owner_can_consult_and_gets_minimized_data():
    r = get_authorized_contract(subject_id="SYN-U-1", contract_id="SYN-C-001")
    assert r == {"id": "SYN-C-001", "status": "actif", "type": "auto"}
    assert "owner" not in r


@pytest.mark.parametrize("subject,contract", [
    ("SYN-U-1", "SYN-C-002"),
    ("SYN-U-2", "SYN-C-001"),
    ("", "SYN-C-001"),
    ("SYN-U-1", ""),
    ("SYN-U-1", "MISSING"),
])
def test_bola_or_missing_identity_fails_closed(subject, contract):
    with pytest.raises(ContractAccessDenied):
        get_authorized_contract(subject_id=subject, contract_id=contract)


def test_no_error_message_reveals_foreign_owner():
    with pytest.raises(ContractAccessDenied) as exc:
        get_authorized_contract(subject_id="SYN-U-1", contract_id="SYN-C-002")
    assert "SYN-U-2" not in str(exc.value)


def test_empty_repository_does_not_fallback_to_global_data():
    with pytest.raises(ContractAccessDenied):
        get_authorized_contract(subject_id="SYN-U-1",
                                contract_id="SYN-C-001", contracts={})
