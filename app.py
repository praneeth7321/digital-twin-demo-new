# ------------------------------------------------------
# AI-Powered Digital Twin for Personal Finance & Lifestyle
# Prototype built using Flask + Linear Regression
# Author: Praneeth Netha & Team | 2025
# ------------------------------------------------------

from flask import Flask, jsonify, request, send_from_directory
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# -------------------- App Setup -----------------------
app = Flask(__name__, static_folder="static", static_url_path="/")

# -------------------- Data Generation -----------------
def gen_dummy(days=90, seed=42):
    """Generate synthetic personal finance + lifestyle data."""
    rng = np.random.default_rng(seed)
    dates = [datetime.today() - timedelta(days=i) for i in range(days)][::-1]
    income = rng.normal(50000, 4000, size=days).clip(35000, 65000)
    expenses = income * rng.normal(0.62, 0.06, size=days).clip(0.45, 0.85)
    sleep = rng.normal(6.8, 0.7, size=days).clip(4.5, 9.5)
    exercise = rng.normal(35, 15, size=days).clip(0, 120)

    df = pd.DataFrame({
        "date": dates,
        "income": income.astype(int),
        "expenses": expenses.astype(int),
        "savings": (income - expenses).astype(int),
        "sleep": np.round(sleep, 2),
        "exercise": exercise.round(0).astype(int)
    })
    return df


# -------------------- Prediction Logic ----------------
def predict_next_savings(df, horizon=30):
    """Predict average savings over the next N days using linear regression."""
    recent = df.tail(60).reset_index(drop=True)
    X = np.arange(len(recent)).reshape(-1, 1)
    y = recent["savings"].values
    model = LinearRegression().fit(X, y)
    future_X = np.arange(len(recent), len(recent) + horizon).reshape(-1, 1)
    preds = model.predict(future_X)
    return float(np.mean(preds))


def lifestyle_score(sleep_h, ex_min):
    """Compute lifestyle score based on sleep and exercise."""
    sleep_component = max(0, 1 - abs(sleep_h - 7.5) / 3.0)
    exercise_component = min(ex_min / 45.0, 1.0)
    score = (0.6 * sleep_component + 0.4 * exercise_component) * 100
    return round(np.clip(score, 0, 100), 1)


def savings_rate(income, expenses):
    """Compute savings rate as a percentage of income."""
    if income <= 0:
        return 0.0
    return round(np.clip((income - expenses) / income * 100, -100, 100), 1)


def recommendations(income, expenses, sleep_h, ex_min, target=20):
    """Generate text-based recommendations."""
    recs = []
    rate = savings_rate(income, expenses)

    # Financial guidance
    if rate < target:
        gap = target - rate
        reduce_amt = round((gap / 100.0) * income, -2)
        recs.append(f"Reduce monthly expenses by ~₹{int(reduce_amt)} to reach {target}% savings.")
    else:
        recs.append("Savings rate is on target—consider investing surplus into SIP or emergency fund.")

    # Lifestyle advice
    if sleep_h < 7:
        recs.append("Increase sleep by ~0.5–1 hour for better recovery.")
    elif sleep_h > 8.5:
        recs.append("Reduce oversleeping to maintain optimal alertness (7–8 hrs).")

    if ex_min < 45:
        recs.append("Target ≥45 mins exercise most days to raise lifestyle score.")
    else:
        recs.append("Great exercise consistency—keep it up!")

    return recs


# -------------------- API Routes ----------------------
HISTORY = gen_dummy(days=90)

@app.route("/")
def index():
    """Serve the main dashboard UI."""
    return send_from_directory("static", "index.html")


@app.route("/api/history")
def api_history():
    """Return synthetic historical data."""
    return jsonify(HISTORY.to_dict(orient="records"))


@app.route("/api/metrics", methods=["POST"])
def api_metrics():
    """Compute metrics and recommendations from user input."""
    data = request.get_json(force=True)
    income = float(data.get("income", 50000))
    expenses = float(data.get("expenses", 32000))
    sleep_h = float(data.get("sleep", 6.8))
    ex_min = float(data.get("exercise", 40))

    next_sav = int(predict_next_savings(HISTORY))

    return jsonify({
        "savingsRate": savings_rate(income, expenses),
        "lifestyleScore": lifestyle_score(sleep_h, ex_min),
        "predictedSavingsNextMonth": next_sav,
        "recommendations": recommendations(income, expenses, sleep_h, ex_min)
    })


@app.route("/api/simulate", methods=["POST"])
def api_simulate():
    """Simulate future 6-month projection."""
    data = request.get_json(force=True)
    income = float(data.get("income", 50000))
    expenses = float(data.get("expenses", 32000))
    sleep_h = float(data.get("sleep", 6.8))
    ex_min = float(data.get("exercise", 40))

    sim_rate = savings_rate(income, expenses)
    sim_score = lifestyle_score(sleep_h, ex_min)

    # 6-month projection (1% growth per month)
    base = max(income - expenses, 0)
    growth = 0.01
    months, values = [], []
    now = datetime.today()
    val = base
    for i in range(6):
        months.append((now.replace(day=1) + pd.DateOffset(months=i)).strftime("%b %Y"))
        values.append(int(val))
        val *= (1 + growth)

    return jsonify({
        "savingsRate": sim_rate,
        "lifestyleScore": sim_score,
        "projection": list(zip(months, values))
    })


# -------------------- Main Entry ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
