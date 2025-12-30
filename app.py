from flask import Flask, render_template

app = Flask(__name__)

# --- कोर डैशबोर्ड ---
@app.route('/')
def index(): return render_template('index.html')

@app.route('/mission')
def mission(): return render_template('mission.html')

@app.route('/centers-matrix')
def centers(): return render_template('centers_matrix.html')

# --- व्यक्तिगत विकास और आदतें ---
@app.route('/kaizen-steps')
def kaizen_steps(): return render_template('kaizen_steps.html')

@app.route('/sharpen-the-saw')
def sharpen_saw(): return render_template('sharpen_the_saw.html')

@app.route('/victory-hour')
def victory(): return render_template('victory_hour.html')

@app.route('/success-denominator')
def success(): return render_template('success_denominator.html')

# --- सामाजिक और भावनात्मक कौशल (SEL) ---
@app.route('/skills-growth')
def skills(): return render_template('skills.html')  # आपकी SEL वाली फाइल

@app.route('/stoplight')
def stoplight(): return render_template('stoplight.html')

@app.route('/xyz-formula')
def xyz_formula(): return render_template('xyz_formula.html')

@app.route('/win-win')
def winwin(): return render_template('win_win.html')

# --- पैरेंटिंग और विरासत ---
@app.route('/parenting-styles')
def parenting_styles(): return render_template('parenting_styles.html')

@app.route('/child-confidence')
def child_confidence(): return render_template('child_confidence.html')

@app.route('/parenting-quiz')
def parenting_quiz(): return render_template('parenting_quiz.html')

@app.route('/father-forgets')
def father(): return render_template('father_forgets.html')

@app.route('/legacy-service')
def legacy(): return render_template('legacy_service.html')

# --- अन्य थ्योरी ---
@app.route('/perspective-matrix')
def perspective(): return render_template('perspective_matrix.html')

@app.route('/maturity-continuum')
def maturity(): return render_template('maturity_continuum.html')

@app.route('/ppc-balance')
def ppc(): return render_template('ppc_balance.html')

@app.route('/self-acceptance')
def self_acceptance():
    return render_template('self_science.html')


@app.route('/reading-list')
def reading_list():
    return render_template('reading_list.html')



if __name__ == '__main__':
    app.run(debug=False)
