from flask import Flask, request
from flask_cors import CORS
from .endpoint import Information, SignUp, Login, GetUser, AddTopics, GetCity, CreateRoom, SearchRoomsByPrefecture
from .handler import Handler
from .config import Model, ENGINE, session

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False
CORS(app)
handler = Handler()
VERSION = 1.0

def run(host, port):
    Model.metadata.create_all(bind=ENGINE)
    app.run(host=host, port=port)

@app.route('/information', methods=Information.http_method())
def getInfo():
    return handler.handle_information()

@app.route('/signup', methods=SignUp.http_method())
def signup():
    return handler.handle_signup(request.json)

@app.route('/login', methods=Login.http_method())
def login():
    return handler.handle_login(request.json)

@app.route('/get_user', methods=GetUser.http_method())
def get_user():
    return handler.handle_get_user(request.json)

@app.route('/add_topics', methods=AddTopics.http_method())
def add_topics():
    return handler.handle_add_topics(request.json)

@app.route('/get_city', methods=GetCity.http_method())
def get_city():
    return handler.handle_get_city(request.json)

@app.route('/create_room', methods=CreateRoom.http_method())
def create_room():
    return handler.handle_create_room(request.json)

@app.route('/search_rooms_by_prefecture', methods=SearchRoomsByPrefecture.http_method())
def search_rooms_by_prefecture():
    return handler.handle_search_rooms_by_prefecture(request.json)

@app.errorhandler(404)
def not_found(error):
    return handler.handle_404()

@app.teardown_appcontext
def session_clear(exception):
    if exception and session.is_active:
        session.rollback()
    else:
        pass
    session.close()
