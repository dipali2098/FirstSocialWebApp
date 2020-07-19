from flask import Flask , render_template , request , redirect , url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_info import Base, UserPersonalInfo, UserLoginInfo
from datetime import datetime
from UserHome import userHome

engine = create_engine ('sqlite:///userinformation.db' , connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/', methods = ['GET','POST'])
def home():
	# newuser1 = UserPersonalInfo( name = "Deepali", user_id = "deeps", dob = datetime.datetime(1998, 10, 20), gender = "Female", email = "dips@gm.com", mobno = "8871666808", passwrd = "12345")
	# session.add(newuser1)
	# session.commit()
	# output = ""
	# users = session.query(UserPersonalInfo)
	# for user in users:
	# 	output+= "<p>%s</p><br>" %user.passwrd
	# return output
	if request.method == 'POST':
		try:
			user = session.query(UserLoginInfo).filter_by(user_id = request.form['userid1']).one()

			if user :
				if user.password == request.form['userpassword1']:
					return redirect(url_for('userHomeCLL', user_id = request.form['userid1']))
				else:
					flash("Invalid password")
					return redirect(url_for('home'))
			else:
				flash("User not found!")
				return redirect(url_for('home'))
		except:
			flash("User not found!")
			return redirect(url_for('home'))
		# user = session.query(UserLoginInfo).filter_by(user_id = request.form['userid1']).one()

		# if user :
		# 	if user.password == request.form['userpassword1']:
		# 		return redirect(url_for('userHomeCall', user_id = request.form['userid1'])) #userHome(request.form['userid1']) #
		# 	else:
		# 		flash("Invalid password")
		# 		return redirect(url_for('home'))
		# else:
		# 	flash("User not found!")
		# 	return redirect(url_for('home'))
			
	else:
		return render_template('login.html')

# @app.route('/SignIn' , methods = ['GET','POST'])
# def login():
# 	if request.method == 'POST':
# 		user = session.query(UserPersonalInfo).filter_by(user_id = request.form['userid1']).one()
# 		if user == null:
# 			flash("User not found!")
# 		else:
# 			if user.password == request.form['userpassword1']:
# 				return redirect(url_for('newUser'))
# 			else:
# 				flash("Invalid password")
# 	else:
# 		return render_template('login.html')

@app.route('/newaccount', methods = ['GET','POST'])
def newUser():
	if request.method == 'POST':
		newuser = UserPersonalInfo( name = request.form['username'], user_id = request.form['userid'], dob = datetime.strptime(request.form['userdob'],'%Y-%m-%d'), gender = request.form['usergender'], email = request.form['useremail'], mobno = request.form['usermobno'])
		session.add(newuser)
		session.commit()
		newuser = UserLoginInfo( user_id = request.form['userid'], password = request.form['userpassword'])
		session.add(newuser)
		session.commit()
		flash("User successully added!")
		return redirect(url_for('home'))
	else:
		return render_template('newuser.html')

@app.route('/<string:user_id>', methods = ['GET','POST'])
def userHomeCall(user_id):
	return userHome(user_id)



if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5001)