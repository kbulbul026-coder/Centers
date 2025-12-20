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

@app.route('/victory-hour') # नया रूट
def victory_hour():
    return render_template('victory_hour.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

# app.py में नया रूट जोड़ें
@app.route('/success-denominator')
def success_denominator():
    return render_template('success_denominator.html')


if __name__ == '__main__':
    app.run(debug=False)
