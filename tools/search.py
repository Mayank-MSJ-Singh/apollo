import httpx
from .base import get_apollo_client

async def apollo_organization_job_postings(
    organization_id: str,
    page: int = None,
    per_page: int = None
):
    url = f'https://api.apollo.io/api/v1/organizations/{organization_id}/job_postings'
    params = {
        'page': page,
        'per_page': per_page
    }
    headers = get_apollo_client()
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


async def apollo_news_articles_search(
    organization_ids: list,
    categories: list = None,
    published_at_min: str = None,
    published_at_max: str = None,
    page: int = None,
    per_page: int = None
):
    url = 'https://api.apollo.io/api/v1/news_articles/search'
    params = {
        'organization_ids[]': organization_ids,
        'categories[]': categories,
        'published_at[min]': published_at_min,
        'published_at[max]': published_at_max,
        'page': page,
        'per_page': per_page
    }
    headers = get_apollo_client()
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

if __name__ == "__main__":
    #print(apollo_organization_job_postings('5e66b6381e05b4008c8331b8', per_page=10))
    pass