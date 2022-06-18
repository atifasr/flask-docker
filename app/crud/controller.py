from flask import jsonify
from flask import request

from app.crud.models import Students,Streams,UserStreams
from app import db


def push_data():
    params = request.json
    studnts = Students(**params)
    db.session.add(studnts) 
    db.session.commit() 
    
    return jsonify({'status':'OK','data':params}),200



def get_data():

    students = db.session.query(Students).all()
    
    return jsonify({'status':'OK','data':[
            {   
                'id':student.id,
                'name':student.name,
                'place':student.place,
                'address':student.address,
                'date_created':student.date_created,
                'date_updated':student.date_updated,
            }
            for student in students
        ]}),200

def create_streams():

    params = request.json

    streams = Streams(**params)
    db.session.add(streams) 
    db.session.commit() 
    
    return jsonify({'status':'OK','message':'Data added!'}),200

def user_stream():

    params = request.json

    streams = UserStreams(**params)
    db.session.add(streams) 
    db.session.commit() 
    
    return jsonify({'status':'OK','message':'Data added!'}),200

def related_streams():


    streams = db.session.query(Students,Streams,UserStreams).with_entities(
        UserStreams.id,
        Students.name,
        Students.place,
        Students.address,
        UserStreams.date_updated,
        UserStreams.date_created,
    ).join(UserStreams,Students.id == UserStreams.std_id).join(Streams,UserStreams.steam_id == Streams.id).all()
    
    
    return jsonify({'status':'OK','data':[
            {   
                'id':stream.id,
                'name':stream.name,
                'place':stream.place,
                'address':stream.address,
                'date_created':stream.date_created,
                'date_updated':stream.date_updated,
            }
            for stream in streams
        ]}),200