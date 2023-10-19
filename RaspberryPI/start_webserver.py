from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, HTTPS!'

if __name__ == '__main__':
    app.run(host='localhost', port=443, ssl_context=('certs/server-cert.pem', 'certs/server-key.pem'))
