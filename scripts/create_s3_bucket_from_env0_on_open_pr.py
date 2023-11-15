import requests


API_ID = ''
API_KEY = ''
ENVIRONMENT_TEMPLATE_ID = '-2cb1-49d2-932a-0538f37d00ad'


if __name__ == '__main__':
    session = requests.session()
    session.auth = requests.auth.HTTPBasicAuth(
        username=API_ID,
        password=API_KEY,
    )
    response = session.post(
        url=f'https://api.env0.com/environments/{ENVIRONMENT_TEMPLATE_ID}/deployments', 
        json={
            'configurationChanges': {
                'type': 0,
                'name': 'kosta',
            },
            'ttl': {
                'type': 'INFINITE',
            },
            'deploymentType': 'deploy'
        }, 
        headers={
            'accept': 'application/json',
            'content-type': 'application/json',
        },
    )
    
    print(response.text)
                  