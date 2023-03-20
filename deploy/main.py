from flask import Flask
import os


app = Flask(__name__)


@app.route("/")
def index():
   env_var = os.environ.get("COLOR_ENV")
   return f"Hey {env_var}!"

# start the application on port 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

