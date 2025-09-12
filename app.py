from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, User, Post


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///social.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

migrate= Migrate(app, db)
db.init_app(app)


@app.route("/")
def welcome():
    user="Karani"
    return render_template("index.html", name=user)

@app.route("/users")
def list_users():
    all_users=User.query.all()
    return render_template("user.html", users=all_users)

    
@app.route("/posts")
def view_posts():
    list_posts = Post.query.all()
    return render_template("posts.html", posts=list_posts)


if __name__ == "__main__":
    app.run(debug=True)
    
   

