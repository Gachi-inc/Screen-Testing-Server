from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
from sqlLite.BdInit import DataBase 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'
socket = SocketIO(
    app, cors_allowed_origins="*", engineio_logger=True, asunc_mode='eventlet'
)
CORS(app)
db = DataBase("sites.db")


@app.route('/api/screenshots', methods=['POST'])
def get_analise():
    request_data = request.get_json()
    # db.addSiteData(request_data)
    # socket.emit({"result" : "Change has been made"})
    return "OK"


@app.route('/api/testing', methods=['POST'])
def trace():
    request_data = request.get_json()
    url = request_data['url']
    # result = db.addURLData(request_data)
    # Обработка
    #  socket.emit('List3', data)
    #print(result)
    return "ss"

@socket.on('message')
def handle_message(data):
    print(data)
    print(request)
    socket.emit('List3', data)


# @socket.on('List2')
# def colors(msg):
#     print(msg)
#     socket.send(msg)
#     socket.emit('List3', msg)


if __name__ == '__main__':
    socket.run(app, host='192.168.1.202', port='6543', debug=True)