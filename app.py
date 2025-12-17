
from flask import Flask, render_template

app = Flask(__name__)

# होम पेज - यहाँ से आप दोनों टेबल पर जा सकते हैं
@app.route('/')
def index():
    return render_template('index.html')

# पुराना Centers of Life पेज
@app.route('/centers')
def centers():
    return render_template('centers.html')

# आपका नया मिशन वक्तव्य पेज
@app.route('/mission')
def mission():
    return render_template('mission.html')

if __name__ == '__main__':
    app.run(debug=False)
