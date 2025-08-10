import httpx
from .base import get_apollo_client

import httpx

async def apollo_create_account(
    name: str = None,
    domain: str = None,
    owner_id: str = None,
    account_stage_id: str = None,
    phone: str = None,
    raw_address: str = None
):
    if name is None and domain is None:
        return {"error": "Either name or domain must be provided"}

    url = 'https://api.apollo.io/api/v1/accounts'
    data = {
        'name': name,
        'domain': domain,
        'owner_id': owner_id,
        'account_stage_id': account_stage_id,
        'phone': phone,
        'raw_address': raw_address
    }

    headers = get_apollo_client()

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()  # raises if not 2xx
            return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

async def apollo_update_account(
    account_id: str,
    name: str = None,
    domain: str = None,
    owner_id: str = None,
    account_stage_id: str = None,
    raw_address: str = None,
    phone: str = None
):
    if not account_id:
        return {"error": "account_id is required"}

    url = f"https://api.apollo.io/api/v1/accounts/{account_id}"
    data = {
        "name": name,
        "domain": domain,
        "owner_id": owner_id,
        "account_stage_id": account_stage_id,
        "raw_address": raw_address,
        "phone": phone
    }
    headers = get_apollo_client()  # Must return master API key headers

    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, json=data)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


async def apollo_search_accounts(
    q_organization_name: str = None,
    account_stage_ids: list = None,
    sort_by_field: str = None,
    sort_ascending: bool = False,
    page: int = None,
    per_page: int = None
):
    url = "https://api.apollo.io/api/v1/accounts/search"
    params = {
        "q_organization_name": q_organization_name,
        "account_stage_ids[]": account_stage_ids,
        "sort_by_field": sort_by_field,
        "sort_ascending": sort_ascending,
        "page": page,
        "per_page": per_page
    }

    headers = get_apollo_client()  # Needs API key

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

async def apollo_view_account(account_id: str):
    url = f"https://api.apollo.io/api/v1/accounts/{account_id}"
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.text
    except Exception as e:
        return {"error": str(e)}

async def apollo_update_account_stage_bulk(
    account_ids: list,
    account_stage_id: str
):
    url = "https://api.apollo.io/api/v1/accounts/bulk_update"
    params = {
        "account_ids[]": account_ids,
        "account_stage_id": account_stage_id
    }

    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}

async def apollo_update_account_owner_bulk(
    account_ids: list,
    owner_id: str
):
    url = "https://api.apollo.io/api/v1/accounts/update_owners"
    params = {
        "account_ids[]": account_ids,
        "owner_id": owner_id
    }

    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}

async def apollo_list_account_stages():
    url = "https://api.apollo.io/api/v1/account_stages"
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.text
    except Exception as e:
        return {"error": str(e)}

