import os

from flask import Flask, render_template, request

from .src.plot import top_k_keywords, top_k_bigrams
from .src.conn import search_term


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/frequency', methods=["GET", "POST"])
    def frequency():
        if request.method == "POST":
            topk = int(request.form['topk'])
            days = request.form['days']

            top_k_keywords("report/static/top_k_keyword.png", topk=topk, days=days)
            top_k_bigrams("report/static/top_k_bigram.png", topk=topk, days=days)

            return render_template("frequency.html", do_show=True)    

        return render_template("frequency.html", do_show=False)
    
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template("home.html")
    
    @app.route("/search", methods=["GET", "POST"])
    def search():
        search_value = ""
        searched_items = []

        if request.method == "POST":
            search_value = request.form['search']
            days = request.form['days']

            searched_items = search_term(search_value, days=days)


        return render_template("search.html", search_value=search_value, searched_items=searched_items)

    return app



