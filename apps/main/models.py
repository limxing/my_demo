from apps.core import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    userpassword = db.Column(db.String(64))
    creatdate = db.Column(db.DateTime)
    updatedate = db.Column(db.DateTime)
    userinfo = db.relationship('UserInfo', uselist=False, backref='userinfo')
    def __repr__(self):
        return '<User %r>' % (self.username)

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<UserInfo %r>' % (self.nickname)