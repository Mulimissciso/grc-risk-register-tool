from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)
# In-memory database (we'll upgrade later)
risks = []

# Function to calculate risk score and level
def calculate_risk(likelihood, impact):
    score = likelihood * impact

    if score <= 5:
        level = "Low"
    elif score <= 15:
        level = "Medium"
    else:
        level = "High"

    return score, level

# Add a new risk
@app.route('/add_risk', methods=['POST'])
def add_risk():
    data = request.get_json()

    likelihood = int(data['likelihood'])
    impact = int(data['impact'])

    score, level = calculate_risk(likelihood, impact)

    risk = {
        "id": len(risks) + 1,
        "title": data['title'],
        "description": data['description'],
        "likelihood": likelihood,
        "impact": impact,
        "risk_score": score,
        "level": level,
        "mitigation": data.get('mitigation', ''),
        "owner": data.get('owner', '')
    }

    risks.append(risk)

    return jsonify({
        "message": "Risk added successfully",
        "risk": risk
    })

# View all risks
@app.route('/risks', methods=['GET'])
def get_risks():
    return jsonify(risks)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)