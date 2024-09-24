from flask import Flask

app = Flask(__name__)

@app.route('/home/<name>')
def home(name):
    return f"Hello, {name}!";

@app.route('/home/<int:age>')
def age(age):
    return f"Your age is {age}!";

@app.route('/home/<name>/<int:age>')
def student(name, age):
    return f"Hello {name}, your age is {age}!";

@app.route('/home/<name>/<int:age>/<section>')
def students_details(name, age, section):
    return f"Hello {name}, your age is {age} and you belong to {section}";

if __name__ == '__main__':
    app.run(debug=True)