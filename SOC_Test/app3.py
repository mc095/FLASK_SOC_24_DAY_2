from flask import Flask, render_template
app = Flask(__name__)

@app.route('/demo')
def message():
    return render_template('file1.html')

if __name__ == '__main__':
    app.run(debug=True)