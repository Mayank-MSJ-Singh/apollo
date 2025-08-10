import httpx
from .base import get_apollo_client

async def apollo_create_call_record(
    logged: bool,
    user_ids: list,
    contact_id: str,
    account_id: str = None,
    to_number: str = None,
    from_number: str = None,
    status: str = None,
    start_time: str = None,
    end_time: str = None,
    duration: int = None,
    phone_call_purpose_id: str = None,
    phone_call_outcome_id: str = None,
    note: str = None
):
    url = "https://api.apollo.io/api/v1/phone_calls"
    params = {
        "logged": str(logged).lower(),
        "user_id[]": user_ids,
        "contact_id": contact_id,
        "account_id": account_id,
        "to_number": to_number,
        "from_number": from_number,
        "status": status,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "phone_call_purpose_id": phone_call_purpose_id,
        "phone_call_outcome_id": phone_call_outcome_id,
        "note": note
    }

    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


async def apollo_search_calls(
    date_range_max: str = None,
    date_range_min: str = None,
    duration_max: int = None,
    duration_min: int = None,
    inbound: str = None,
    user_ids: list = None,
    contact_label_ids: list = None,
    phone_call_purpose_ids: list = None,
    phone_call_outcome_ids: list = None,
    q_keywords: str = None,
    page: int = None,
    per_page: int = None
):
    url = "https://api.apollo.io/api/v1/phone_calls/search"
    params = {
        "date_range[max]": date_range_max,
        "date_range[min]": date_range_min,
        "duration[max]": duration_max,
        "duration[min]": duration_min,
        "inbound": inbound,
        "user_ids[]": user_ids,
        "contact_label_ids[]": contact_label_ids,
        "phone_call_purpose_ids[]": phone_call_purpose_ids,
        "phone_call_outcome_ids[]": phone_call_outcome_ids,
        "q_keywords": q_keywords,
        "page": page,
        "per_page": per_page
    }
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

async def apollo_update_call(
    call_id: str,
    logged: bool = None,
    user_ids: list = None,
    contact_id: str = None,
    account_id: str = None,
    to_number: str = None,
    from_number: str = None,
    status: str = None,
    start_time: str = None,
    end_time: str = None,
    duration: int = None,
    phone_call_purpose_id: str = None,
    phone_call_outcome_id: str = None,
    note: str = None
):
    url = f"https://api.apollo.io/api/v1/phone_calls/{call_id}"
    params = {
        "logged": logged,
        "user_id[]": user_ids,
        "contact_id": contact_id,
        "account_id": account_id,
        "to_number": to_number,
        "from_number": from_number,
        "status": status,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "phone_call_purpose_id": phone_call_purpose_id,
        "phone_call_outcome_id": phone_call_outcome_id,
        "note": note
    }
    headers = get_apollo_client()  # Your master API key headers here

    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url, headers=headers, params=params)
            response.raise_for_status()
            return response.text
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
