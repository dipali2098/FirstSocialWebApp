from flask import Flask , render_template , request , redirect , url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_info import Base, UserPersonalInfo, UserLoginInfo
from datetime import datetime

engine = create_engine ('sqlite:///userinformation.db' , connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/<string:user_id>')
def userHome(user_id):
	# output = user_id
	# return output
	return render_template('userhome.html', user_id = user_id)


# if __name__ == '__main__':
# 	app.secret_key = 'super_secret_key2'
# 	app.debug = True
# 	app.run(host = '0.0.0.0', port = 5001)