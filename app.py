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

@app.route('/mission')
def mission():
    return render_template('mission.html')

if __name__ == '__main__':
    app.run(debug=False)
