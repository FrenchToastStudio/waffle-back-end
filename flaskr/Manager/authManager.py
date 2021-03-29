from flaskr.Store.userStore import userStore
from flaskr.answer import answer
from flaskr.JWTKey import JWTKey
class authManager:

    def register(email, password):
        error = None
        if email is None:
            error = 'No username Sent'
        elif password is None:
            error = 'No email Sent'

        if error is None:
            if userStore.create(email, password):
                return answer.succes('Account created')
            return answer.fail('Account has not been created')
        return answer.fail(error)

    def login (email, password):
        error = None
        if email is None:
            error = 'No username Sent'
        elif password is None:
            error = 'No email Sent'

        if error is None:
            user = userStore.findByLoginInfo(email, password)

            if isinstance(user, str):
                return return answer.fail(user)
            elif user is None:
                return answer.fail('Incorrect username OR password.')

            key = JWTKey.EncodeJWTToken(user["Id"])
            return answer.succes(key)
        return answer.fail(error)
