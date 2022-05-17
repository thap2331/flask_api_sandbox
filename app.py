import os
from flask import Flask, render_template, request, jsonify, redirect
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import dotenv_values

db = SQLAlchemy()

app = Flask(__name__)
CORS(app)

#Config my database
configs = dotenv_values('.env')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'my_precious')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+configs['mysql_user']+":"+configs['mysql_password']+"@"+configs['mysql_host']+"/"+configs['mysql_db']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
ma = Marshmallow(app)

@app.route('/home')
def home_route_redirect():
    from server.models import Users, UsersSchema
    one_user = Users.query.first()
    user_schema = UsersSchema()
    output = user_schema.dump(one_user)
    return jsonify({"user": output})

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from server.models import Users
    return Users.query.get(int(user_id))

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from main import main as main_blueprint
app.register_blueprint(main_blueprint)

from endpoints.data_endpoints import endpoint as endpoint_blueprint
app.register_blueprint(endpoint_blueprint)


if __name__ == "__main__":
    app.run(debug=True)