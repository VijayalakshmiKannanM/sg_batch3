# app.py
# A simple Flask web app to perform basic math operations

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template (kept inside Python for simplicity)
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Math Calculator</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        input, select { padding: 8px; margin: 5px; font-size: 16px; }
        button { padding: 8px 16px; font-size: 16px; cursor: pointer; }
        h2 { color: #2c3e50; }
        .result { margin-top: 20px; font-size: 20px; color: green; }
    </style>
</head>
<body>
    <h2>🧮 Simple Math Operations using Flask</h2>
    <form method="POST">
        <input type="number" name="num1" placeholder="Enter first number" step="any" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">−</option>
            <option value="multiply">×</option>
            <option value="divide">÷</option>
        </select>
        <input type="number" name="num2" placeholder="Enter second number" step="any" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
    <div class="result">
        <strong>Result:</strong> {{ result }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]

            if op == "add":
                result = num1 + num2
            elif op == "subtract":
                result = num1 - num2
            elif op == "multiply":
                result = num1 * num2
            elif op == "divide":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(html, result=result)


if __name__ == "__main__":
    app.run(debug=True)
