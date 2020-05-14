from flask import Flask

from src.people.views import people_api
from src.hello.views import hello_api

app = Flask(__name__)

app.register_blueprint(people_api)
app.register_blueprint(hello_api)

@app.route('/')
def getPeople():
    return 'Home'