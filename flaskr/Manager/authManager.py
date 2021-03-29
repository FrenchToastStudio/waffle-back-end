from flaskr.Store.userStore import userStore
from flaskr.answer import answer
from flaskr.JWTKey import JWTKey
class authManager:

    def register(email, password):
        if userStore.create(email, password):
            return answer.succes('Account created')
        return answer.fail('Account has not been created')

    def login (email, password):
        user = userStore.findByLoginInfo(email, password)
        if user is None:
            return answer.fail('Incorrect username OR password.')
        key = JWTKey.EncodeJWTToken(user["Id"])
        return answer.succes(key)
