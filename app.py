from flask import Flask
from routes.chat_routes import chat_routes
from routes.sentiment_routes import sentiment_routes

app = Flask(__name__)

# Register routes with different URL prefixes
app.register_blueprint(chat_routes, url_prefix='/chat')
app.register_blueprint(sentiment_routes, url_prefix='/sentiment')

if __name__ == "__main__":
    app.run(debug=True)
