from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from any origin

# Load student data from JSON file
with open("marks.json", "r") as file:
    students = json.load(file)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get names from the request
    marks_list = []

    for name in names:
        student = next((s for s in students if s["name"] == name), None)
        marks_list.append(student["marks"] if student else None)  # Return None if name not found

    return jsonify({"marks": marks_list})

if __name__ == "__main__":
    app.run(debug=True)
