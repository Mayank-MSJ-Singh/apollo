import requests
from base import get_apollo_client

def apollo_organization_job_postings(
organization_id:str,
page:int = None,
per_page:int = None
):
    url = f'https://api.apollo.io/api/v1/organizations/{organization_id}/job_postings'
    params = {
        'page' : page,
        'per_page' : per_page
    }
    headers = get_apollo_client()
    response = requests.get(url, headers=headers, params=params)
    return (response.text)

if __name__ == "__main__":
    #print(apollo_organization_job_postings('5e66b6381e05b4008c8331b8', per_page=10))