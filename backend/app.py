from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__)

# Use absolute path for reliability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/backend/")

def home():
    return render_template("index.html")  # Render HTML page

@app.route("/backend/data", methods=["GET"])
def get_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/backend/submit", methods=["GET", "POST"])
def submit():
    try:
        if request.method == "GET":
            name = request.args.get("name")
            email = request.args.get("email")
            data = {"name": name, "email": email}
        else:
            data = request.json  # For POST requests

        print(f"Received Data: {data}")  # Log the data

        # Load existing data
        with open(DATA_FILE, "r") as f:
            existing_data = json.load(f)

        existing_data.append(data)

        # Save new data
        with open(DATA_FILE, "w") as f:
            json.dump(existing_data, f, indent=4)

        return jsonify({"message": "Data saved successfully", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/backend/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not Found this is test "}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
