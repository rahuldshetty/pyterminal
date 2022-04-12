import uuid
from flask import Flask
from flask_socketio import SocketIO

# Configure App
app = Flask(__name__, template_folder="templates", static_url_path="")
app.config["SECRET_KEY"] = str(uuid.uuid4())
app.config["fd"] = None
app.config['child_pid'] = None

socket_io = SocketIO(app)