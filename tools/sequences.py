import httpx
from base import get_apollo_client

async def apollo_search_sequences(
    q_name: str = None,
    page: int = None,
    per_page: int = None
):
    url = "https://api.apollo.io/api/v1/emailer_campaigns/search"
    params = {
        "q_name": q_name,
        "page": page,
        "per_page": per_page
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

async def apollo_add_contacts_to_sequence(
    sequence_id: str,
    emailer_campaign_id: str,
    contact_ids: list,
    send_email_from_email_account_id: str,
    sequence_no_email: bool = False,
    sequence_unverified_email: bool = False,
    sequence_job_change: bool = False,
    sequence_active_in_other_campaigns: bool = False,
    sequence_finished_in_other_campaigns: bool = False,
    user_id: str = None
):
    url = f"https://api.apollo.io/api/v1/emailer_campaigns/{sequence_id}/add_contact_ids"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "emailer_campaign_id": emailer_campaign_id,
        "contact_ids[]": contact_ids,
        "send_email_from_email_account_id": send_email_from_email_account_id,
        "sequence_no_email": sequence_no_email,
        "sequence_unverified_email": sequence_unverified_email,
        "sequence_job_change": sequence_job_change,
        "sequence_active_in_other_campaigns": sequence_active_in_other_campaigns,
        "sequence_finished_in_other_campaigns": sequence_finished_in_other_campaigns,
    }

    if user_id:
        params["user_id"] = user_id

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


async def apollo_update_contact_status_in_sequence(
    emailer_campaign_ids: list,
    contact_ids: list,
    mode: str
):
    url = "https://api.apollo.io/api/v1/emailer_campaigns/remove_or_stop_contact_ids"
    headers = get_apollo_client()  # Needs master API key

    params = {
        "emailer_campaign_ids[]": emailer_campaign_ids,
        "contact_ids[]": contact_ids,
        "mode": mode  # must be 'mark_as_finished', 'remove', or 'stop'
    }

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

async def apollo_search_outreach_emails(
    emailer_message_stats: list = None,
    emailer_message_reply_classes: list = None,
    user_ids: list = None,
    email_account_id_and_aliases: str = None,
    emailer_campaign_ids: list = None,
    not_emailer_campaign_ids: list = None,
    emailer_message_date_range_mode: str = None,
    emailerMessageDateRange_max: str = None,
    emailerMessageDateRange_min: str = None,
    not_sent_reason_cds: list = None,
    q_keywords: str = None,
    page: int = None,
    per_page: int = None
):
    url = "https://api.apollo.io/api/v1/emailer_messages/search"
    params = {
        "emailer_message_stats[]": emailer_message_stats,
        "emailer_message_reply_classes[]": emailer_message_reply_classes,
        "user_ids[]": user_ids,
        "email_account_id_and_aliases": email_account_id_and_aliases,
        "emailer_campaign_ids[]": emailer_campaign_ids,
        "not_emailer_campaign_ids[]": not_emailer_campaign_ids,
        "emailer_message_date_range_mode": emailer_message_date_range_mode,
        "emailerMessageDateRange[max]": emailerMessageDateRange_max,
        "emailerMessageDateRange[min]": emailerMessageDateRange_min,
        "not_sent_reason_cds[]": not_sent_reason_cds,
        "q_keywords": q_keywords,
        "page": page,
        "per_page": per_page,
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

async def apollo_check_email_stats(email_id: str):
    url = f"https://api.apollo.io/api/v1/emailer_messages/{email_id}/activities"
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
