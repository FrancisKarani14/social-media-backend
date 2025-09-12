from flask import Flask
from flask_migrate import Migrate
from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///social.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

migrate= Migrate(app, db)
db.init_app(app)


@app.route("/")
def welcome():

    return "<h1>Welcome to facebook</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    
   

