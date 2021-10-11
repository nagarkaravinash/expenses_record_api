import psycopg2
from psycopg2.extras import RealDictCursor
from flask import make_response

class expensesmodel:
    def __init__(self):
        self.con=psycopg2.connect(dbname="postgres",user="postgres",password="123456",host="localhost",port=5432)
        self.con.set_session(autocommit=True)
        self.cur=self.con.cursor(cursor_factory=RealDictCursor)

    def addexpenses_model(self,userdata):
        try:
            self.cur.execute(f"insert into Expenses(payee,amount,exp_type_id,uid) values('{userdata['payee']}','{userdata['amount']}','{userdata['exp_type_id']}','{userdata['uid']}')")
            if self.cur.rowcount>0:
                return make_response({"status":"Added expenses successfully"},200)
            else:
                return make_response({"massage":"Nothing to Add"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)


    def delete_expense(self,id):
        try:
            self.cur.execute(f"delete from expenses where id={id}")
            if self.cur.rowcount>0:
                return make_response({"status":"Deleted expenses successfully"},200)
            else:
                return make_response({"massage":"nothing to delet"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)


    def expenses_userwise(self,uid):
        try:
            self.cur.execute(f"SELECT * from filter_view where uid:: int={uid}")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"massage":"data not found"},204) 
            else:
                return make_response({"status":"successfull","payload":result},200) 
                
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500) 
        

    def order_expenses(self,method):
        try:
            self.cur.execute(f"SELECT * FROM filter_view ORDER BY id {method}")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"massage":"data not found"},204) 
            else:
                return make_response({"status":"Sorted expenses successfully","payload":result},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

    def update_expenses(self,coloumname):
        try:
            self.cur.execute(f"update from expenses where ")
            if self.cur.rowcont>0:
                return make_response({"status":"successfull","massage":"Requested coloum details displayed"},200) 
            else:
                return make_response({"massage":"Requested coloum details not available"},200) 
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

            

    def expenses_date_rangewise(self,date1,date2):
        try:
            self.cur.execute(f"select * from filter_view where date(created_on)>= '{date1}' and date(created_on)<= '{date2}';")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"massage":"data not found"},204) 
            else:
                return make_response({"payload":result},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

    def update_expenses(self,data,idexpenses):
        try:
            self.cur.execute(f"update expenses set payee = '{data['payee']}',amount = {data['amount']},exp_type_id = {data['exp_type_id']} where id = {idexpenses}")
            print(f"update expenses set payee = '{data['payee']}',amount = {data['amount']},exp_type_id = {data['exp_type_id']} where id = {idexpenses}")
            if self.cur.rowcount>0:
                return make_response({"Massage":"Updated successfully"},200)
            else:
                return make_response({"Massage":"nothing to update"},406)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)
