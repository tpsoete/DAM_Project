from flask import Flask,render_template

app = Flask(__name__)


@app.route('/main')
def hello_world():
    return render_template("index.html")

@app.route('/')
def hello_masonry():
    return render_template("masonry.html")

@app.route('/grid')
def hello_grid():
    return render_template("grid.html")

@app.route('/blog')
def hello_blog():
    return render_template("blog.html")

@app.route('/about')
def hello_about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()
