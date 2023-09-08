from flask import Flask

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludar():
    return 'Hola, mundo!'
if __name__ == '__main__':
    app.run(debug=True)
