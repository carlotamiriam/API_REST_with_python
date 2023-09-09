from flask import Flask

app = Flask(__name__) #The argument name is used to indicate that this Flask application is the main program.

@app.route('/saludo', methods=['GET'])
def saludar(): #Defines the saludar() function, which will be executed when a GET request is made to the path '/greeting'.
    return 'Hola, mundo!'
if __name__ == '__main__':  #This is a conditional check that verifies if the script is being executed as the main program.
    app.run(debug=True)
