from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__)

# Ensure a JSON file exists
DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)  # Initialize with an empty list


@app.route("/")
def home():
    return render_template("index.html")  # Render HTML page


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.json  # Get JSON data from frontend
        print(f"Received Data: {data}")  # Print in logs

        # Load existing data from JSON file
        with open(DATA_FILE, "r") as f:
            existing_data = json.load(f)

        # Append new data
        existing_data.append(data)

        # Save updated data to JSON file
        with open(DATA_FILE, "w") as f:
            json.dump(existing_data, f, indent=4)

        return jsonify({"message": "Data saved successfully", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
