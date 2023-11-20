from flask import *
from database import *

publicc=Blueprint('publicc',__name__)

@publicc.route('/')
def home():
    return render_template('publichome.html')

@publicc.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        usernamee=request.form['username']
        passwordd=request.form['Password']
        fu="select * from login where username ='%s' and password='%s'"%(usernamee,passwordd)
        res=select(fu)
        if res:
            session['login_id']=res[0]['login_id']
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.adminhome'))
            elif res[0]['usertype']=='shop':
                gt="select * from tbl_shop where login_id='%s'"%(session['login_id'])
                tes=select(gt)
                if tes:
                    session['shop_id']=tes[0]['shop_id']
                return redirect(url_for('shop.shophome'))
            elif res[0]['usertype']=='user':
                pt="select * from tbl_user where login_id='%s'"%(session['login_id'])
                kis=select(pt)
                if kis:
                    session['user_id']=kis[0]['user_id']
                return redirect(url_for('user.userhome'))
            elif res[0]['usertype']=='staff':
                jt="select * from tbl_staff where login_id='%s'"%(session['login_id'])
                pis=select(jt)
                if pis:
                    session['staff_id']=pis[0]['staff_id']
                return redirect(url_for('staff.staffhome'))
        else:
            return '''<script>alert('invalid cridentials');window.location='/login';</script>'''            
    return render_template('login.html')   

@publicc.route('/shopregistration',methods=['get','post'])
def shopregistration():
    if 'submit' in request.form:
        shopname=request.form['shopname']
        address=request.form['address']
        pincode=request.form['pincode']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        f="insert into login values(null,'%s','%s','pending')"%(username,password)
        t=insert(f)
        s="insert into tbl_shop values(null,'%s','%s','%s','%s','%s','%s','pending')"%(t,shopname,address,pincode,phone,email)
        insert(s)
        return redirect(url_for('publicc.login'))
    return render_template('shopregistration.html')

@publicc.route('/userregistration',methods=['get','post'])
def userregistration():
    if 'submit' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        td="insert into login values(null,'%s','%s','user')"%(username,password)
        c=insert(td)
        sj="insert into tbl_user values(null,'%s','%s','%s','%s','%s','%s')"%(c,firstname,lastname,place,phone,email)
        insert(sj)
        return redirect(url_for('publicc.login'))
    return render_template('userregistration.html')