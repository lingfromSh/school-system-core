from jwcrypto.jwk import JWK
from jwcrypto.jwt import JWT


JWK_RSA_KEY = JWK(generate="RSA", size=512)


def encode_jwt(header=None, payload=None, claims=None, exp=5*3600):
    header = header if header else {'alg': 'RSA-OAEP-256'}
    claims = claims if claims else {'exp': exp}
    jwt = JWT(header=header,
              claims=claims)
    jwt.make_encrypted_token(JWK_RSA_KEY)
    return jwt.serialize()


def verify_jwt(jwt):
    pass


print(encode_jwt())
