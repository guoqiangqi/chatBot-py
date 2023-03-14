import jwt
import datetime
from user_manager import *

# Note: sercret keys are prohibited from being hard-coded.
# TODO: optimize the implementation here according to your needs.
secret_key = "your_secret_key"

def createTokenForUser(userID):
    userMatch = indexUserWithID(userID)
    if not userMatch:
        return None

    use = userMatch[0]
    expires_in = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    payload = {
        'user_id': user.id,
        'user_name': user.name,
        'expir': expir
    }

    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')

    return jwt_token

def validate_jwt(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        userID = payload.get('user_id')
        userName = payload.get('user_name')
        expirTime = payload.get('expir')
        if not user_id or not userName or not expirTime:
            return False

        # TODO: Do more checks here, such as access/permission.

        return True
    except:
        return False
