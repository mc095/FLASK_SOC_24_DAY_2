from flask import Flask

# Creating the flask class object
app = Flask(__name__)

@app.route('/CSE')
def CSE():
    return """
        <html>
            <head>
                <title>Branches List</title>
                <style>
                    * {
                        background-color: azure;
                    }
                    h1, h3 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1><u>This is CSE Homepage</u></h1>
            </body>
        </html>
    """;
    

@app.route('/ECE')
def ECE():
    return """
        <html>
            <head>
                <title>Branches List</title>
                <style>
                    * {
                        background-color: azure;
                    }
                    h1, h3 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1><u>This is ECE Homepage</u></h1>
            </body>
        </html>
    """;
    

@app.route('/CST')
def CST():
    return """
        <html>
            <head>
                <title>Branches List</title>
                <style>
                    * {
                        background-color: azure;
                    }
                    h1, h3 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1><u>This is CST Homepage</u></h1>
            </body>
        </html>
    """;

@app.route('/CAI')
def CAI():
    return """
        <html>
            <head>
                <title>Branches List</title>
                <style>
                    * {
                        background-color: azure;
                    }
                    h1, h3 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1><u>This is CAI Homepage</u></h1>
            </body>
        </html>
    """;
    
@app.route('/CIVIL')
def CIVIL():
    return """
        <html>
            <head>
                <title>Branches List</title>
                <style>
                    * {
                        background-color: azure;
                    }
                    h1, h3 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1><u>This is CIVIL Homepage</u></h1>
            </body>
        </html>
    """;
    
# Decorator defines the url of the web page
@app.route('/home')
def home():
    # stmt = "Welcome to your first flask website"
    # return stmt
    
    return """
        <html>
            <head>
                <title>Branches List</title>
                <style>
                    * {
                        background-color: azure;
                    }
                    h1, h3 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1><u>Sri Vasavi Engineering College</u></h1>
                <hr>
                <h3><u>List of Departments</u></h3>
                <hr>
                <ul>
                    <li><a href='/CSE'>CSE</a></li>
                    <li><a href='/CST'>CST</a></li>
                    <li><a href='/CAI'>CAI</a></li>
                    <li><a href='/ECE'>ECE</a></li>
                    <li><a href='/CIVIL'>CIVIL</a></li>
                    </ul>
            </body>
        </html>
    """; 

if __name__ == '__main__':
    app.run(debug = True, port=8000)