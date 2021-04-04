from flask import Flask, redirect, url_for, render_template, request, jsonify
import pymongo
from bson.json_util import dumps


#setup server configuration
app = Flask(__name__)

#DB configuration
myclient = pymongo.MongoClient("mongodb+srv://pratik:12345@cluster0.qgys7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["userdata"]
mycol = mydb["users"]




#User displayed pages
@app.route('/')
def homepage():
    return "Home"

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/list', methods=['GET'])
def list():
    return render_template("list.html")

@app.route('/create', methods=['GET'])
def create():
    return render_template("create.html")








#API endpoints

#Login authorization
@app.route('/auth', methods=['POST'])
def auth():
    dbData = mycol.find_one({"email": request.form["email"]})
    
    
    if (bool(dbData) and  request.form["pass"] == dbData["pass"]):
        return redirect(url_for('list'))
    else:
        return redirect(url_for('login'))









#New user creation
@app.route('/new', methods=['POST'])
def new():

    data = {"email":request.form["email"],"pass":request.form["pass"],"name":request.form["name"], "phone":request.form["phone"]}
    
    mycol.insert_one(data)
    return redirect(url_for('user'))







#User listing
@app.route('/user', methods=['GET'])
def user():        
    dbData = mycol.find({}, {'_id': False})
    return jsonify(dumps(dbData))




if __name__ == '__main__':
    print('Server is ready!')
    app.run(host='0.0.0.0', port=5000)
