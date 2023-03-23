import requests

baseURL = 'http://localhost:8080/'

headers = {
    'Content-Type': 'application/json'
}

if __name__ == "__main__":
    authURL = baseURL + 'auth'
    
    authPayload = {
        'username': 'temporary_user',
        'password': 'default_password'
    }

    try:
        response = requests.post(url=authURL, headers=headers, json=authPayload)
    except Exception as e:
        print(e)
    else:
        # status_code = response.status_code
        access_token = response.json()['access_token']
        print(access_token)

    chatURL = baseURL + 'chatgpt'
    headers['Authorization'] = 'JWT' + ' ' + access_token
    chatPayload = {
        'question': 'who are you?'
    }

    try:
        response = requests.post(url=chatURL, headers=headers, json=chatPayload, stream=True)
    except Exception as e:
        print(e)
    else:
        str = ""
        for line in response.iter_lines():
            message = line.decode()
            if "content" in message:
                str += message[14:-1]
        print(str)