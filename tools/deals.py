import httpx
from base import get_apollo_client

async def apollo_create_deal(
    name: str,
    owner_id: str = None,
    account_id: str = None,
    amount: str = None,
    opportunity_stage_id: str = None,
    closed_date: str = None
):
    url = "https://api.apollo.io/api/v1/opportunities"
    params = {
        "name": name,
        "owner_id": owner_id,
        "account_id": account_id,
        "amount": amount,
        "opportunity_stage_id": opportunity_stage_id,
        "closed_date": closed_date
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


async def apollo_list_all_deals(
    sort_by_field: str = None,
    page: int = None,
    per_page: int = None
):
    url = "https://api.apollo.io/api/v1/opportunities/search"
    params = {
        "sort_by_field": sort_by_field,
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

async def apollo_view_deal(opportunity_id: str):
    url = f"https://api.apollo.io/api/v1/opportunities/{opportunity_id}"
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


async def apollo_update_deal(
    opportunity_id: str,
    owner_id: str = None,
    name: str = None,
    amount: str = None,
    opportunity_stage_id: str = None,
    closed_date: str = None,
    is_closed: bool = None,
    is_won: bool = None,
    source: str = None,
    account_id: str = None
):
    url = f"https://api.apollo.io/api/v1/opportunities/{opportunity_id}"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "owner_id": owner_id,
        "name": name,
        "amount": amount,
        "opportunity_stage_id": opportunity_stage_id,
        "closed_date": closed_date,
        "is_closed": is_closed,
        "is_won": is_won,
        "source": source,
        "account_id": account_id
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.patch(url, headers=headers, params=params)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

async def apollo_list_deal_stages():
    url = "https://api.apollo.io/api/v1/opportunity_stages"
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.text
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
