from flaskr.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash
class userStore:


    def create(email, password):
        error = None
        db = get_db()
        print(generate_password_hash(password))
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


    def findByLoginInfo(email, password):
        error = None
        db = get_db()
        user = db.execute(
            'SELECT * FROM Users WHERE Email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email OR password.'
        elif not check_password_hash(user['password'], password) :
            error = 'Incorrect password.'

        if error is None:
            return user
        flash(error)
