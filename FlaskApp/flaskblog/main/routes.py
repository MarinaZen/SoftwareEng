from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flask_login import login_required
import subprocess
from bokeh.embed import server_document



#initialization of main module as a blueprint
main = Blueprint('main', __name__)

#this allows the bokeh app running on port 5006 to be accessed by Flask at port 5000
def bash_command(cmd):
    subprocess.Popen(cmd, shell=True)
bash_command('bokeh serve ./flaskblog/multi_plot.py --allow-websocket-origin=127.0.0.1:5000')

#creation of main web pages routes
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
    return render_template('map.html', title='Map')

@main.route("/statistics")
@login_required
def statistics():
    script=server_document("http://localhost:5006/multi_plot")
    print(script)
    return render_template('statistic.html', bokS=script, title='Statistics')
