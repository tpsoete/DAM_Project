from .about import *
from .blog import *
from .grid import *
from .main import *


@app.route('/')
def hello_masonry():
    print("init /")
    return render_template('masonry.html')
