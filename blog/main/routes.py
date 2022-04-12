from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', title='Главная')


@main.route('/blog')
def blog():
    return render_template('index.html', title='Блог')


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