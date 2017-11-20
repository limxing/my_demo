from flask import Blueprint, render_template, session, request,jsonify
import time
from apps.main.models import *
from .forms import MyForm
from apps.core import db

mod = Blueprint('socketdemo', __name__, url_prefix='/', template_folder='templates')

@mod.route('/', methods=("post", "get"))
def index():
    return render_template('index.html')

@mod.route('/login' ,methods=("post", "get"))
def login():
    form = MyForm()
    if not form.validate_on_submit():
        return render_template('login.html', form=form)
    user = db.session.query(User).filter_by(username=form.username,password=form.password).first()
    if user == None:
        return render_template('login.html', form=form)
    return '登陆成功'
