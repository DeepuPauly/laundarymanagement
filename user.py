from flask import *

from database import *

userr=Blueprint('user',__name__)

@userr.route('/userhome')
def userhome():
    return render_template('userhome.html')

@userr.route('/usersendcomplaint',methods=['get','post'])
def usersendcomplaint():
    data={}
    if 'submit' in request.form:
        complaint=request.form['complaint']
        date=request.form['date']
        bo="insert into tbl_complaint values(null,'%s','%s','pending','%s')"%(session['login_id'],complaint,date)
        insert(bo)

    mr="select * from tbl_complaint where login_id='%s'"%(session['login_id'])
    data['complaint']=select(mr)

    return render_template('usersendcomplaint.html',data=data)

@userr.route('/userviewshop',methods=['get','post'])
def userviewshop():
    data={}
    om="select * from tbl_shop"
    data['viewshop']=select(om)

    return render_template('userviewshop.html',data=data)

@userr.route('/userviewservices',methods=['get','post'])
def userviewservices():
    data={}

    if 'shopid' in request.args:
        shopsid=request.args['shopid']
    else:
        action=None

    qq="SELECT * FROM `tbl_service` INNER JOIN `tbl_addservice` USING(`service_id`) WHERE `shop_id`='%s'"%(shopsid)
    print(qq)
    data['viewservices']=select(qq)

    return render_template('userviewservices.html',data=data)

@userr.route('/userbookservice',methods=['get','post'])
def userbookservice():
    data={}
    serviceid=request.args['serviceid']
    shopid=request.args['shopid']

    if 'submit' in request.form:
        amm=request.form['amount']
        clothid=request.form['clothtype']
        quantity=request.form['quantity']
        bmtotal=request.form['total']
        date=request.form['date']
        clothprice=request.form['clothprice']

        bookingchildamount=int(clothprice) + int(amm)

        pel="select * from tbl_bookingmaster where user_id='%s' and status='pending'"%(session['user_id'])
        lo=select(pel)
        if lo:
            bmid=lo[0]['bookingmaster_id']
            dt="update tbl_bookingmaster set ammount=ammount+'%s',status='pending' where bookingmaster_id='%s'"%(bmtotal,bmid)
            update(dt)
            sha="select * from tbl_bookingchild where bookingmaster_id='%s'"%(bmid)
            tha=select(sha)
            if tha:
                bcid=tha[0]['bookingchild_id']
                # ath="update tbl_bookingchild set quantity=quantity+'%s',rate='%s' where bookingchild_id='%s'"%(quantity,bookingchildamount,bcid)
                # update(ath)
            # else:
                xz="insert into tbl_bookingchild values(null,'%s','%s','%s','%s','%s','%s')"%(bmid,serviceid,clothid,shopid,bookingchildamount,quantity)
                insert(xz)
        else:
            abc="insert into tbl_bookingmaster values(null,'%s','%s','%s','pending')"%(session['user_id'],bmtotal,date)
            mun=insert(abc)
            efg="insert into tbl_bookingchild values(null,'%s','%s','%s','%s','%s','%s')"%(mun,serviceid,clothid,shopid,bookingchildamount,quantity)
            insert(efg)
            return redirect(url_for('user.userviewservicebooked'))

    pp="select * from tbl_service where service_id='%s'"%(serviceid)
    data['hu']=select(pp)
    dd="select * from tbl_clothtype"
    data['pe']=select(dd)
    
    return render_template('userbookservice.html',data=data)

@userr.route('/get_cloth_amount',methods=['post'])
def get_cloth_amount():
    id=request.form['cloth_type_id']
    qa="select * from tbl_clothtype where clothtype_id='%s'"%(id)
    res=select(qa)
    amt=res[0]['price']
    return jsonify({'amount':amt})

@userr.route('/userviewservicebooked',methods=['get','post'])
def userviewservicebooked():
    data={}

    if 'cancel' in request.args:
        bookingmasterid=request.args['cancel']

        ksh="update tbl_bookingmaster set status='cancel' where bookingmaster_id='%s'"%(bookingmasterid)
        update(ksh)

    ai="SELECT *,`tbl_bookingmaster`.status AS statuss FROM `tbl_bookingmaster` INNER JOIN `tbl_bookingchild` USING (`bookingmaster_id`) INNER JOIN `tbl_service` USING (`service_id`)INNER JOIN `tbl_clothtype` USING(`clothtype_id`) INNER JOIN `tbl_shop` USING (`shop_id`) WHERE user_id='%s'"%(session['user_id'])
    data['viewbookedservice']=select(ai)

    return render_template('userviewservicebooked.html',data=data)

@userr.route('/usermakepayment',methods=['get','post'])
def usermakepayment():
    data={}
    total=request.args['totalammount']
    bookingmasterid=request.args['bookingmasterid']

    por="select * from tbl_bookingmaster where bookingmaster_id='%s'"%(bookingmasterid)
    data['payment']=select(por)

    if 'submit' in request.form:
        kan="insert into tbl_payment values(null,'%s','%s',now())"%(bookingmasterid,total)
        insert(kan)
        fk="update tbl_bookingmaster set status='paid' where bookingmaster_id='%s'"%(bookingmasterid)
        update(fk)
        return redirect(url_for('user.userviewservicebooked'))

    return render_template('usermakepayment.html',data=data)

@userr.route('/userviewpickedupdetails',methods=['get','post'])
def userviewpickedupdetails():
    data={}
    bookingmasterid=request.args['bookingmasterid']

    gf="SELECT * FROM `tbl_bookingmaster` INNER JOIN `tbl_assign` USING(`bookingmaster_id`)  INNER JOIN `tbl_staff` USING(`staff_id`) WHERE `bookingmaster_id`='%s'"%(bookingmasterid)
    data['viewpickedupdetails']=select(gf)

    return render_template('userviewpickedupdetails.html',data=data)