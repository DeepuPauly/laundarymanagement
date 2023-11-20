from flask import *

from database import *

adminn=Blueprint('admin',__name__)

@adminn.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@adminn.route('/adminverifyshop',methods=['get','post'])
def adminverifyshop():
    data={}
    ee="select * from tbl_shop"
    data['verifyshop']=select(ee)
	
    if 'action' in request.args:
        action=request.args['action']
        login_id=request.args['login_id']
    else:
        action=None
    if action=='accept':
        q="update tbl_shop set status='accept' where login_id='%s'"%(login_id)
        update(q)
        u="update login set usertype='shop' where login_id='%s'"%(login_id) 
        update(u)
    if action=='reject':
        h="update tbl_shop set status='reject' where login_id='%s'"%(login_id)
        update(h)
        u="update login set usertype='block' where login_id='%s'"%(login_id) 
        update(u)

    return render_template('adminverifyshop.html',data=data)

@adminn.route('/adminmanageservice',methods=['get','post'])
def adminmanageservice():
    data={}
    if 'submit' in request.form:
        service=request.form['service'] 
        rate=request.form['rate']
        hq="insert into tbl_service values(null,'%s','%s')"%(service,rate)
        insert(hq)
        return redirect(url_for('admin.adminmanageservice'))
    
    if 'action' in request.args:
        action=request.args['action']
        usid=request.args['sid']
    else:
        action=None
    
    if action=='update':
        fu="select * from tbl_service where service_id='%s'"%(usid)
        data['updates']=select(fu)

    if 'update' in request.form:
        service=request.form['service'] 
        rate=request.form['rate']
        yy="update tbl_service set service='%s',rate='%s' where service_id='%s'"%(service,rate,usid)
        update(yy)
        return redirect(url_for('admin.adminmanageservice'))
    
    if action=='delete':
        pu="delete from tbl_service where service_id='%s'"%(usid)
        delete(pu)
        return redirect(url_for('admin.adminmanageservice'))

    dp="select * from tbl_service"
    data['services']=select(dp)
    return render_template('adminmanageservice.html',data=data)

@adminn.route('/adminmanagetypeofcloth',methods=['get','post'])
def adminmanagetypeofcloth():
    data={}
    if 'submit' in request.form:
        cloth=request.form['clothtype'] 
        rate=request.form['rate']
        hq="insert into tbl_clothtype values(null,'%s','%s')"%(cloth,rate)
        insert(hq)
        return redirect(url_for('admin.adminmanagetypeofcloth'))
    
    if 'action' in request.args:
        action=request.args['action']
        ucid=request.args['cid']
    else:
        action=None
    
    if action=='update':
        fu="select * from tbl_clothtype where clothtype_id='%s'"%(ucid)
        data['updates']=select(fu)

    if 'update' in request.form:
        cloth=request.form['clothtype'] 
        rate=request.form['rate']
        yy="update tbl_clothtype set clothtype='%s',price='%s' where clothtype_id='%s'"%(cloth,rate,ucid)
        update(yy)
        return redirect(url_for('admin.adminmanagetypeofcloth'))
    
    if action=='delete':
        pu="delete from tbl_clothtype where clothtype_id='%s'"%(ucid)
        delete(pu)
        return redirect(url_for('admin.adminmanagetypeofcloth'))
    
    ku="select * from tbl_clothtype"
    data['clothtype']=select(ku)

    return render_template('adminmanagetypeofcloths.html',data=data)

@adminn.route('/adminviewcomplaint',methods=['get','post'])
def adminviewcomplaint():
    data={}

    ko="select * from tbl_complaint"
    data['complaint']=select(ko)

    return render_template('adminviewcomplaints.html',data=data)

@adminn.route('/adminsendcomplaintreply',methods=['get','post'])
def adminsendcomplaintreply():
    data={}

    if 'complaint' in request.args:
        complaintid=request.args['complaint']
    else:
        action=None

    if 'submit' in request.form:
        reply=request.form['reply']
        po="update tbl_complaint set replay='%s' where complaint_id='%s'"%(reply,complaintid)
        update(po)
        return redirect(url_for('admin.adminviewcomplaint'))

    return render_template('adminsendcomplaintreply.html',data=data)

@adminn.route('/adminviewbookings',methods=['get','post'])
def adminviewbookings():
    data={}

    ai="SELECT *,`tbl_bookingmaster`.status AS statuss FROM `tbl_bookingmaster` INNER JOIN `tbl_bookingchild` USING (`bookingmaster_id`) INNER JOIN `tbl_service` USING (`service_id`)INNER JOIN `tbl_clothtype` USING(`clothtype_id`) INNER JOIN `tbl_shop` USING (`shop_id`)"
    data['viewbookedservice']=select(ai)


    return render_template('adminviewbookings.html',data=data)

@adminn.route('/adminviewpayment',methods=['get','post'])
def adminviewpayment():
    data={}

    bookingmasterid=request.args['bookingmasterid']

    dd="select * from tbl_payment where bookingmaster_id='%s'"%(bookingmasterid)
    data['adminviewpayment']=select(dd)

    return render_template('adminviewpayment.html',data=data)

@adminn.route('/adminviewuserdetails',methods=['get','post'])
def adminviewuserdetails():
    data={}

    bookingmasterid=request.args['bookingmasterid']

    th="SELECT * FROM `tbl_bookingmaster` INNER JOIN `tbl_user` USING(`user_id`) where bookingmaster_id='%s'"%(bookingmasterid)
    data['adminviewuserdetails']=select(th)

    return render_template('adminviewuserdetails.html',data=data)