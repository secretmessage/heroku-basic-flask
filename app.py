from flask import Flask
import sys
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    
    version_string = sys.version

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    
    <p>
        I am on {version-string}.
    </p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

