from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
sio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')


@app.route('/')
def hello_world():
    return render_template('index.html')


@sio.on('List ready')
def colors(msg):
    print(msg)
    sio.emit('List ready', 'List ready')


if __name__ == '__main__':
    sio.run(app, host='192.168.1.7', port='6543', debug=True)
