
from datetime import datetime
from app import db


class Students(db.Model):
    __tablename__ = 'students'

    id  = db.Column(db.Integer(),primary_key = True, autoincrement = True)
    name = db.Column( db.String(200),nullable = False )
    place = db.Column( db.String(200),nullable = False,)
    address = db.Column( db.String(200),nullable = False )
    date_created = db.Column( db.DateTime,default=datetime.now() )
    date_updated = db.Column( db.DateTime,default=datetime.now() )


class UserStreams(db.Model):
    __tablename__ = 'user_streams'


    id  = db.Column(db.Integer(),primary_key = True, autoincrement = True)
    std_id = db.Column( db.Integer(),db.ForeignKey('students.id'),nullable = False )
    steam_id = db.Column( db.Integer(),db.ForeignKey('streams.id'),nullable = False )
    date_created = db.Column( db.DateTime,default=datetime.now() )
    date_updated = db.Column( db.DateTime,default=datetime.now() )




class Streams(db.Model):
    __tablename__ = 'streams'

    id  = db.Column(db.Integer(),primary_key = True, autoincrement = True)
    name = db.Column( db.String(200),nullable = False )
    place = db.Column( db.String(200),nullable = False ,)
    address = db.Column( db.String(200),nullable = False )
    date_created = db.Column( db.DateTime,default=datetime.now() )
    date_updated = db.Column( db.DateTime,default=datetime.now() )