from flask import render_template
from app import app


@app.route('/blog')
def hello_blog():
    return render_template("blog.html")