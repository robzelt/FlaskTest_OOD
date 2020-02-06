from flask import Flask, session, render_template, request
import os



#import session

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
    sessionheaders = dict(request.headers)
    sessioni = request.headers['X-Forwarded-User']
    sessiono = os.environ['USERNAME']
    
    return render_template('index.html', sessions = sessioni)

if __name__ == "__main__":
	MyApp.run()
