from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- कोर डैशबोर्ड ---
@app.route('/')
def index(): return render_template('index.html')

@app.route('/mission')
def mission(): return render_template('mission.html')
'''
@app.route('/centers-matrix')
def centers(): return render_template('centers_matrix.html')
'''
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

@app.route('/self-science')
def self_acceptance():
    return render_template('self_science.html')


@app.route('/reading-list')
def reading_list():
    return render_template('reading_list.html')

@app.route('/purpose')
def purpose():
    return render_template('life_purpose.html')

@app.route('/reality-check')
def reality_check():
    return render_template('reality_check.html')



'''
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# आपकी 21 किताबों से प्रेरित दैनिक विचार
quotes = [
    "सफल लोग वह करते हैं जो असफल लोग नहीं करना चाहते।",
    "आपका बैंक बैलेंस आपके कौशल (Value Creation) का प्रतिबिंब है।",
    "छोटी सही आदतें + दीर्घकालिक सोच = असाधारण परिणाम।",
    "पहले समझने की कोशिश करें, फिर समझे जाने की (आदत 5)।",
    "आपका जीवन एक भव्य मशाल है, इसे समाज के लिए जलने दें।"
]

@app.route('/')
def index():
    daily_quote = random.choice(quotes)
    return render_template('index.html', quote=daily_quote)

@app.route('/reading-list')
def reading_list():
    return render_template('reading_list.html')

@app.route('/purpose')
def purpose():
    return render_template('life_purpose.html')

@app.route('/self-science')
def self_science():
    return render_template('self_science.html')

@app.route('/kaizen')
def kaizen():
    return render_template('kaizen_steps.html')

@app.route('/success-denominator')
def success_denominator():
    return render_template('success_denominator.html')

if __name__ == '__main__':
    app.run(debug=True)

'''


@app.route('/knowledge-map')
def knowledge_map():
    return render_template('knowledge_map.html')


@app.route('/emotional-coach')
def emotional_coach():
    return render_template('emotional_coach.html')

@app.route('/parenting-quiz')
def parenting_quiz():
    return render_template('parenting_quiz.html')

'''
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# --- 1. दैनिक विचार डेटा ---
quotes = [
    "सफल लोग वह करते हैं जो असफल लोग नहीं करना चाहते।",
    "आपका बैंक बैलेंस आपके कौशल (Value Creation) का प्रतिबिंब है।",
    "छोटी सही आदतें + दीर्घकालिक सोच = असाधारण परिणाम।",
    "पहले समझने की कोशिश करें, फिर समझे जाने की (आदत 5)।",
    "आपका जीवन एक भव्य मशाल है, इसे समाज के लिए जलने दें।"
]

# --- 2. मुख्य रूट्स ---

@app.route('/')
def index():
    daily_quote = random.choice(quotes)
    return render_template('index.html', quote=daily_quote)

# ज्ञान और विकास रूट्स
@app.route('/reading-list')
def reading_list(): return render_template('reading_list.html')

@app.route('/knowledge-map')
def knowledge_map(): return render_template('knowledge_map.html')

@app.route('/purpose')
def purpose(): return render_template('life_purpose.html')

# SEL और भावनात्मक रूट्स
@app.route('/self-science')
@app.route('/self-acceptance')
def self_science(): return render_template('self_science.html')

@app.route('/emotional-coach')
@app.route('/child-confidence')
def emotional_coach(): return render_template('emotional_coach.html')

@app.route('/xyz-formula')
def xyz_formula(): return render_template('xyz_formula.html')

# सिद्धांत और संतुलन रूट्स
@app.route('/sharpen-the-saw')
def sharpen_saw(): return render_template('sharpen_saw.html')

@app.route('/stoplight')
def stoplight(): return render_template('stoplight.html')

@app.route('/victory-hour')
def victory_hour(): return render_template('victory_hour.html')

@app.route('/parenting-quiz')
def parenting_quiz(): return render_template('parenting_quiz.html')

@app.route('/mission')
def mission(): return render_template('mission.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
# --- 1. JSON Data for D3.js Mind Map ---
MIND_MAP_JSON = {                                                                                                                              "name": "You / Self-Identification",
  "icon": "👤",
  "children": [
    {
      "name": "Principles Center 🌟",
      "color": "blue",                                                                                                                             "children": [
        {"name": "Spouse/Partner", "icon": "🤝", "value": "Equal partner in a mutually beneficial interdependent relationship"},
        {"name": "Family", "icon": "🏡", "value": "Sacred stewardship and responsibility"},
        {"name": "Friends", "icon": "🌱", "value": "Companions in growth and shared values"},
        {"name": "Work", "icon": "🧭", "value": "Opportunity to contribute meaningfully and ethically"},
        {"name": "Possessions", "icon": "✨", "value": "Tools to contribute or manage responsibly"},
        {"name": "Community/Church", "icon": "🙏", "value": "Platform for service and shared moral commitment"},
        {"name": "Self", "icon": "🧘", "value": "Focus on growth, contribution, and character development"}
      ]
    },
    {
      "name": "Self Center",
      "color": "purple",
      "children": [
        {"name": "Spouse/Partner", "icon": " Narcissus", "value": "Someone who should meet my needs and validate my identity"},
        {"name": "Family", "icon": "👪", "value": "Extensions of myself; source of unconditional approval"},
        {"name": "Friends", "icon": "🙌", "value": "People who admire and affirm my choices"},
        {"name": "Work", "icon": "🗣️", "value": "Platform for self-expression and recognition"},
        {"name": "Possessions", "icon": "💎", "value": "Symbols that reflect my unique taste and status"},
        {"name": "Community/Church", "icon": "🎙️", "value": "Venue for performing my role or seeking attention"},
        {"name": "Self", "icon": "👑", "value": "The primary focus and source of all goals"}
      ]
    },
    {
      "name": "Work Center",
      "color": "orange",
      "children": [
        {"name": "Spouse/Partner", "icon": "🛠️", "value": "Support system for career success; handles domestic distractions"},
        {"name": "Family", "icon": "💼", "value": "Dependents relying on my productivity; reason for long hours"},
        {"name": "Friends", "icon": "🤝", "value": "Networking contacts or people who advance my career"},
        {"name": "Work", "icon": "📈", "value": "The central duty and main source of identity and security"},
        {"name": "Possessions", "icon": "💰", "value": "Rewards for hard work; symbols of achievement"},
        {"name": "Community/Church", "icon": "📢", "value": "Place to showcase professional leadership or network"},
        {"name": "Self", "icon": "⌚", "value": "Defined by titles, accomplishments, and efficiency"}
      ]
    },
    {
      "name": "Family Center",
      "color": "green",
      "children": [
        {"name": "Spouse/Partner", "icon": "💍", "value": "Core member of family unit; role-based loyalty"},
        {"name": "Family", "icon": "🔒", "value": "The ultimate source of security and the main priority in all decisions"},
        {"name": "Friends", "icon": "🏡", "value": "Extensions of family circle; people who fit into the family unit"},
        {"name": "Work", "icon": "📝", "value": "Duty to provide for family; measured by financial stability"},
        {"name": "Possessions", "icon": "🖼️", "value": "Assets to be inherited or managed for the family's welfare"},
        {"name": "Community/Church", "icon": "👨‍👩‍👧‍👦", "value": "Place to reinforce family traditions and values"},
        {"name": "Self", "icon": "🛡️", "value": "Defined by my role (Parent, Spouse, Provider) within the family"}
      ]
    },
    {
      "name": "Pleasure Center",
      "color": "red",
      "children": [
        {"name": "Spouse/Partner", "icon": "🥳", "value": "Source of fun, excitement, or sensual gratification"},
        {"name": "Family", "icon": "🍹", "value": "Companions for enjoyment and leisure; source of effortless fun"},
        {"name": "Friends", "icon": "🎈", "value": "People to party with; temporary companions for entertainment"},
        {"name": "Work", "icon": "💸", "value": "Means to afford pleasures; distraction from boredom"},
        {"name": "Possessions", "icon": "🎮", "value": "Toys and tools that maximize enjoyment and comfort"},
        {"name": "Community/Church", "icon": "📺", "value": "Avoided, unless it offers effortless enjoyment or entertainment"},
        {"name": "Self", "icon": "😋", "value": "Focused on comfort, instant gratification, and sensory input"}
      ]
    },
    {
      "name": "Possessions Center",
      "color": "yellow",
      "children": [
        {"name": "Spouse/Partner", "icon": "💎", "value": "Status symbol or extension of personal success"},
        {"name": "Family", "icon": "🏦", "value": "Assets to be inherited or managed; must not damage property"},
        {"name": "Friends", "icon": " admiring", "value": "People who admire my possessions and appreciate my success"},
        {"name": "Work", "icon": "🏆", "value": "The means to acquire, protect, and enhance assets"},
        {"name": "Possessions", "icon": "🏠", "value": "The main focus of security, guidance, and pride"},
        {"name": "Community/Church", "icon": "🖼️", "value": "Place to display wealth and reinforce social standing"},
        {"name": "Self", "icon": "🔑", "value": "Worth is tied directly to net worth and material holdings"}
      ]
    }
  ]
}

# --- 2. Legend Data ---
# This data is used to render the color key in the HTML template.
CENTER_LEGEND = [
    {"name": "Principles Center", "color": "blue"},
    {"name": "Self Center", "color": "purple"},
    {"name": "Work Center", "color": "orange"},
    {"name": "Family Center", "color": "green"},
    {"name": "Pleasure Center", "color": "red"},
    {"name": "Possessions Center", "color": "yellow"}
]

@app.route('/centers-matrix')
def centers_matrix(): return render_template('mind_map.html',legend_data=CENTER_LEGEND) # Covey's Mind Map


# --- 3. API डेटा (D3.js Mind Map के लिए) ---
@app.route('/api/data')
def api_data():
    # यहाँ आपका Covey's Centers वाला JSON डेटा आएगा
    return jsonify(MIND_MAP_JSON)


if __name__ == '__main__':
    app.run(debug=False)
