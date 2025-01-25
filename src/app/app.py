from flask import Flask

from src.app.error_handlers import handle_application_exceptions
from src.app.routes import bp

app = Flask(__name__)

app.register_blueprint(bp)
app.register_error_handler(Exception, handle_application_exceptions)

if __name__ == "__main__":
    app.run(debug=True)
