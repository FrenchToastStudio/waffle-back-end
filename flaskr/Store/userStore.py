from flaskr.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

class userStore:


    def createUser(email, password):
        error = None
        db = get_db()
        if db.execute(
            'SELECT id FROM Users WHERE Email = ?', (email,)
        ).fetchone() is not None:
            error = 'Email {} is already registered.'.format(email)
        if error is None:
            db.execute(
                    'INSERT INTO Users (Email, Password) VALUES (?, ?)',
                    (email, generate_password_hash(password))
                    )
            db.commit()
            return True
        return False
