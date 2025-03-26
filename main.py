import os
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route("/calculate_factorial/<int:number>")
def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers", 400
    return str(math.factorial(number))

@app.route("/check_prime/<int:number>")
def check_prime(number):
    if number <= 1:
        return "Not prime", 200
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not prime", 200
    return "Prime", 200

@app.route("/reverse_string", methods=["POST"])
def reverse_string():
    data = request.get_json()
    if "text" not in data:
        return "Missing 'text' field", 400
    return data["text"][::-1], 200

@app.route("/calculate_distance", methods=["POST"])
def calculate_distance():
    data = request.get_json()
    if not all(key in data for key in ["x1", "y1", "x2", "y2"]):
        return "Missing coordinates", 400
    distance = math.sqrt((data["x2"] - data["x1"])**2 + (data["y2"] - data["y1"])**2)
    return jsonify({"distance": distance}), 200

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))