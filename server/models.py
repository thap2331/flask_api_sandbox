from datetime import datetime, timedelta
from flask_login import UserMixin
from app import db, ma, configs
import jwt

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    password_hash = db.Column(db.String(255))
    token = db.Column(db.String(200))
    admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(50))
    api_key_iat = db.Column(db.Date)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.utcnow() - timedelta(days=60),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            token =  jwt.encode(payload, configs['SECRET_KEY'], algorithm='HS256')
            return token
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_code(auth_token):
        try:
            payload = jwt.decode(auth_token, configs['SECRET_KEY'])
            return True if payload else False
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True


# class States(db.Model):
#     state = db.Column(db.String(30))
#     state_id = db.Column(db.String(2), primary_key=True)
#     legislature_name = db.Column(db.String(200))
#     upper_chamber_name = db.Column(db.String(200))
#     lower_chamber_name = db.Column(db.String(200))
#     bicameral = db.Column(db.SmallInteger)
#     lower_chamber_members = db.Column(db.SmallInteger)
#     upper_chamber_members = db.Column(db.SmallInteger)
#     statehood_date = db.Column(db.Date)

# class StatesSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = States
#         load_instance = True