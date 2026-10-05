from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>OpsPilot</title>
        </head>
        <body>
            <h1>🚀 OpsPilot</h1>
            <h2>Cloud Deployment & Infrastructure Operations Platform</h2>

            <p><b>Status:</b> Application is running</p>
            <p><b>Hostname:</b> {socket.gethostname()}</p>
            <p><b>Time:</b> {datetime.datetime.now()}</p>

            <hr>

            <h3>DevOps Stack</h3>
            <ul>
                <li>Linux</li>
                <li>Git & GitHub</li>
                <li>Docker</li>
                <li>Jenkins</li>
                <li>AWS EC2</li>
                <li>Nginx</li>
                <li>Terraform</li>
                <li>Prometheus</li>
                <li>Grafana</li>
            </ul>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "opspilot",
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
