from flaskr.Store.userStore import userStore
from flaskr.answer import answer
class authManager:

    def register(email, password):
        if userStore.createUser(email, password):
            return answer.succes('Account created')
        return answer.fail('Account has not been created')
