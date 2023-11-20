from flask import *
from database import *

stafff=Blueprint('staff',__name__)

@stafff.route('/staffhome')
def staffhome():
    return render_template('staffhome.html')

@stafff.route('/staffviewbookingassign',methods=['get','post'])
def staffviewbookingassign():
    data={}

    if 'pickedup' in request.args:
        pickedupbookingmasterid=request.args['pickedup']

        ju="update tbl_bookingmaster set status='pickedup' where bookingmaster_id='%s'"%(pickedupbookingmasterid)
        update(ju)
        return redirect(url_for('staff.staffviewbookingassign'))
    
    if 'processing' in request.args:
        pickedupbookingmasterid=request.args['processing']

        uj="update tbl_bookingmaster set status='processing' where bookingmaster_id='%s'"%(pickedupbookingmasterid)
        update(uj)
        return redirect(url_for('staff.staffviewbookingassign'))
    
    if 'delivered' in request.args:
        pickedupbookingmasterid=request.args['delivered']

        pa="update tbl_bookingmaster set status='delivered' where bookingmaster_id='%s'"%(pickedupbookingmasterid)
        update(pa)
        return redirect(url_for('staff.staffviewbookingassign'))
    
    kk="SELECT * FROM `tbl_assign` INNER JOIN `tbl_bookingmaster` USING(`bookingmaster_id`) INNER JOIN `tbl_user` USING(`user_id`) where staff_id='%s'"%(session['staff_id'])
    data['viewassignbooking']=select(kk)

    return render_template('staffviewbookingassign.html',data=data)