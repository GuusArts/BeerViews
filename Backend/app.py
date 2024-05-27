from flask import Flask
from Controllers.BarController import BarController_blueprint
from Controllers.BeerController import BeerController_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(BarController_blueprint)
app.register_blueprint(BeerController_blueprint)

if __name__ == "__main__":
    app.run(debug=True)