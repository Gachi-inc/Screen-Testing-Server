from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development key'
socket = SocketIO(
    app, cors_allowed_origins="*", engineio_logger=True, asunc_mode='eventlet'
)
CORS(app)


@app.route('/api/screenshots', methods=['GET', 'POST'])
def hello_world():
    request_data = request.get_json()
    url = request_data['url']
    return ""


# @app.route('/screenshots', methods=['GET', 'POST'])
# def parse_request():
#     if request.method == 'POST':
#         first = request.form.get('first')
#         second = request.form.get('second')
#         return '''
#                     <h1>The language value is: {}</h1>
#                     <h1>The framework value is: {}</h1>'''.format(first, second)
#     return '''
#            <form method="POST">
#                <div><label>Language: <input type="text" name="language"></label></div>
#                <div><label>Framework: <input type="text" name="framework"></label></div>
#                <input type="submit" value="Submit">
#            </form>'''

@socket.on('message')
def handle_message(data):
    print(data)
    print(request)
    socket.emit('List3', data)


@socket.on('List2')
def colors(msg):
    print(msg)
    socket.send(msg)
    socket.emit('List3', msg)


if __name__ == '__main__':
    socket.run(app, host='192.168.1.7', port='6543', debug=True)