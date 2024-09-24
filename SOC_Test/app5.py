from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def sports():
    return render_template('main.html')

@app.route('/cricket')
def cricket():
    return render_template('cricket.html')

@app.route('/cricket/<favname>')
def favplay(favname):
    return render_template('favplay.html', fav=favname)

@app.route('/carroms')
def carroms():
    return render_template('carrom.html')

@app.route('/carroms/<team1>/<team2>')
def cricket_teams(team1, team2):
    return render_template('carrom_teams.html', t1=team1, t2=team2)

@app.route('/baseball')
def baseball():
    return render_template('baseball.html')

if __name__ == '__main__':
    app.run(debug=True)