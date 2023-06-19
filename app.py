from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/prevalence')
def prevalence():
    return render_template('prevalence.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/current-situation')
def current_situation():
    return render_template('current_situation.html')

@app.route('/key-players')
def key_players():
    return render_template('key_players.html')

@app.route('/needs')
def needs():
    return render_template('needs.html')

@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')

if __name__ == '__main__':
    app.run(debug=True)
