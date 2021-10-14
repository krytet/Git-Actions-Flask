from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'У меня получилось!'


@app.route('/seconds')
def hello_people():
    return 'Здесь так же все работает!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')