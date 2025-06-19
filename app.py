from flask import Flask
from routes.chat_routes import chat_bp
from routes.sentiment_routes import sentiment_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(chat_bp, url_prefix="/chat")
app.register_blueprint(sentiment_bp, url_prefix="/analyze")

@app.route("/")
def home():
    return {
        "message": "Citizen AI Flask App is running",
        "routes": ["/chat", "/analyze"]
    }

if __name__ == "__main__":
    app.run(debug=True)
