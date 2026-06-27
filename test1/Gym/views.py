from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime, date
from datetime import date, timedelta
from django.db.models import Sum, Avg
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from datetime import datetime
# Create your views here.

from .models import emp,gym_admin,gym_member,plan1,booking,equipment,trainer1,Enquiry,workoutplan1,feedback,attendance

def show1(request):
    return HttpResponse("<h1> welcome to pooja computer </h1>")

def form1(request):
    return render(request,"form1.html",{})

def getform1(request):
    xname=request.GET['fullname']
    xemail=request.GET['email']
    xnumber=request.GET['number']
    xadd=request.GET['address']
    msg="<h1>your record"+"name:"+xname
    msg=msg+"<br>email:"+xemail
    msg=msg+"<br>number:"+xnumber
    msg=msg+"<br>address:"+xadd

    obj=emp()
    obj.ename=xname
    obj.eemail=xemail
    obj.enum=xnumber
    obj.eadd=xadd
    obj.save()

    return HttpResponse(msg+"Data save successfull")

def disp(request):
    obj=emp.objects.all()
    data="<li>"
    for i in obj:
        data+="<li>"+str(i.eno)+"-"+i.ename+"-"+i.eemail+"-"+i.enum+"-"+i.eadd
    return HttpResponse(data)


def home(request):
    return render(request,"home.html",{})

def adminlogin(request):
    return render(request,"adminlogin.html",{})

def adminlogin1(request):
    xname=request.GET['username']
    xpass=request.GET['password']
    obj=gym_admin.objects.filter(aname=xname,apass=xpass)
    if obj:
        return redirect("admindashboard")
    else:
        return HttpResponse("""<script> alert('Please Enter Correct Username or Password');window.location.href='/memberlogin/';</script>""")

def memberlogin(request):
    return render(request,"memberlogin.html",{})

def memberlogin1(request):

    uname = request.GET['username']
    upass = request.GET['password']

    obj = gym_member.objects.filter(mname=uname,mpass=upass)
    if obj:
        obj = gym_member.objects.get(mname=uname,mpass=upass)
        request.session['sid']=obj.mid
        request.session['sname']=obj.mname
        return HttpResponse("""<script> alert('login successfull');window.location.href='/memberdashboard/';</script>""")
    else:
        return HttpResponse("""<script> alert('Please Enter Correct Username or Password');window.location.href='/memberlogin/';</script>""")

def memberforgotpassword(request):

    if request.method == "POST":

        mname = request.POST.get('mname')
        mmobile = request.POST.get('mmobile')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        member = gym_member.objects.filter(
            mname=mname,
            mmobile=mmobile
        ).first()

        if member is None:
            return render(request, 'memberforgotpassword.html', {
                'msg': 'Member name or mobile number is wrong.',
                'type': 'danger'
            })

        elif new_password != confirm_password:
            return render(request, 'memberforgotpassword.html', {
                'msg': 'New password and confirm password do not match.',
                'type': 'warning'
            })

        else:
            member.mpass = new_password
            member.save()

            return render(request, 'memberforgotpassword.html', {
                'msg': 'Password reset successfully. Now you can login.',
                'type': 'success'
            })

    return render(request, 'memberforgotpassword.html')

def admindashboard(request):
    total_members = gym_member.objects.count()
    total_plans = plan1.objects.count()
    total_trainers = trainer1.objects.count()
    total_payments = booking.objects.count()
    total_equipment = equipment.objects.count()
    total_enquiries = Enquiry.objects.count()
    total_feedbacks = feedback.objects.count()
    total_workoutplans = workoutplan1.objects.count()

    total_income = booking.objects.aggregate(
        total=Sum('prent')
    )['total'] or 0

    return render(request, "admindashboard.html", {
        "total_members": total_members,
        "total_plans": total_plans,
        "total_trainers": total_trainers,
        "total_payments": total_payments,
        "total_equipment": total_equipment,
        "total_enquiries": total_enquiries,
        "total_feedbacks": total_feedbacks,
        "total_workoutplans": total_workoutplans,
        "total_income": total_income,
        "today_registrations": 0,
        "pending_enquiries": 0,
    })

def adminmember(request):
    adminmember = gym_member.objects.all()
    return render(request, "adminmember.html", {"members": adminmember})

def adminaddmember(request):
    pobj=plan1.objects.all()
    tobj=trainer1.objects.all()
    return render(request,"adminaddmember.html",{'pobj':pobj,'tobj':tobj})

def membersignup(request):
    pobj=plan1.objects.all()
    tobj=trainer1.objects.all()
    return render(request, "membersignup.html", {'pobj':pobj, 'tobj':tobj})


def addmember(request):
    xname = request.GET['username']
    xpass = request.GET['password']
    xadd = request.GET['address']
    xgen = request.GET['gender']
    xage = request.GET['age']
    xtime = request.GET['date']
    xmob = request.GET['mobile']

    if gym_member.objects.filter(mname=xname).exists():
        return HttpResponse("<h1>sorry duplicate name<br><a href='/memberlogin'>go back</a>")
    else:
        obj = gym_member()
        obj.mname = xname
        obj.mpass = xpass
        obj.maddress = xadd
        obj.mgender = xgen
        obj.mage = xage
        obj.mtime = xtime
        obj.mmobile = xmob
        obj.save()
        xno=obj.pk
        return HttpResponse(f"""<script> alert('Record save your id:{xno}');
                        window.location.href='/adminmember/'; </script>""")


from django.shortcuts import render, redirect

def admineditmember(request, id):
    obj = gym_member.objects.get(mid=id)

    return render(request, 'admineditmember.html', {
        'member': obj
    })


def update_member(request, id):
    obj = gym_member.objects.get(mid=id)

    obj.mname = request.GET.get('mname')
    obj.mpass = request.GET.get('mpass')
    obj.maddress = request.GET.get('maddress')
    obj.mgender = request.GET.get('mgender')
    obj.mage = request.GET.get('mage')
    obj.mtime = request.GET.get('mtime')
    obj.mmobile = request.GET.get('mmobile')

    obj.save()

    return redirect('/adminmember/')


def admindeletemember(request, id):
    obj = gym_member.objects.get(mid=id)
    obj.delete()

    return redirect('/adminmember/')

def adminplan(request):
    plans = plan1.objects.all()
    return render(request, "adminplan.html", {"planss": plans})


def adminaddplan(request):
    return render(request,"adminaddplan.html",{})

def addplan1(request):

    xpname = request.GET['pname']
    xpdes = request.GET['pdes']
    xptime = int(request.GET['ptime'])
    xprent = int(request.GET['prent'])

    obj = plan1()
    obj.pname = xpname
    obj.pdes = xpdes
    obj.ptime = xptime
    obj.prent = xprent

    obj.save()

    if obj:
        return HttpResponse("""<script> alert("Record save");window.location.href='/adminplan/';</script>""")
    else:
        return HttpResponse("""<script> alert("sorry something is wrong");window.location.href='/adminplan/';</script>""")

def admintrainers(request):
    admintrainer = trainer1.objects.all()
    return render(request, "admintrainers.html", {"trainers": admintrainer})

def adminaddtrainers(request):
    return render(request,"adminaddtrainers.html",{})

def addtrainer(request):
    xpname = request.GET['name']
    xmo = request.GET['mobile']
    xdes = request.GET['specialization']
    xtime = request.GET['shift_timing']

    obj = trainer1()
    obj.tname = xpname
    obj.tmobile = xmo
    obj.tdes = xdes
    obj.ttime = xtime

    obj.save()

    if obj:
        return HttpResponse("""<script> alert("Record save");window.location.href='/admintrainers/';</script>""")
    else:
        return HttpResponse("""<script> alert("sorry something is wrong");window.location.href='/admintrainers/';</script>""")

def adminpayment(request):
    bookings = booking.objects.all()

    mid = request.GET.get('mid')
    pid = request.GET.get('pid')

    if mid:
        bookings = bookings.filter(mid__icontains=mid)

    if pid:
        bookings = bookings.filter(pid__icontains=pid)

    total_income = bookings.aggregate(Sum('prent'))['prent__sum'] or 0
    total_bookings = bookings.count()
    average_income = bookings.aggregate(Avg('prent'))['prent__avg'] or 0
    total_trainers = bookings.values('tid').distinct().count()

    return render(request, 'adminpayment.html', {
        'bookings': bookings,
        'total_income': total_income,
        'total_bookings': total_bookings,
        'average_income': average_income,
        'total_trainers': total_trainers,
    })


def adminrecordpayment(request):
    return render(request,"adminrecordpayment.html",{})

def adminattendance(request):

    attendance_data = attendance.objects.all().order_by('-atid')
    members = gym_member.objects.all()

    selected_date = request.GET.get("date")
    selected_member = request.GET.get("member")

    if selected_date:
        attendance_data = attendance_data.filter(adate=selected_date)

    if selected_member:
        attendance_data = attendance_data.filter(mid=selected_member)

    return render(request, "adminattendance.html", {
        "attendance": attendance_data,
        "members": members,
        "selected_date": selected_date,
        "selected_member": selected_member,
    })

def adminmarkattendance(request):

    members = gym_member.objects.all()

    today = date.today()
    current_time = datetime.now().strftime("%H:%M")

    if request.method == "POST":

        mid = request.POST.get('member')
        adate = request.POST.get('date')
        atime = request.POST.get('time_in')

        if adate == "":
            adate = date.today().strftime("%Y-%m-%d")

        if atime == "":
            atime = datetime.now().strftime("%H:%M")

        obj = attendance()
        obj.mid = mid
        obj.adate = adate
        obj.atime = atime
        obj.save()

        return redirect('/adminattendance/')

    return render(request, 'adminmarkattendance.html', {
        'members': members,
        'today': today,
        'current_time': current_time
    })

def adminequipment(request):
    admintrainer = equipment.objects.all()

    total_items = admintrainer.count()
    total_units = 0
    total_investment = 0

    for i in admintrainer:
        unit = int(i.eunit)
        price = int(i.eprice)

        total_units += unit
        total_investment += unit * price

    return render(request, "adminequipment.html", {
        "equipments": admintrainer,
        "total_items": total_items,
        "total_units": total_units,
        "total_investment": total_investment,
    })

def adminaddequipment(request):
    return render(request,"adminaddequipment.html",{})

def addequipment(request):
    xpname = request.GET['ename']
    xunit = request.GET['units']
    xprice = request.GET['price']
    xdate = request.GET['purchase_date']

    obj = equipment()
    obj.ename = xpname
    obj.eunit = xunit
    obj.eprice = xprice
    obj.edate = xdate

    obj.save()

    if obj:
        return HttpResponse("""<script> alert("Record save");window.location.href='/adminequipment/';</script>""")
    else:
        return HttpResponse("""<script> alert("sorry something is wrong");window.location.href='/adminequipment/';</script>""")

def addenquiry(request):
    if request.method == "GET":
        obj = Enquiry()
        obj.name = request.GET.get('name')
        obj.email = request.GET.get('email')
        obj.mobile = request.GET.get('mobile')
        obj.message = request.GET.get('message')
        obj.status = "New"
        obj.created = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        obj.save()

    return redirect('/home/')
    
def adminenquiries(request):
    enquiries = Enquiry.objects.all().order_by('-id')

    return render(request,'adminenquiries.html',{'enquiries': enquiries})

def updateenquiry(request,id):

    if request.method == "POST":

        status = request.POST.get('status')

        obj = Enquiry.objects.get(id=id)
        obj.status = status
        obj.save()

    return redirect('/adminenquiries/')

def adminworkoutplans(request):

    members = gym_member.objects.all()

    member_name = request.GET.get('member')

    if member_name:
        adminworkoutplans = workoutplan1.objects.filter(wname=member_name)
    else:
        adminworkoutplans = workoutplan1.objects.all()

    return render(request, "adminworkoutplans.html", {
        "plans": adminworkoutplans,
        "members": members,
    })

def adminaddworkoutplans(request):
    members = gym_member.objects.all()
    return render(request, "adminaddworkoutplans.html", {"members": members})


def addworkoutplans(request):
    xname = request.GET['member']
    xtitle = request.GET['title']
    xdesc = request.GET['description']

    obj = workoutplan1()
    obj.wname = xname
    obj.wtitle = xtitle
    obj.wdes = xdesc
    obj.save()

    if obj:
        return HttpResponse("""<script> alert("Record save");window.location.href='/adminworkoutplans/';</script>""")
    else:
        return HttpResponse("""<script> alert("sorry something is wrong");window.location.href='/adminworkoutplans/';</script>""")

def adminfeedback(request):
    feedbacks = feedback.objects.all().order_by('-fid')

    mid = request.GET.get('mid')

    if mid:
        feedbacks = feedbacks.filter(mid__icontains=mid)

    return render(request, 'adminfeedback.html', {
        'feedbacks': feedbacks
    })

def memberdashboard(request):
    return render(request,"memberdashboard.html",{})

def membereditprofile(request):
    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    mid = request.session['sid']
    obj = gym_member.objects.get(mid=mid)

    return render(request, 'membereditprofile.html', {'obj': obj})

def updatememberprofile(request, mid):
    if request.method == "POST":
        obj = gym_member.objects.get(mid=mid)

        obj.mname = request.POST.get('mname')
        obj.mmobile = request.POST.get('mmobile')
        obj.mage = request.POST.get('mage')
        obj.mgender = request.POST.get('mgender')
        obj.mtime = request.POST.get('mtime')
        obj.mpass = request.POST.get('mpass')
        obj.maddress = request.POST.get('maddress')

        obj.save()

    return redirect('/memberprofile/')

def memberprofile(request):
    sid=int(request.session['sid'])
    obj=gym_member.objects.get(mid=sid)
    return render(request,"memberprofile.html",{'obj':obj})

def memberchangepassword(request):
    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    mid = request.session['sid']
    obj = gym_member.objects.get(mid=mid)

    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if obj.mpass != current_password:
            messages.error(request, "Current password is wrong.")
            return redirect('/memberchangepassword/')

        elif new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match.")
            return redirect('/memberchangepassword/')

        elif len(new_password) < 8:
            messages.warning(request, "Password should be at least 8 characters.")
            return redirect('/memberchangepassword/')

        else:
            obj.mpass = new_password
            obj.save()
            messages.success(request, "Password updated successfully.")
            return redirect('/memberchangepassword/')

    return render(request, 'memberchangepassword.html')

def membermembership(request):
    return render(request,"membermembership.html",{})

def memberattendance(request):

    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    mid = request.session['sid']

    attendance_data = attendance.objects.filter(mid=str(mid)).order_by('-atid')

    return render(request, 'memberattendance.html', {
        'attendance': attendance_data
    })
    
def memberpayment(request):

    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    mid = request.session['sid']

    books = booking.objects.filter(mid=str(mid)).order_by('-bid')

    payments = []

    for b in books:
        plan = plan1.objects.filter(pid=b.pid).first()

        payments.append({
            'bid': b.bid,
            'plan': plan.pname if plan else 'Plan Deleted',
            'amount': b.prent,
            'date': b.pdate,
            'mode': b.pdes.split(' - ')[0],
            'status': 'Paid',
            'notes': b.pdes,
        })

    return render(request, 'memberpayment.html', {'payments': payments})

def paymentreceipt(request, bid):
    b = booking.objects.get(bid=bid)
    plan = plan1.objects.filter(pid=b.pid).first()

    return render(request, 'paymentreceipt.html', {
        'b': b,
        'planname': plan.pname if plan else 'Plan Deleted'
    })

def membermembership(request):

    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    mid = request.session['sid']

    book = booking.objects.filter(mid=str(mid)).order_by('-bid').first()

    if book is None:
        return render(request, 'membermembership.html', {'membership': None})

    plan = plan1.objects.filter(pid=int(book.pid)).first()

    if plan is None:
        return render(request, 'membermembership.html', {'membership': None})

    trainer = None

    # Trainer from booking table
    if book.tid and str(book.tid).isdigit():
        trainer = trainer1.objects.filter(tid=int(book.tid)).first()

    # If not found, trainer from plan table
    if trainer is None and plan.eid and str(plan.eid).isdigit():
        trainer = trainer1.objects.filter(tid=int(plan.eid)).first()

    start_date = date.fromisoformat(book.pdate)
    end_date = start_date + timedelta(days=int(plan.ptime) * 30)

    days_remaining = (end_date - date.today()).days
    if days_remaining < 0:
        days_remaining = 0

    membership = {
        'plan_name': plan.pname,
        'duration': plan.ptime,
        'plan_fee': plan.prent,
        'total_paid': book.prent,
        'remaining_amount': int(plan.prent) - int(book.prent),
        'start_date': start_date,
        'end_date': end_date,
        'days_remaining': days_remaining,

        'trainer_name': trainer.tname if trainer else 'Not Assigned',
        'trainer_mobile': trainer.tmobile if trainer else 'Not Available',
        'trainer_time': trainer.ttime if trainer else 'Not Available',

        'plan_details': plan.pdes,
    }

    return render(request, 'membermembership.html', {'membership': membership})

def memberworkout(request):
    mid = request.session['sid']

    member = gym_member.objects.get(mid=mid)

    plans = workoutplan1.objects.filter(wname=member.mname)

    return render(request,'memberworkout.html',{
        'plans': plans
    })

def memberbooking(request):
    plans = plan1.objects.all()

    for p in plans:
        p.features = p.pdes.split(',')
    
    return render(request, "memberbooking.html", {
        "plans": plans
    })

def membertrainer(request):


    trainers = trainer1.objects.all()
    pid=request.GET['xpid']

    return render(request, 'membertrainer.html', {
        'trainers': trainers,'pid':pid
    })

def memberpay(request):

    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    pid = request.GET['pid']
    tid = request.GET['tid']

    plan = plan1.objects.get(pid=pid)
    trainer = trainer1.objects.get(tid=tid)

    payment = {
        'pid': plan.pid,
        'pname': plan.pname,
        'prent': plan.prent,
        'pdes': plan.pdes,
        'tid': trainer.tid,
        'tname': trainer.tname,
        'tmobile': trainer.tmobile,
        'ttime': trainer.ttime,
    }

    return render(request, 'memberpay.html', {
        'payment': payment
    })

def confirmpayment(request):

    if 'sid' not in request.session:
        return render(request, 'memberlogin.html')

    mid = request.session['sid']

    pid = request.GET.get('pid')
    tid = request.GET.get('trainer')
    amount = request.GET.get('amount')
    mode = request.GET.get('paymentmode')
    info = request.GET.get('paymentinfo', '')

    cardholder = request.GET.get('cardholder', '')
    expiry = request.GET.get('expiry', '')

    if not pid:
        return HttpResponse("<h2>Plan id missing</h2><a href='/membermembership/'>Go Back</a>")

    plan = plan1.objects.get(pid=pid)

    if mode == "Card":
        payinfo = "Card Payment - " + cardholder + " - " + expiry + " - " + info
    else:
        payinfo = mode + " - " + info

    obj = booking()
    obj.mid = str(mid)
    obj.pid = str(pid)
    obj.pdate = str(date.today())
    obj.prent = amount
    obj.pdes = payinfo
    obj.tid = str(tid)
    obj.save()

    return HttpResponse("""
    <script>
    alert('Payment Saved Successfully');
    window.location.href='/membermembership/';
    </script>
    """)

def memberfeedback(request):
    x = request.session.get('memberid')
    feedbacks = feedback.objects.filter(mid=x).order_by('-fid')

    return render(request, 'memberfeedback.html', {
        'feedbacks': feedbacks
    })


def addfeedback(request):
    x = request.session.get('sid')

    if request.method == "GET":
        msg = request.GET.get('fmessage')

        obj = feedback()
        obj.mid = x
        obj.fmessage = msg
        obj.fdate = datetime.now().strftime("%d-%m-%Y")
        obj.ftime = datetime.now().strftime("%I:%M %p")
        obj.save()

    return render(request,"memberfeedback.html",{})

def memberlogout(request):
    request.session.flush()      
    return redirect('/memberlogin/')

def adminlogout(request):
    request.session.pop("admin_id", None)
    return redirect("/adminlogin/")