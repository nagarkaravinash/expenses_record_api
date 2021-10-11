from src import app
from flask import request
from src.models.usermodel import usermodel
from flask_cors import CORS, cross_origin

a=usermodel()

@app.route("/user/add",methods=["POST"])
def adduser():
    return a.addusers_model(request.form)

@app.route("/user/getuserdetail/<id>",methods=["GET"])
def getusers(id):
    return a.get_users(id)

@app.route("/user/delet/<id>",methods=["GET"])
def deletuser(id):
    return a.delet_user(id)

@app.route("/user/getall",methods=["GET"])
@cross_origin()
def getallusers():
    return a.getallusers_model()

@app.route("/users/updateinfo/<idvar>",methods=["POST"])
def update_users(idvar):
    return a.update_user(request.form,idvar)






























@app.route("/")
def default_page():
    return "Welcome to default Page"    



# @app.route("/user/citywise/<cityname>")
# def citywise_users(cityname):
#     return a.citywise_users_model(cityname)

# @app.route("/userage")
# def user_ageeighteenplus():
#     return a.user_age()

@app.route("/agerange/<age1>/<age2>")
def age_between_range(age1,age2):
    return a.age_range(age1,age2)

@app.route("/user_email")
def user_gmail_details():
    return a.user_email()

@app.route("/emailwise_user/<email>")
def emailwise_users(email):
    return a.find_emailwise_user_list(email)





@app.route("/user/order/<method>",methods=["GET"])
def orderuser(method):
    return a.order_user(method)

@app.route("/user/distinct/<coloumname>",methods=["GET"])
def disctinctuser(coloumname):
    return a.distinct_user(coloumname)
