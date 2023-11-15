import requests


API_ID = ''
API_KEY = ''
ENVIRONMENT_TEMPLATE_ID = ''


if __name__ == '__main__':
    session = requests.session()
    session.auth = requests.auth.HTTPBasicAuth(
        username=API_ID,
        password=API_KEY,
    )
    response = session.post(
        url=f'https://api.env0.com/environments/{ENVIRONMENT_TEMPLATE_ID}/destroy', 
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
                  