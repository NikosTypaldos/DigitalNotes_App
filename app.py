from pymongo import MongoClient, cursor
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
from bson import ObjectId
from bson.json_util import dumps
import uuid
import time

# Connect to our local MongoDB
client = MongoClient('localhost:27017')

# Choose database
db = client['InfoSys']

# Choose collection
clients = db['Clients']
notes = db['Notes']

# Intialize our Flask application
app = Flask(__name__)

client_sessions = {}


def addClientToSession(client_email):
    client_uuid = str(uuid.uuid4())
    client_sessions[client_uuid] = (client_email, time.time())
    return client_uuid


def sessionValidity(client_uuid):
    return client_uuid in client_sessions


@app.route('/')
@app.route('/createUser', methods=['POST'])
def create_user():
    data = None
    if request.method == 'POST':
        # Get the data from the POST request
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "username" in data or not "password" in data or not "email" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        # Check if the username is already in use
        if clients.find({"username": data["username"], "password": data["password"], "email": data["email"]}).count() == 1:
            return Response("username already in use", status=500, mimetype='application/json')
        else:
            # Insert the new user
            new_user = {
                'username': data['username'],
                'email': data['email'],
                'password': data['password'],
                'fullname': data['fullname'],
                "category": 'user'
            }
            clients.insert_one(new_user)
            return Response("user created", status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "username" in data or not "password" in data or not "email" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        # Check if the username is already in use
        if clients.find({"username": data["username"], "password": data["password"]}).count() == 0:
            return Response("User doesnt exist try again", status=500, mimetype='application/json')
        else:
            client1 = clients.find_one(
                {"username": data["username"], "password": data["password"], "email": data["email"]})
            if client1['password'] == data['password']:
                global client_email
                global client_category
                global notes
                global client_uuid
                global client_category
                client_email = str(data['email'])
                client_category = str(client1['category'])
                client_uuid = addClientToSession(client_email)
                client_category = str(client1['category'])
                return Response(f"Logged in. Your UserID is : {client_uuid} at {time.time()}", status=200, mimetype='application/json')
            else:
                return Response("Wrong email, password or username", status=500, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/createNote', methods=['POST'])
def createNote():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "title" in data or not "content" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # Insert the new note
            new_note = {
                'title': data['title'],
                'content': data['content'],
                'keywords': data['keywords'],
                'timestamp': time.time(),
                'clientEmail': str(client_email)
            }
            notes.insert_one(new_note)
            return Response("Note created", status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/searchNote', methods=['POST'])
def searchNoteTitle():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "title" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # search for the note
            note = notes.find_one({"title": data['title']})
            if note == None:
                return Response("Note not found", status=500, mimetype='application/json')
            else:
                return Response(dumps(note), status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/searchNoteKey', methods=['POST'])
def searchNoteKey():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "keywords" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # search for the note
            note = []
            note = notes.find({"keywords": data['keywords']})
            if note == None:
                return Response("Note not found", status=500, mimetype='application/json')
            else:
                return Response(dumps(note), status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/updateNote', methods=['POST'])
def updateNote():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "title" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # Update the note
            note = notes.find_one({"title": data['title']})
            if note == None:
                return Response("Note not found", status=500, mimetype='application/json')
            else:
                note['content'] = data['content']
                note['keywords'] = data['keywords']
                note['timestamp'] = time.time()
                notes.replace_one({"title": data['title']}, note)
                return Response("Note updated", status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/deleteNote', methods=['POST'])
def deleteNote():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "title" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # Delete the note
            note = notes.find_one({"title": data['title']})
            if note == None:
                return Response("Note not found", status=500, mimetype='application/json')
            else:
                notes.delete_one({"title": data['title']})
                return Response("Note deleted", status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/deleteAccount', methods=['POST'])
def deleteAccount():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "email" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # Delete the account
            if data['email'] == client_email:
                clients.delete_one({"email": data["email"]})
                notes.delete_many({'clientEmail': str(client_email)})
                return Response("Account deleted", status=200, mimetype='application/json')
            else:
                return Response("Wrong password", status=500, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/showNotesTime', methods=['POST'])
def showNotesChronological():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "order" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # Show the notes in chronological order
            if data['order'] == "asc":
                note = notes.find({"clientEmail": str(client_email)})
                note = sorted(note, key=lambda k: k['timestamp'])
                return Response(dumps(note), status=200, mimetype='application/json')
            elif data['order'] == "desc":
                note = notes.find({"clientEmail": str(client_email)})
                note = sorted(note, key=lambda k: k['timestamp'], reverse=True)
                return Response(dumps(note), status=200, mimetype='application/json')
            else:
                return Response("bad request", status=500, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


@app.route('/createAdmin', methods=['POST'])
def createAdmin():
    data = None
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    try:
        data = request.get_json()
    except Exception as e:
        return Response("bad json content", status=500, mimetype='application/json')
    
    #chek one time password
    if "otp" in data and data['otp']=="123456":
        if request.method == 'POST':
            # Get the data from the POST request
           
            if data == None:
                return Response("bad request", status=500, mimetype='application/json')
            if not "username" in data or not "password" in data or not "email" in data:
                return Response("Information incomplete", status=500, mimetype='application/json')
            else:
                # Create the user
                user = clients.find_one({"username": data['username']})
                if user != None:
                    return Response("User already exists", status=500, mimetype='application/json')
                else:
                    user = clients.find_one({"email": data['email']})
                    if user != None:
                        return Response("Email already exists", status=500, mimetype='application/json')
                    else:
                        clients.insert_one({'username': data['username'],
                                            'email': data['email'],
                                            'password': data['password'],
                                            'fullname': data['fullname'], "category": "admin"})
                        return Response("Admin created", status=200, mimetype='application/json')
    else:
        return Response("invalid one time password", status=500, mimetype='application/json')

@app.route('/deleteAdmin', methods=['POST'])
def deleteAdmin():
    if (sessionValidity(client_uuid)) == False:
        return Response("Information incomplete", status=401, mimetype="application/json")

    if(client_category != "admin"):
        return Response("You are not an admin", status=401, mimetype="application/json")

    if request.method == 'POST':
        # Get the data from the POST request
        data = None
        try:
            data = request.get_json()
        except Exception as e:
            return Response("bad json content", status=500, mimetype='application/json')
        if data == None:
            return Response("bad request", status=500, mimetype='application/json')
        if not "username" in data:
            return Response("Information incomplete", status=500, mimetype='application/json')
        else:
            # Delete the user
            user = clients.find_one({"username": data['username']})
            if user == None:
                return Response("User not found", status=500, mimetype='application/json')
            else:
                clients.delete_one({"username": data['username']})
                return Response("Admin deleted", status=200, mimetype='application/json')
    else:
        return Response("bad request", status=500, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
