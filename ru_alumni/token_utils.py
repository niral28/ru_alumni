# project/token.py

from itsdangerous import URLSafeTimedSerializer

from ru_alumni import application


def generate_token(obj):
    serializer = URLSafeTimedSerializer(application.config['TOKEN_SECRET_KEY'])
    return serializer.dumps(obj, salt=application.config['TOKEN_SALT'])


def confirm_token(token):
    serializer = URLSafeTimedSerializer(application.config['TOKEN_SECRET_KEY'])
    try:
        obj = serializer.loads(
            token,
            salt=application.config['TOKEN_SALT'],
            max_age=application.config['TOKEN_EXPIRATION']
        )
    except Exception as e:
        # TODO: Add better exception handling
        raise e

    return obj
