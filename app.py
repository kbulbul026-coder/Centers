from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/centers-matrix')
def centers_matrix():
    return render_template('centers_matrix.html')

@app.route('/perspective-matrix')
def perspective_matrix():
    return render_template('perspective_matrix.html')

@app.route('/skills-growth')
def skills_growth():
    return render_template('skills_growth.html')

@app.route('/stoplight')
def stoplight():
    return render_template('stoplight.html')

@app.route('/victory-hour')
def victory_hour():
    return render_template('victory_hour.html')

@app.route('/success-denominator')
def success_denominator():
    return render_template('success_denominator.html')

@app.route('/legacy-service')
def legacy_service():
    return render_template('legacy_service.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/win-win')
def win_win():
    return render_template('win_win.html')

@app.route('/maturity-continuum')
def maturity():
    return render_template('maturity_continuum.html')

@app.route('/ppc-balance')
def ppc_balance():
    return render_template('ppc_balance.html')


if __name__ == '__main__':
    app.run(debug=False)
