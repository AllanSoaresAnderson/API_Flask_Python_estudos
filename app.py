from flask import Flask



server = Flask(__name__)


@server.get('/pessoas')
def get_pessoa():
    return 'Ok'


server.run()