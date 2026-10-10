from flask import Blueprint, jsonify
import matplotlib.pyplot as plt
import io
from flask import send_file

lifestyle_bp = Blueprint("lifestyle", __name__, url_prefix="/api/lifestyle")

@lifestyle_bp.route("/test")
def test():
    return jsonify({"status": "Lifestyle API working"})

@lifestyle_bp.route("/chart", methods=["GET"])
def lifestyle_chart():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    sleep_hours = [6, 7, 5.5, 8, 7.5]

    plt.figure()
    plt.bar(days, sleep_hours)
    plt.title("Weekly Sleep Pattern")
    plt.xlabel("Day")
    plt.ylabel("Hours Slept")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()

    return send_file(img, mimetype="image/png")
