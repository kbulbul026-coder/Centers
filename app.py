from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')

@app.route('/centers-matrix')
def centers(): return render_template('centers_matrix.html')

@app.route('/perspective-matrix')
def perspective(): return render_template('perspective_matrix.html')

@app.route('/skills-growth')
def skills(): return render_template('skills_growth.html')

@app.route('/stoplight')
def stoplight(): return render_template('stoplight.html')

@app.route('/victory-hour')
def victory(): return render_template('victory_hour.html')

@app.route('/success-denominator')
def success(): return render_template('success_denominator.html')

@app.route('/legacy-service')
def legacy(): return render_template('legacy_service.html')

@app.route('/win-win')
def winwin(): return render_template('win_win.html')

@app.route('/maturity-continuum')
def maturity(): return render_template('maturity_continuum.html')

@app.route('/ppc-balance')
def ppc(): return render_template('ppc_balance.html')

@app.route('/father-forgets')
def father(): return render_template('father_forgets.html')

@app.route('/mission')
def mission(): return render_template('mission.html')

@app.route('/xyz-formula')
def xyz_formula():
    return render_template('xyz_formula.html')


if __name__ == '__main__':
    app.run(debug=False)
