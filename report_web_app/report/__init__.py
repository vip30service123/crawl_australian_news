import os

from flask import Flask, render_template, request

from .src.plot import most_word_appearence


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

            most_word_appearence("report/static/plot.png", topk=topk)

            return render_template("frequency.html", do_show=True)    

        return render_template("frequency.html", do_show=False)
    
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template("base.html")


    return app