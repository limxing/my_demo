from flask import Blueprint, render_template, session, request,jsonify
import time
from apps.main.models import *
from .forms import MyForm
from apps.core import db
from .modelschema import UserSchema

mod = Blueprint('main', __name__, url_prefix='', template_folder='templates')

@mod.route('/', methods=("post", "get"))
def index():
    return render_template('index.html')

@mod.route('/login' ,methods=["POST", "GET"])
def login():
    # form = request.form
    # print(form)
    # if request.method == "GET":
    #     return render_template("login.html", form=form)
    # # 由于request中的form参数以字典的形式存在，故以下语句等价
    # try:
    #     uname = request.form['username']
    #     pwd = request.form['password']
    #     print(uname,pwd)
    # except Exception as e:
    #     print(e)
    # return 'finish'
    form = MyForm()
    if not form.validate_on_submit():
        return render_template("login.html",form=form)
    else:
        if form.validate():
            user = db.session.query(User).filter_by(username=form.username.data, userpassword=form.password.data).first()
            if user == None:
                return render_template('login.html', form=form)
            return str(UserSchema().dumps(user).data).replace('\'','\"').replace('None','NULL')
        else:
            print(form.errors)
            return u"错误"

