import httpx
from .base import get_apollo_client

async def apollo_create_tasks(
    user_id: str,
    contact_ids: list,
    priority: str,
    due_at: str,
    task_type: str,
    status: str,
    note: str = None
):
    url = "https://api.apollo.io/api/v1/tasks/bulk_create"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "user_id": user_id,
        "contact_ids[]": contact_ids,
        "priority": priority,
        "due_at": due_at,
        "type": task_type,
        "status": status
    }

    if note:
        params["note"] = note

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            response.raise_for_status()
            return response.text  # should return "true"
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


async def apollo_search_tasks(
        sort_by_field: str = None,
        open_factor_names: list = None,
        page: int = None,
        per_page: int = None
):
    url = "https://api.apollo.io/api/v1/tasks/search"
    params = {
        "sort_by_field": sort_by_field,
        "page": page,
        "per_page": per_page
    }

    if open_factor_names:
        params["open_factor_names[]"] = open_factor_names

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
