import psycopg2
from psycopg2.extras import RealDictCursor
from flask import make_response

class expensestypemodel:
    def __init__(self):
        self.con=psycopg2.connect(dbname="postgres",user="postgres",password="123456",host="localhost",port=5432)
        self.con.set_session(autocommit=True)
        self.cur=self.con.cursor(cursor_factory=RealDictCursor)

    def addexpensestype_model(self,userdata):
        try:
            self.cur.execute(f"insert into expensestype(exp_name,uid) values('{userdata['exp_name']}','{userdata['uid']}')")
            if self.cur.rowcount>0:
                return make_response({"status":"Added expenses type successfully"},200)
            else:
                return make_response({"status":"nothing to add"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

    def delete_expensetype(self,id):
        try:
            self.cur.execute(f"delete from expensestype where id={id}")
            if self.cur.rowcount>0:
                return make_response({"status":"Deleted expenses type successfully"},200)
            else:
                return make_response({"massage":"nothing to delet"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

    def userwise_expensestype(self,uid):
        try:
            self.cur.execute(f"SELECT * from filter_view where uid= {uid}")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"massage":"data not found"},204) 
            else:
                return make_response({"status":"Displayed requested data successfully","payload":result},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)


    def update_expensestype(self,data,id):
        try:
            self.cur.execute(f"update expensestype set exp_name = '{data['exp_name']}',uid = '{data['uid']}' where id = {id}")
            if self.cur.rowcount>0:
                return make_response({"updated successfully"},200)
            else:
                return make_response({"massage":"nothing to update"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)


    def order_expensestype(self,method):
        try:
            self.cur.execute(f"SELECT * FROM filter_view ORDER BY id {method}")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"status":"Sorted expenses type successfully","payload":result},200)
            else:
                return make_response({"massage":"sorting method not available"},204)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)