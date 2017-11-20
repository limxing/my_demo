from flask import Blueprint, render_template, session, request,jsonify
import time
from apps.main.models import *

mod = Blueprint('socketdemo', __name__, url_prefix='/', template_folder='templates')

@mod.route('/', methods=("post", "get"))
def index():
    return render_template('index.html')
