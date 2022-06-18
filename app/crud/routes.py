from app.crud.controller import push_data,get_data,create_streams,user_stream,related_streams
from app import app


app.add_url_rule('/push_data/','push_data',push_data,methods = ['POST'])
app.add_url_rule('/push_data/','get_data',get_data,methods = ['GET'])
app.add_url_rule('/create_stream/','create_streams',create_streams,methods = ['POST'])
app.add_url_rule('/user_stream/','user_stream',user_stream,methods = ['POST'])
app.add_url_rule('/user_stream/','related_streams',related_streams,methods = ['GET'])
