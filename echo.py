from flask import Flask, render_template, request

flask_app = Flask(__name__)

@flask_app.route('/', methods = ['GET'])
def root():
	return render_template('template.html')

@flask_app.route('/response/', methods = ['POST'])
def response():
	return render_template('response.html', name=request.form['username'])

if __name__ == '__main__':
#    flask_app.debug = True
    flask_app.run()
