from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi "+ name

@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    
    return "{} ".format(name) * int(num)

if __name__=="__main__":
    app.run(debug=True)
