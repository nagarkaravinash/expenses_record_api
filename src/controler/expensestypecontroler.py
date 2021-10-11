from src import app
from flask import request
from src.models.expensestypemodel import expensestypemodel

b=expensestypemodel()

@app.route("/expensestype/addexpensestype",methods=["POST"])
def addexpensestype():
    return b.addexpensestype_model(request.form)

@app.route("/expensestype/delet/<id>",methods=["GET"])
def deletexpensestype(id):
    return b.delete_expensetype(id)

@app.route("/expensestype/userwise/<uid>",methods=["GET"])
def userwise_expenses_type(uid):
    return b.userwise_expensestype(uid)

@app.route("/expensestype/update/<id>",methods=["POST"])
def update_expensestype(id):
    return b.update_expensestype(request.form,id)















@app.route("/expensestype/order/<method>",methods=["GET"])
def orderexpensestype(method):
    return b.order_expensestype(method)


