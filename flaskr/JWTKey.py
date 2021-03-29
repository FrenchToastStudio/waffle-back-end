import datetime
import jwt
from flask import current_app

class JWTKey:
    def EncodeJWTToken(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def decodeJWTToken(cle):
        try:
            payload = jwt.decode(auth_token, config.ConfigurationBasique.get('SECRET_KEY'))
            return messapayload['sub']
        except jwt.ExpiredSignatureError:
            return 'the KEY has expired please reconnect again.'
        except jwt.InvalidTokenError:
            return 'KEY not valid, please aquire a new one.'
