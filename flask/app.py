from flask import Flask, g, request
from pymongo import Connection
import os, json

app = Flask(__name__)


@app.before_request
def before_request():
    g.Connection = Connection(os.environ['MYDATABASE_PORT_27017_TCP_ADDR'])
    g.db = g.Connection.mydatabase

@app.route("/")
def hello():
	city = request.args.get('city')
	state = request.args.get('state')
	pop = request.args.get('pop')
	mylist = []
	if pop is not None:
		mypop = pop.split("-")
		if mypop[0] == "<":
			myrequests = {"city":{'$regex':city},"state":{'$regex':state}, "pop":{"$lt": int(mypop[1]) }}
		elif mypop[0] == ">":
			myrequests = {"city":{'$regex':city},"state":{'$regex':state}, "pop": {"$gt": int(mypop[1]) }}
	else:
		myrequests = {"city":{'$regex':city},"state":{'$regex':state}}
		
	for x in g.db.mytable.find({"$and": [myrequests]}): 
		mylist.append(x)
	
	return json.dumps(mylist)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
