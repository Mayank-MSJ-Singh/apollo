import httpx
from base import get_apollo_client


async def apollo_organisation_enrichment(domain: str):
    url = "https://api.apollo.io/api/v1/organizations/enrich"
    parts = domain.split(".")
    if parts[0] == "www":
        domain = ".".join(parts[1:])
    params = {"domain": domain}
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


async def apollo_bulk_organisation_enrichment(domains: list):
    url = "https://api.apollo.io/api/v1/organizations/bulk_enrich"

    # remove 'www'------------------
    new_domains = []
    for d in domains:
        parts = d.split(".")
        if parts[0] == "www":
            new_domains.append(".".join(parts[1:]))
        else:
            new_domains.append(d)
    #-------------------------------

    headers = get_apollo_client()
    params = {"domains[]": new_domains}

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


if __name__ == '__main__':
    #print(apollo_organisation_enrichment("www.apollo.io"))
    #lists = ["www.apollo.io", "wikihow.com"]
    #print(apollo_bulk_organisation_enrichment(lists))
    pass