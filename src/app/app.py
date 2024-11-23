from typing import Dict

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() -> Dict[str, str]:
    return {'message': 'Hello, Flask!'}

if __name__ == "__main__":
    app.run(debug=True)
