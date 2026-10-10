from flask import Blueprint, request, jsonify

finance_bp = Blueprint("finance", __name__)

# Temporary in-memory storage (prototype only)
finance_data = {}

@finance_bp.route("/add", methods=["POST"])
def add_finance():
    data = request.get_json()

    income = data.get("income")
    expenses = data.get("expenses")

    if income is None or expenses is None:
        return jsonify({"error": "Income and expenses required"}), 400

    total_expense = sum(expenses)
    savings = income - total_expense
    savings_percentage = (savings / income) * 100 if income > 0 else 0

    finance_data["summary"] = {
        "income": income,
        "total_expense": total_expense,
        "savings": savings,
        "savings_percentage": round(savings_percentage, 2)
    }

    return jsonify({"message": "Finance data added successfully"})
    

@finance_bp.route("/summary", methods=["GET"])
def get_summary():
    if "summary" not in finance_data:
        return jsonify({"error": "No finance data available"}), 404

    return jsonify(finance_data["summary"])