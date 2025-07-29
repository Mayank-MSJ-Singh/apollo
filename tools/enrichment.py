import requests
from base import get_apollo_client


def apollo_organisation_enrichment(domain:str):
    url = "https://api.apollo.io/api/v1/organizations/enrich"
    parts = domain.split(".")
    if parts[0] == "www":
        domain = ".".join(parts[1:])
    params = {"domain":domain}
    headers = get_apollo_client()
    response = requests.get(url, headers=headers, params=params)
    return (response.text)

if __name__ == '__main__':
    print(apollo_organisation_enrichment("www.apollo.io"))