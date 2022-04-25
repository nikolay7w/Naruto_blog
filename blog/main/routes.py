from flask import Blueprint, render_template, url_for, request
from flask_login import current_user, login_required

from blog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', title='Главная')


@main.route('/blog')
@login_required
def blog():
    post = Post.query.get(current_user.id)
    if post:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
        image_file = url_for('static', filename=f'profile_pics/{current_user.username}/{post.image_post}')
        return render_template('blog.html', title='Блог', posts=posts, image_file=image_file)
    else:
        return render_template('blog.html', title='Блог', nothing='Постов пока нет')


@main.route('/characters')
def characters_page():
    return render_template('characters_page.html')


@main.route('/villages')
def villages_page():
    return render_template('villages_page.html')


@main.route('/technology')
def technology_page():
    return render_template('technology_page.html')


@main.route('/guns')
def guns_page():
    return render_template('guns_page.html')


@main.route('/hronology')
def hronology_page():
    return render_template('hronology_page.html')