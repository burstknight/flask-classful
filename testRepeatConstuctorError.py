from flask import Flask
from flask_classful import FlaskView, route
from random import randint

app = Flask(__name__)

class AppRouting(FlaskView):
	route_base = '/'

	def __init__(self):
		self.m_iData = randint(0, 9999)
		print("--------constructor: %d ---------" %(self.m_iData))
		return 

	def test1(self):
		return "test1 " + str(self.m_iData)

	def test2(self):	
		return "test2 " + str(self.m_iData)

	def test3(self):
		return "test3 " + str(self.m_iData)

	def test4(self):
		return "test4 " + str(self.m_iData)

	def test5(self):
		return "test5 " + str(self.m_iData)


if __name__ == '__main__':
	AppRouting.register(app)
	app.run()