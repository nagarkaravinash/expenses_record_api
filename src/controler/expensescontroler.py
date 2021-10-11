from src import app
from flask import request
from src.models.expensesmodel import expensesmodel


c=expensesmodel()

@app.route("/expenses/addexpenses",methods=["POST"])
def addexpenses():
    return c.addexpenses_model(request.form)

@app.route("/expenses/delet/<id>",methods=["GET"])
def deletexpenses(id):
    return c.delete_expense(id)

@app.route("/expenses/userwise/<uid>",methods=["GET"])
def userwise_expenses(uid):
    return c.expenses_userwise(uid)

@app.route("/expenses/update/<coloumname>",methods=["GET"])
def updateexpenses(coloumname):
    return c.update_expenses(coloumname)

@app.route("/expenses/<date1>/<date2>")
def expeses_between_range(date1,date2):
    return c.expenses_date_rangewise(date1,date2)

@app.route("/expenses/update/<idexpenses>",methods=["POST"])
def update_exp(idexpenses):
    return c.update_expenses(request.form,idexpenses)

















@app.route("/expenses/order/<method>",methods=["GET"])
def orderexpenses(method):
    return c.order_expenses(method)



@app.route("/expenses/viewexp",methods=["GET"])
def viewexpenses(coloumname):
    return c.view_expenses(coloumname)
