from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
import deletefile

application = Flask(__name__)

@application.route('/')
def show_html():
    htmlfile = open("index.html")
    return (htmlfile.read())

@application.route('/delete_file')
def delete_file():
    deletefile.application()
    return 'ok'

@application.route('/calibrate_well')
def calibrate_well():
	requestCalibration.application(1)
	return

application.wsgi_app = ProxyFix(application.wsgi_app)

if __name__ == '__main__':
    application.run()
