from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import emp,gym_admin,gym_member,plan1,booking,equipment,trainer1,Enquiry

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
        return render(request,"admindashboard.html",{})
    else:
        return HttpResponse("sorry")  

def memberlogin(request):
    return render(request,"memberlogin.html",{})

def admindashboard(request):
    return render(request,"admindashboard.html",{})

def adminmember(request):
    return render(request,"adminmember.html",{})

def adminaddmember(request):
    return render(request,"adminaddmember.html",{})

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

    return HttpResponse("Plan Saved Successfully")

def admintrainers(request):
    return render(request,"admintrainers.html",{})

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

    return HttpResponse("Plan Saved Successfully")

def adminpayment(request):
    return render(request,"adminpayment.html",{})

def adminrecordpayment(request):
    return render(request,"adminrecordpayment.html",{})

def adminattendance(request):
    return render(request,"adminattendance.html",{})

def adminmarkattendance(request):
    return render(request,"adminmarkattendance.html",{})

def adminequipment(request):
    return render(request,"adminequipment.html",{})

def adminaddequipment(request):
    return render(request,"adminaddequipment.html",{})

def adminenquiries(request):
    return render(request,"adminenquiries.html",{})

def adminworkoutplans(request):
    return render(request,"adminworkoutplans.html",{})

def adminaddworkoutplans(request):
    return render(request,"adminaddworkoutplans.html",{})

def adminfeedback(request):
    return render(request,"adminfeedback.html",{})

def memberdashboard(request):
    return render(request,"memberdashboard.html",{})

def memberprofile(request):
    return render(request,"memberprofile.html",{})

def memberchangepassword(request):
    return render(request,"memberchangepassword.html",{})
