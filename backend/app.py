from flask import Flask, jsonify, request , send_from_directory
from routes.finance import finance_bp
from routes.lifestyle import lifestyle_bp
from routes.ai import ai_bp



app = Flask(__name__, static_folder="../frontend")

app.register_blueprint(finance_bp , url_prefix="/api/finance")
app.register_blueprint(lifestyle_bp)
app.register_blueprint(ai_bp)

@app.route("/")
def home():
    return send_from_directory("../frontend","index.html")

if __name__ == "__main__":
    app.run(debug=True)
