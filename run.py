from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Главная')


@app.route('/characters_page')
def characters_page():
    return render_template('characters_page.html')


@app.route('/villages_page')
def villages_page():
    return render_template('villages_page.html')


@app.route('/technology_page')
def technology_page():
    return render_template('technology_page.html')


@app.route('/guns_page')
def guns_page():
    return render_template('guns_page.html')


@app.route('/hronology_page')
def hronology_page():
    return render_template('hronology_page.html')

if __name__ == '__main__':
    app.run(debug=True, port=5656)


