from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('centers_matrix.html') # अब सीधे पहली टेबल खुलेगी

@app.route('/perspective')
def perspective():
    return render_template('perspective_matrix.html')

@app.route('/skills')
def skills():
    return render_template('skills_growth.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')


@app.route('/stoplight')
def stoplight():
    return render_template('stoplight.html')



if __name__ == '__main__':
    app.run(debug=False)
