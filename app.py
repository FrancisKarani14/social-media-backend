from flask import Flask, render_template
from flask_migrate import Migrate
from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///social.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

migrate= Migrate(app, db)
db.init_app(app)


@app.route("/")
def welcome():
    user="Karani"
    return render_template("index.html", name=user)

    



if __name__ == "__main__":
    app.run(debug=True)
    
   

