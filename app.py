from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This will look for templates/centers.html
    return render_template('centers.html')

if __name__ == '__main__':
    app.run(debug=False)
