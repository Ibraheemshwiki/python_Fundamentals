from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' 
    
@app.route('/dojo')       
def hello_dojo():
    return 'Dojo' 
    
@app.route('/say/flask')       
def hello_flask():
    return 'Hi Flask!' 
    
@app.route('/say/<name1>')       
def hello_name(name1):
    return f'Hi {name1}' 

@app.route('/repeat/<num>/<name2>')       
def hello_num(num,name2):
    return f'{name2}'*int(num) 

@app.route('/<name>')       
def hello_stranger(name):
    return "sorry Get the HELL OUTTA HERE"


if __name__=="__main__":       
    app.run(debug=True)    
