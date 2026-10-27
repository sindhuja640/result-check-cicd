from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for our academic project
STUDENTS = {
    "101": {"name": "Ananya", "marks": 85},
    "102": {"name": "Rahul", "marks": 42},
    "103": {"name": "Priya", "marks": 28},
}


def get_result(roll_number):
    student = STUDENTS.get(roll_number)

    if student is None:
        return None

    return {
        "roll_number": roll_number,
        "name": student["name"],
        "marks": student["marks"],
        "status": "Pass" if student["marks"] >= 35 else "Fail",
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        roll_number = request.form.get("roll_number", "").strip()

        if not roll_number:
            error = "Please enter a roll number."
        else:
            result = get_result(roll_number)
            if result is None:
                error = "No result found for this roll number."

    return render_template("index.html", result=result, error=error)


@app.route("/api/result/<roll_number>")
def api_result(roll_number):
    result = get_result(roll_number)

    if result is None:
        return jsonify({"error": "Result not found"}), 404

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
