import sys, os

# change path to parent directory to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from steerclear import db
from steerclear.models import User, Role
from sqlalchemy import exc

def create_user():
	# prompt for input
	email = raw_input('Enter email: ')
	password = raw_input('Enter Password: ')
	phone = raw_input('Enter Phone Number (e.x. +1xxxyyyzzzz): ')
	
	student_role = Role.query.filter_by(name='student').first()
	if student_role is None:
		print "Error: student Role does not exist. Start app once and make request"
		sys.exit(1)

	# create user
	user = User(email=email, password=password, phone=phone, roles=[student_role])
	try:
		# attempt to add user to db
		db.session.add(user)
		db.session.commit()
		print "User created successfully"
	except exc.IntegrityError:
		print "User already exists"

if __name__ == '__main__':
	create_user()