from django.db import models


class emp(models.Model):
    eno=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    eemail=models.CharField(max_length=35)
    enum=models.CharField(max_length=15)
    eadd=models.CharField(max_length=100)

    def __str__(self):
        return str(self.eno)+" "+self.ename+" "+self.eemail+" "+self.enum+" "+self.eadd

#gym management system
class gym_admin(models.Model):
    aid=models.AutoField(primary_key=True)
    aname=models.CharField(max_length=50)
    apass=models.CharField(max_length=50)

    def __str__(self):
        return self.aid+" "+self.aname+" "+self.apass
    
class gym_member(models.Model):
    mid=models.AutoField(primary_key=True)
    mname=models.CharField(max_length=50)
    mpass=models.CharField(max_length=50)
    maddress=models.CharField(max_length=150)
    mgender=models.CharField(max_length=100)
    mage=models.CharField(max_length=20)
    mtime=models.CharField(max_length=10) 
    mmobile=models.CharField(max_length=15)

    def __str__(self):
        return self.mid+" "+self.mname+" "+self.mpass+" "+self.maddress+" "+self.mgender+" "+self.mage+" "+self.mtime+" "+self.mmobile
    
#class plan(models.Model):
#    pid=models.AutoField(primary_key=True)
#    pname=models.CharField(max_length=50)
#    pdes=models.CharField(max_length=200)
#    ptime=models.IntegerField(max_length=10) 
#    eid=models.CharField(max_length=50)
#    prent=models.IntegerField()

 #   def __str__(self):
  #      return str(self.pid)+" "+self.pname+" "+self.pdes+" "+str(self.prent)+" "+self.eid+" "+str(self.ptime)

class plan1(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pdes=models.CharField(max_length=200)  
    ptime=models.IntegerField() 
    eid=models.CharField(max_length=50)
    prent=models.IntegerField()

    def __str__(self):
        return str(self.pid)+" "+self.pname+" "+self.pdes+" "+str(self.prent)+" "+self.eid+" "+str(self.ptime) 
    
class booking(models.Model):
    bid=models.AutoField(primary_key=True)
    mid=models.CharField(max_length=50)
    pid=models.CharField(max_length=50)
    pdate=models.CharField(max_length=50)
    prent=models.IntegerField()
    pdes=models.CharField(max_length=200)
    tid=models.CharField(max_length=50)

    def __str__(self):
        return self.bid+" "+self.mid+" "+self.pid+" "+self.pdate+" "+str(self.prent)+" "+self.pdes+" "+self.tid
    
class equipment(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=50)
    edate=models.CharField(max_length=50)
    eunit=models.CharField(max_length=20)
    eprice=models.IntegerField()

    def __str__(self):
        return self.eid+" "+self.ename+" "+self.edate+" "+self.eunit+" "+str(self.eprice)
    
class trainer(models.Model):
    tid=models.AutoField(primary_key=True)
    tname=models.CharField(max_length=50)
    tdes=models.CharField(max_length=50)
    tmobile = models.CharField(max_length=15)
    ttime = models.CharField(max_length=10)

    def __str__(self):
        return self.tid+" "+self.tname+" "+self.tdes+" "+self.tmobile+" "+self.ttime
    
class trainer1(models.Model):
    tid=models.AutoField(primary_key=True)
    tname=models.CharField(max_length=50)
    tdes=models.CharField(max_length=50)
    tmobile = models.CharField(max_length=15)
    ttime = models.CharField(max_length=10)

    def __str__(self):
        return str(self.tid)+" "+self.tname+" "+self.tdes+" "+self.tmobile+" "+self.ttime
    
class Enquiry(models.Model):  
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    message = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    created = models.CharField(max_length=20)

    def __str__(self):
        return self.name+" "+self.email+" "+self.mobile+" "+self.message+" "+self.status+" "+self.created


class workoutplan(models.Model):
    wid=models.AutoField(primary_key=True)
    wname=models.CharField(max_length=50)
    wtitle=models.CharField(max_length=100)
    wdes=models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.wid)+" "+self.wname+" "+self.wtitle+" "+self.wdes

class workoutplan1(models.Model):
    wid=models.AutoField(primary_key=True)
    wname=models.CharField(max_length=50)
    wtitle=models.CharField(max_length=100)
    wdes=models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.wid)+" "+self.wname+" "+self.wtitle+" "+self.wdes

class attendance(models.Model):
    atid = models.AutoField(primary_key=True)
    mid = models.CharField(max_length=20)
    adate = models.CharField(max_length=30)
    atime = models.CharField(max_length=30)

    def __str__(self):
        return str(self.atid)+" "+self.mid+" "+self.adate+" "+self.atime
    
class feedback(models.Model):
    fid = models.AutoField(primary_key=True)   
    mid = models.CharField(max_length=20)
    fmessage = models.CharField(max_length=300)
    fdate = models.CharField(max_length=20)
    ftime = models.CharField(max_length=20)

    def __str__(self):
        return str(self.fid)+" "+self.mid+" "+self.fmessage+" "+self.fdate+" "+self.ftime