from flask import render_template, request, Blueprint
from flaskblog.models import Post
<<<<<<< HEAD
from flaskblog.connection import bikeJson, stations


main = Blueprint('main', __name__)



=======
#initialization of main module as a blueprint
main = Blueprint('main', __name__)

#creation of main web pages routes
>>>>>>> e1c914fc9bfad7dd39aea6a70d5934a475e21369
@main.route("/")
@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)

@main.route("/map")
def map():
    return render_template('map.html', title='Map', bikeJson = bikeJson, stations=stations)
