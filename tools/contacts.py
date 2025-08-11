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
    """
    Create a new contact in Apollo.

    This function calls the Create a Contact endpoint to add a person explicitly added to your team's Apollo database.

    Note:
    - Apollo does not deduplicate on create. If a contact with the same name or email exists, a new contact will be created.
    - Use the Update a Contact endpoint to modify existing contacts.
    - Requires a master API key; unauthorized calls return 403.

    Parameters:
        first_name (str, optional): Contact's first name (e.g., "Tim").
        last_name (str, optional): Contact's last name (e.g., "Zheng").
        organization_name (str, optional): Contact's current employer name (e.g., "apollo").
        title (str, optional): Contact's current job title (e.g., "senior research analyst").
        account_id (str, optional): Apollo account ID to assign the contact.
        email (str, optional): Contact's email address.
        website_url (str, optional): Corporate website URL (full URL, no social links).
        label_names (list[str], optional): Lists to add the contact to; auto-creates new lists if needed.
        contact_stage_id (str, optional): Apollo ID for the contact stage to assign.
        present_raw_address (str, optional): Contact's personal location (city, state, country).
        direct_phone (str, optional): Primary phone number (any format).
        corporate_phone (str, optional): Work/office phone number.
        mobile_phone (str, optional): Mobile phone number.
        home_phone (str, optional): Home phone number.
        other_phone (str, optional): Alternative or unknown type phone number.

    Returns:
        Response text from Apollo API or error details.
    """
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
    """
    Update an existing contact in Apollo.

    This function calls the Update a Contact endpoint to modify contact details in your team's Apollo database.

    Note:
    - Use the Create a Contact endpoint to add new contacts.
    - Use the Update Contact Stage for Multiple Contacts endpoint to update stages in bulk.
    - Requires a master API key; unauthorized calls return 403.

    Parameters:
        contact_id (str): Apollo ID of the contact to update (required).
        first_name (str, optional): Updated first name.
        last_name (str, optional): Updated last name.
        organization_name (str, optional): Updated employer name.
        title (str, optional): Updated job title.
        account_id (str, optional): Updated Apollo account ID.
        email (str, optional): Updated email address.
        website_url (str, optional): Updated corporate website URL (full URL).
        label_names (list[str], optional): Lists the contact belongs to (replaces existing lists).
        contact_stage_id (str, optional): Updated contact stage ID.
        present_raw_address (str, optional): Updated personal location (city, state, country).
        direct_phone (str, optional): Updated primary phone number.
        corporate_phone (str, optional): Updated work/office phone number.
        mobile_phone (str, optional): Updated mobile phone number.
        home_phone (str, optional): Updated home phone number.
        other_phone (str, optional): Updated alternative or unknown phone number.

    Returns:
        Response text from Apollo API or error details.
    """

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
    """
    Search for contacts in your team's Apollo account.

    Calls the Search for Contacts endpoint to find contacts explicitly added to your Apollo database.

    Notes:
    - Returns only contacts, not general people in Apollo's database.
    - Limited to 50,000 records (100 per page, max 500 pages).
    - Not available on free Apollo plans.
    - Use filters to narrow down results.
    - Requires a master API key; unauthorized calls return 403.

    Parameters:
        q_keywords (str, optional): Keywords to search contact names, titles, companies, or emails.
        contact_stage_ids (list[str], optional): Filter by one or more contact stage IDs.
        sort_by_field (str, optional): Field to sort results by. Options:
            - contact_last_activity_date
            - contact_email_last_opened_at
            - contact_email_last_clicked_at
            - contact_created_at
            - contact_updated_at
        sort_ascending (bool, optional): True for ascending order (requires sort_by_field).
        per_page (int, optional): Number of results per page.
        page (int, optional): Page number of results to retrieve.

    Returns:
        Response text from Apollo API or error details.
    """

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
    """
    Update the contact stage for multiple contacts in your team's Apollo account.

    Calls the Update Contact Stage for Multiple Contacts endpoint to batch update contact stages.

    Notes:
    - Only updates contact stages.
    - To update other contact details, use the Update a Contact endpoint.
    - Requires a master API key; unauthorized calls return 403.

    Parameters:
        contact_ids (list[str]): List of Apollo contact IDs to update.
        contact_stage_id (str): Apollo ID of the contact stage to assign.

    Returns:
        Response text from Apollo API or error details.
    """

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
    """
    Assign multiple contacts to a different owner in your team's Apollo account.

    Calls the Update Contact Owner for Multiple Contacts endpoint to batch update contact owners.

    Notes:
    - Only updates contact ownership.
    - To update other contact details, use the Update a Contact endpoint.
    - Requires a master API key; unauthorized calls return 403.

    Parameters:
        contact_ids (list[str]): List of Apollo contact IDs to update.
        owner_id (str): Apollo user ID to assign as the new owner.

    Returns:
        Response text from Apollo API or error details.
    """

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
    """
    Retrieve all available contact stage IDs in your team's Apollo account.

    Calls the List Contact Stages endpoint.

    Notes:
    - Contact stage IDs are used to update individual contacts or multiple contacts' stages.
    - Requires a master API key; unauthorized calls return 403.

    Returns:
        Response text containing contact stage IDs and details.
    """

    url = "https://api.apollo.io/api/v1/contact_stages"
    headers = get_apollo_client()  # Needs master API key

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.text
    except Exception as e:
        return {"error": str(e)}
