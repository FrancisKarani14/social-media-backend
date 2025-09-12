from app import app, db
from models import Post, Profile, Comment, User

with app.app_context():
    # clear existing data

    Profile.query.delete()
    User.query.delete()
    Post.query.delete()
    Comment.query.delete()

    # adds data into the db
    # adds users into the db
    user1 = User(user_name="Karani", password="Karani123")
    user2 = User(user_name="Kimani", password="Kimani123")
    user3 = User(user_name="Jecinta", password="Jecinta123")

    # adds profiles into the db and links them to the users
    profile1 = Profile(bio="Software Developer", user=user1)
    profile2 = Profile(bio="Stock Brocker", user=user2)
    profile3 = Profile(bio="therapist", user=user3)

    # adds posts
    post1 = Post(title="My First Flask App",
                 content="Flask + SQLAlchemy is fun!")
    post2 = Post(title="ML Journey",
                 content="Started learning machine learning...")
    # create comments
    comment1 = Comment(content="Nice post bro", post=post1)
    comment2 = Comment(content="Good luck on your ML journey", post=post2)
    comment3 = Comment(content="Nice work bro keep up", post=post1)
    comment4 = Comment(content="Me too bro lets keep in touch", post=post2)

    # save all to db
    db.session.add_all([user1, user2, user3, profile3, profile1, profile2,
                       post1, post2, comment1, comment2, comment3, comment4])
    db.session.commit()
    print("✅ Database seeded successfully with users, profiles, posts, and comments!")
