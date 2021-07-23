from flask import Flask
from flask_classful import FlaskView, route

app = Flask(__name__)

class AppRouting(FlaskView):
	route_base = '/'

	def __init__(self):
		print("--------constructor---------")
		return 

	def test1(self):
		return "test1"

	def test2(self):	
		return "test2"

	def test3(self):
		return "test3"

	def test4(self):
		return "test4"

	def test5(self):
		return "test5"


if __name__ == '__main__':
	AppRouting.register(app)
	app.run()