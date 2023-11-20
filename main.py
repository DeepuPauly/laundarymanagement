from flask import *
from admin import adminn
from public import publicc
from user import userr
from shop import shopp
from staff import stafff


app=Flask(__name__)
app.secret_key='hlo'
app.register_blueprint(publicc)
app.register_blueprint(adminn)
app.register_blueprint(userr)
app.register_blueprint(shopp)
app.register_blueprint(stafff)
app.run(debug=True,port=5008)