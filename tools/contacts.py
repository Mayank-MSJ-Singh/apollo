import httpx
from .base import get_apollo_client

async def apollo_create_contact(
    first_name=None,
    last_name=None,
    organization_name=None,
    title=None,
    account_id=None,
    email=None,
    website_url=None,
    label_names=None,
    contact_stage_id=None,
    present_raw_address=None,
    direct_phone=None,
    corporate_phone=None,
    mobile_phone=None,
    home_phone=None,
    other_phone=None
):
    url = "https://api.apollo.io/api/v1/contacts"
    headers = get_apollo_client()  # Needs master API key
    params = {
        "first_name": first_name,
        "last_name": last_name,
        "organization_name": organization_name,
        "title": title,
        "account_id": account_id,
        "email": email,
        "website_url": website_url,
        "label_names[]": label_names,
        "contact_stage_id": contact_stage_id,
        "present_raw_address": present_raw_address,
        "direct_phone": direct_phone,
        "corporate_phone": corporate_phone,
        "mobile_phone": mobile_phone,
        "home_phone": home_phone,
        "other_phone": other_phone
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}

async def apollo_update_contact(
    contact_id,
    first_name=None,
    last_name=None,
    organization_name=None,
    title=None,
    account_id=None,
    email=None,
    website_url=None,
    label_names=None,
    contact_stage_id=None,
    present_raw_address=None,
    direct_phone=None,
    corporate_phone=None,
    mobile_phone=None,
    home_phone=None,
    other_phone=None
):
    url = f"https://api.apollo.io/api/v1/contacts/{contact_id}"
    headers = get_apollo_client()  # Needs master API key
    params = {
        "first_name": first_name,
        "last_name": last_name,
        "organization_name": organization_name,
        "title": title,
        "account_id": account_id,
        "email": email,
        "website_url": website_url,
        "label_names[]": label_names,
        "contact_stage_id": contact_stage_id,
        "present_raw_address": present_raw_address,
        "direct_phone": direct_phone,
        "corporate_phone": corporate_phone,
        "mobile_phone": mobile_phone,
        "home_phone": home_phone,
        "other_phone": other_phone
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}


async def apollo_search_contacts(
    q_keywords=None,
    contact_stage_ids=None,
    sort_by_field=None,
    sort_ascending=None,
    per_page=None,
    page=None
):
    url = "https://api.apollo.io/api/v1/contacts/search"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "q_keywords": q_keywords,
        "contact_stage_ids[]": contact_stage_ids,
        "sort_by_field": sort_by_field,
        "sort_ascending": sort_ascending,
        "per_page": per_page,
        "page": page
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}

async def apollo_update_contact_stages(
    contact_ids=None,
    contact_stage_id=None
):
    url = "https://api.apollo.io/api/v1/contacts/update_stages"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "contact_ids[]": contact_ids,
        "contact_stage_id": contact_stage_id
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}


async def apollo_update_contact_owners(
    contact_ids=None,
    owner_id=None
):
    url = "https://api.apollo.io/api/v1/contacts/update_owners"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "contact_ids[]": contact_ids,
        "owner_id": owner_id
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params)
            return response.text
    except Exception as e:
        return {"error": str(e)}

async def apollo_list_contact_stages():
    url = "https://api.apollo.io/api/v1/contact_stages"
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.text
    except Exception as e:
        return {"error": str(e)}
