from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/student')
def student():
    return """
            <html>
                <h3 style="color: violet; text-align: center">This is Student page</h3>
            </html>
    """;
    
@app.route('/admin')
def admin():
    return """
            <html>
                <h3 style="color: pink; text-align: center">This is admin page</h3>
            </html>
    """;
    
@app.route('/librarian')
def librarian():
    return """
            <html>
                <h3 style="color: red; text-align: center">This is librarian page</h3>
            </html>
    """;
    
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'librarian':
        return redirect(url_for('librarian'))
    if name == 'student':
        return redirect(url_for('student'))

if __name__ == '__main__':
    app.run(debug=True)