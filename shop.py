from flask import *

from database import *

shopp=Blueprint('shop',__name__)

@shopp.route('/shophome')
def shophome():
    return render_template('shophome.html')

@shopp.route('/staffregistration',methods=['get','post'])
def staffregistration():
    if 'submit' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        desigination=request.form['desigination']
        username=request.form['username']
        password=request.form['password']
        ts="insert into login values(null,'%s','%s','staff')"%(username,password)
        c=insert(ts)
        svj="insert into tbl_staff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(c,firstname,lastname,place,phone,email,desigination)
        insert(svj)
    return render_template('shopmanagestaff.html')

@shopp.route('/shopviewclothtype',methods=['get','post'])
def shopviewclothtype():
    data={}

    ku="select * from tbl_clothtype"
    data['clothtype']=select(ku)

    return render_template('shopviewclothtype.html',data=data)

@shopp.route('/shopsendcomplaint',methods=['get','post'])
def shopsendcomplaint():
    data={}
    if 'submit' in request.form:
        complaint=request.form['complaint']
        date=request.form['date']
        bo="insert into tbl_complaint values(null,'%s','%s','pending','%s')"%(session['login_id'],complaint,date)
        insert(bo)
        return redirect(url_for('shop.shopsendcomplaint'))

    mr="select * from tbl_complaint where login_id='%s'"%(session['login_id'])
    data['complaint']=select(mr)

    return render_template('shopsendcomplaint.html',data=data)

@shopp.route('/shopaddmyservice',methods=['get','post'])
def shopaddmyservice():
    data={}
    if 'submit' in request.form:
        service=request.form['service']
        fr="insert into tbl_addservice values(null,'%s','%s')"%(session['shop_id'],service)
        insert(fr)
        return redirect(url_for('shop.shopaddmyservice'))

    kun="select * from tbl_service"
    data['service']=select(kun)

    return render_template('shopaddmyservice.html',data=data)

@shopp.route('/shopviewbookings',methods=['get','post'])
def shopviewbookings():
    data={}

    ai="SELECT *,`tbl_bookingmaster`.status AS statuss FROM `tbl_bookingmaster` INNER JOIN `tbl_bookingchild` USING (`bookingmaster_id`) INNER JOIN `tbl_service` USING (`service_id`)INNER JOIN `tbl_clothtype` USING(`clothtype_id`) INNER JOIN `tbl_shop` USING (`shop_id`)  WHERE shop_id='%s'"%(session['shop_id'])
    data['viewbookedservice']=select(ai)


    return render_template('shopviewbookings.html',data=data)

@shopp.route('/shopviewpayment',methods=['get','post'])
def shopviewpayment():
    data={}

    bookingmasterid=request.args['bookingmasterid']

    dd="select * from tbl_payment where bookingmaster_id='%s'"%(bookingmasterid)
    data['adminviewpayment']=select(dd)

    return render_template('shopviewpayment.html',data=data)

@shopp.route('/shopviewuserdetails',methods=['get','post'])
def shopviewuserdetails():
    data={}

    bookingmasterid=request.args['bookingmasterid']

    th="SELECT * FROM `tbl_bookingmaster` INNER JOIN `tbl_user` USING(`user_id`) where bookingmaster_id='%s'"%(bookingmasterid)
    data['adminviewuserdetails']=select(th)

    return render_template('shopviewuserdetails.html',data=data)

@shopp.route('/shopassignbooking',methods=['get','post'])
def shopassignbooking():
    data={}
    bookingmasterid=request.args['bookingmasterid']

    if 'submit' in request.form:
        staffid=request.form['staff']
        date=request.form['date']

        gg="insert into tbl_assign values(null,'%s','%s','%s')"%(bookingmasterid,staffid,date)
        insert(gg)
        hh="update tbl_bookingmaster set status='assigned' where bookingmaster_id='%s'"%(bookingmasterid)
        update(hh)

    tid="select * from tbl_staff"
    data['viewstaff']=select(tid)

    return render_template('shopassignbooking.html',data=data)