from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return """
    <h1>My E-Commerce Store</h1>
    <h2>Cloud-Native Application</h2>
    <p>Automated deployment using Docker.</p>
    <p>Application is running successfully!</p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)