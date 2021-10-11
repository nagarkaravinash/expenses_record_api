import psycopg2 
from psycopg2.extras import RealDictCursor
from flask import make_response

class usermodel:
    def __init__(self):
        self.con=psycopg2.connect(dbname="postgres", user="postgres",password="123456",host="localhost",port=5432)
        self.con.set_session(autocommit=True)
        self.cur=self.con.cursor(cursor_factory=RealDictCursor)

    def addusers_model(self,userdata):
        try:
            self.cur.execute(f"insert into users(full_name,email,phone,age,salary,city) values('{userdata['full_name']}','{userdata['email']}','{userdata['phone']}',{userdata['age']},{userdata['salary']},'{userdata['city']}')")
            result=self.cur.fetchall()
            if self.cur.rowcount>0:
                return make_response({"status":"Added user detials given below","payload": result},200)
            else:
                return make_response({"massage":"nothing to add"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

        
    def get_users(self,id):
        try:
            self.cur.execute(f"select * from users_view where id={id}")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"massage":"data not found"},204) 
            else:
                return make_response({"status":"successfull","payload":result},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)


    def delet_user(self,id):
        try:
            self.cur.execute(f"delete from users where id={id}")
            if self.cur.rowcount>0:
                return make_response({"status":"successfull","massage":"Deleted successfully"},200)
            else:
                return make_response({"massage":"nothing to delet"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)


    def getallusers_model(self):
        try:
            self.cur.execute("select * from users_view")
            result=self.cur.fetchall()
            if len(result)==0:
                return make_response({"massage":"data not found"},204) 
            else:
                return make_response({"status":"successfull","payload":result},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)

    def update_user(self,data,idoffilter):
        try:
            self.cur.execute(f"update users set full_name = '{data['full_name']}',email = '{data['email']}',phone = '{data['phone']}',age = '{data['age']}',salary = '{data['salary']}',city = '{data['city']}' where id = {idoffilter}")
            if self.cur.rowcount>0:
                return make_response({"updated successfully"},200)
            else:
                return make_response({"massage":"nothing to update"},200)
        except Exception as e:
            return make_response({"status":"Error","massage":str(e)},500)





        

    """ 
    1. select * from users
    2. select * from users where city='<city_name>'
    3. select * from users where age>=18
    4. select * from users where age>18 and age<35
    5. select * from users where email like '%gmail%'
    6. delet from users where id=11 
    7. update users set age=36, email=xy.ab@ya.com where id=11

    """
    

    def citywise_users_model(self,citynametofilter):
        self.cur.execute(f"select * from users_view where city='{citynametofilter}'")
        result=self.cur.fetchall()
        return make_response({"status":"Citywise user details are as follows","payload":result},200)

    def user_age(self):
        self.cur.execute(f"select * from users_view where age>=18")
        result=self.cur.fetchall()
        return make_response({"status":"Agewise user details are as follows","payload":result},200)

    def age_range(self,age1,age2):
        self.cur.execute(f"select * from users where age>={age1} and age<={age2}")
        result=self.cur.fetchall()
        return make_response({"status":"Agerangewise user details displayed between"'{age1}'"and" '{age2}',"payload":result},200)

    def user_email(self):
        self.cur.execute(f"select * from users_view where email like N'%gmail%'")
        result=self.cur.fetchall()
        return str(result)

    def find_emailwise_user_list(self,email):
        self.cur.execute(f"select * from users_view where email like '%{email}%'")
        result=self.cur.fetchall()
        return make_response({"status":"Requested Email user details displaye"'{eamil}',"payload":result},200)

    def order_user(self,method):
        self.cur.execute(f"SELECT * FROM users_view ORDER BY id {method}")
        result=self.cur.fetchall()
        return make_response({"status":"successfull","massage":"Sorted successfully"},200)

    def distinct_user(self,coloumname):
        self.cur.execute(f"SELECT distinct {coloumname} from users_view")
        result=self.cur.fetchall()
        return make_response({"status":"successfull","massage":"Requested coloum details displayed"},200)
