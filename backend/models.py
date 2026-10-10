import numpy as np
from sklearn.linear_model import LinearRegression

def predict_savings(income, expenses):
    X = np.array([[income]])
    y = np.array([income - expenses])
    model = LinearRegression()
    model.fit(X, y)
    return int(model.predict([[income]])[0])

def lifestyle_score(sleep, exercise):
    sleep_score = max(0, 1 - abs(sleep - 7) / 3)
    exercise_score = min(exercise / 45, 1)
    return round((0.6 * sleep_score + 0.4 * exercise_score) * 100, 2)
