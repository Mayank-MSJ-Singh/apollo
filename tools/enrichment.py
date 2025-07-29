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

def apollo_bulk_organisation_enrichment(domains: list):
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

    response = requests.post(url, headers=headers, params=params)
    return response.text


if __name__ == '__main__':
    #print(apollo_organisation_enrichment("www.apollo.io"))
    #lists = ["www.apollo.io", "wikihow.com"]
    #print(apollo_bulk_organisation_enrichment(lists))
    pass