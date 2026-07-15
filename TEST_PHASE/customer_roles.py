import json
import os
import random
from typing import Any, Dict, Optional, Tuple

__all__ = ["Admin", "DeliveryBoy"]


# =============================================================================
# Helper functions
# =============================================================================

def _normalize_customer_id(customer_id: Any) -> str:
    """Convert customer ID to a clean string, because JSON keys are strings."""
    return str(customer_id).strip()


def _load_data(file_path: str) -> Dict[str, Dict[str, Any]]:
    """Load customer data from JSON file. If file is missing or invalid, return empty dict."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_data(file_path: str, data: Dict[str, Dict[str, Any]]) -> None:
    """Save customer data back to JSON file."""
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def _generate_otp() -> str:
    """Generate a 6-digit OTP as a string."""
    return str(random.randint(100000, 999999))


def _next_extra_key(customer_record: Dict[str, Any]) -> str:
    """Generate a unique extra key like extra_1, extra_2, extra_3..."""
    index = 1
    while f"extra_{index}" in customer_record:
        index += 1
    return f"extra_{index}"


# =============================================================================
# ADMIN CLASS
# =============================================================================
class Admin:
    """
    Admin role class.

    Import this class into your Admin page like this:

        from customer_roles import Admin
        admin = Admin("path/to/user_delivery_data.json")

    Then use the methods below inside your Admin page code.
    This class does NOT contain any GUI or navigation logic.
    """

    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path
        self.data = _load_data(self.json_file_path)

    def _refresh(self) -> None:
        """Reload latest data from file before every operation."""
        self.data = _load_data(self.json_file_path)

    def _persist(self) -> None:
        """Save current data to file."""
        _save_data(self.json_file_path, self.data)

    # -------------------------------------------------------------------------
    # ADMIN METHOD: Search customer
    # Use this in your Admin page to check whether a customer exists.
    # Example:
    #     if admin.search_customer(customer_id):
    #         ...
    # -------------------------------------------------------------------------
    def search_customer(self, customer_id: Any) -> bool:
        self._refresh()
        cid = _normalize_customer_id(customer_id)
        return cid in self.data

    # -------------------------------------------------------------------------
    # ADMIN METHOD: View customer details
    # Use this in your Admin page to display customer JSON data.
    # Example:
    #     details = admin.view_customer_details(customer_id)
    # -------------------------------------------------------------------------
    def view_customer_details(self, customer_id: Any) -> Optional[Dict[str, Any]]:
        self._refresh()
        cid = _normalize_customer_id(customer_id)

        record = self.data.get(cid)
        if isinstance(record, dict):
            return dict(record)  # return a copy
        return None

    # -------------------------------------------------------------------------
    # ADMIN METHOD: Update customer details
    # Use this in your Admin page when you want to update an EXISTING key.
    # Example:
    #     admin.update_customer_details(customer_id, "status", "Delivered")
    #
    # Note:
    #     This method updates only existing keys.
    #     If you want to add a brand-new field, use add_extra_info().
    # -------------------------------------------------------------------------
    def update_customer_details(self, customer_id: Any, key: str, value: Any) -> bool:
        self._refresh()
        cid = _normalize_customer_id(customer_id)
        key = str(key).strip()

        if cid not in self.data or not isinstance(self.data[cid], dict):
            return False

        if key not in self.data[cid]:
            return False

        self.data[cid][key] = value
        self._persist()
        return True

    # -------------------------------------------------------------------------
    # ADMIN METHOD: Add extra info
    # Use this in your Admin page when you want to add a new custom field.
    # Example:
    #     success, generated_key = admin.add_extra_info(customer_id, "Urgent delivery")
    # -------------------------------------------------------------------------
    def add_extra_info(self, customer_id: Any, extra_value: Any) -> Tuple[bool, Optional[str]]:
        self._refresh()
        cid = _normalize_customer_id(customer_id)

        if cid not in self.data or not isinstance(self.data[cid], dict):
            return False, None

        extra_key = _next_extra_key(self.data[cid])
        self.data[cid][extra_key] = extra_value
        self._persist()
        return True, extra_key

    # -------------------------------------------------------------------------
    # ADMIN METHOD: Delete customer
    # Use this in your Admin page to permanently remove a customer record.
    # Example:
    #     admin.delete_customer(customer_id)
    # -------------------------------------------------------------------------
    def delete_customer(self, customer_id: Any) -> bool:
        self._refresh()
        cid = _normalize_customer_id(customer_id)

        if cid not in self.data:
            return False

        del self.data[cid]
        self._persist()
        return True


# =============================================================================
# DELIVERY BOY CLASS
# =============================================================================
class DeliveryBoy:
    """
    DeliveryBoy role class.

    Import this class into your Delivery Boy page like this:

        from customer_roles import DeliveryBoy
        delivery_boy = DeliveryBoy("path/to/user_delivery_data.json")

    Then use the methods below inside your Delivery Boy page code.
    This class does NOT contain any GUI or navigation logic.
    """

    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path
        self.data = _load_data(self.json_file_path)

        # Optional in-memory request cache.
        # The actual request info is also written inside the customer's record
        # so your future customer interface can read it later.
        self.pending_requests: Dict[str, Dict[str, Any]] = {}

    def _refresh(self) -> None:
        """Reload latest data from file before every operation."""
        self.data = _load_data(self.json_file_path)

    def _persist(self) -> None:
        """Save current data to file."""
        _save_data(self.json_file_path, self.data)

    # -------------------------------------------------------------------------
    # DELIVERY BOY METHOD: Search customer
    # Use this in your Delivery Boy page to check whether a customer exists.
    # Example:
    #     if delivery_boy.search_customer(customer_id):
    #         ...
    # -------------------------------------------------------------------------
    def search_customer(self, customer_id: Any) -> bool:
        self._refresh()
        cid = _normalize_customer_id(customer_id)
        return cid in self.data

    # -------------------------------------------------------------------------
    # DELIVERY BOY METHOD: View customer details
    # Use this in your Delivery Boy page to display customer JSON data.
    # Example:
    #     details = delivery_boy.view_customer_details(customer_id)
    # -------------------------------------------------------------------------
    def view_customer_details(self, customer_id: Any) -> Optional[Dict[str, Any]]:
        self._refresh()
        cid = _normalize_customer_id(customer_id)

        record = self.data.get(cid)
        if isinstance(record, dict):
            return dict(record)  # return a copy
        return None

    # -------------------------------------------------------------------------
    # DELIVERY BOY METHOD: Request delivery status change
    # Use this in your Delivery Boy page when the delivery boy wants to
    # request a status change and generate an OTP.
    #
    # Example:
    #     otp = delivery_boy.request_status_change(customer_id, "Delivered")
    #
    # Important:
    #     This method does NOT directly finalize the delivery status.
    #     It stores a pending request + OTP in the customer record so your
    #     future customer page can verify the OTP and approve the change.
    # -------------------------------------------------------------------------
    def request_status_change(
        self,
        customer_id: Any,
        requested_status: Optional[str] = None
    ) -> Optional[str]:
        self._refresh()
        cid = _normalize_customer_id(customer_id)

        if cid not in self.data or not isinstance(self.data[cid], dict):
            return None

        otp = _generate_otp()

        request_info = {
            "requested_status": requested_status,
            "otp": otp,
            "pending": True
        }

        # Keep a local copy too
        self.pending_requests[cid] = request_info

        # Persist request info inside the customer record for future customer UI
        self.data[cid]["delivery_request_pending"] = True
        self.data[cid]["delivery_request_otp"] = otp
        self.data[cid]["delivery_request_status"] = requested_status

        self._persist()
        return otp

    # -------------------------------------------------------------------------
    # DELIVERY BOY METHOD: Get pending request
    # Optional helper for your Delivery Boy page if you want to inspect
    # the latest request details for a customer.
    # Example:
    #     request = delivery_boy.get_pending_request(customer_id)
    # -------------------------------------------------------------------------
    def get_pending_request(self, customer_id: Any) -> Optional[Dict[str, Any]]:
        self._refresh()
        cid = _normalize_customer_id(customer_id)

        if cid in self.pending_requests:
            return dict(self.pending_requests[cid])

        record = self.data.get(cid)
        if isinstance(record, dict) and record.get("delivery_request_pending"):
            return {
                "requested_status": record.get("delivery_request_status"),
                "otp": record.get("delivery_request_otp"),
                "pending": True
            }

        return None