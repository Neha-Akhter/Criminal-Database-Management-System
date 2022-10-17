from django.db import models
from django.db.models.expressions import Value
from django.db.models.fields.related import ForeignKey
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value


# Create your models here.


class ComplainReg(models.Model):
    complain_id = models.AutoField(primary_key=True)
    complainee_fname = models.CharField(max_length=20)
    complainee_lname = models.CharField(max_length=20)
    dateofcomplain = models.DateField()
    timeofcomplain = models.TimeField()
    complainee_cnic = models.CharField(max_length=15)
    complainee_contactno = models.CharField(max_length=11)
    FIR_status = models.BooleanField(default=0)
    crime_description = models.TextField(max_length=200)
    victim_description = models.TextField(max_length=150)
    email_address = models.EmailField(max_length=25)


class Designations(models.Model):

    BasicSalary = models.IntegerField()
    Designation = models.CharField(max_length=30, unique=True)
    Ranking = models.IntegerField(primary_key=True)


class Work_force(models.Model):
    
    
    officer = models.AutoField(primary_key=True)
    Officerfname = models.CharField(max_length=20)
    Officerlname = models.CharField(max_length=20)
    Officer_CNIC = models.CharField(max_length=15, unique=True)
    Officer_email = models.CharField(max_length=25)
    Officer_cellNo = models.BigIntegerField()
    Officer_phoneNo = models.CharField(max_length=11)
    Officer_DOB = models.DateField()
    Officer_DOJ = models.DateField()
    Officer_Education = models.CharField(max_length=27)
    Temp_address = models.CharField(max_length=70)
    Permanent_address = models.CharField(max_length=70)
    MaritalStatus = models.CharField(max_length=10)
    PostingNo = models.IntegerField()
    Ranking = models.ForeignKey(Designations, on_delete=CASCADE)


class CasesRecord(models.Model):
    
    
    case_id = models.AutoField(primary_key=True)
    complain_id = models.OneToOneField(ComplainReg, on_delete=CASCADE)
    officer = models.ForeignKey(Work_force, on_delete=CASCADE, default=None)
    CrimeScene = models.CharField(max_length=50)
    Evidence = models.CharField(max_length=50)
    CaseStatus = models.BooleanField(default=0)


class SuspectRecord(models.Model):

    CNIC = models.CharField(primary_key=True, unique=True, max_length=15)

    suspectlFname = models.CharField(max_length=20)
    suspectLname = models.CharField(max_length=20)
    suspect_DOB = models.DateField(blank=True, null=False)
    Height = models.CharField(max_length=6)
    Education = models.CharField(max_length=20)
    BloodGroup = models.CharField(max_length=6)
    address = models.CharField(max_length=60)
    MaritalStatus = models.CharField(max_length=10)
    Picture = models.ImageField(blank=True)


class CriminalRecord(models.Model):
    

    criminal_ID = models.AutoField(primary_key=True)
    CNIC = models.ForeignKey(SuspectRecord, on_delete=CASCADE)
    case_id = ForeignKey(CasesRecord, on_delete=CASCADE)
    Sentence = models.CharField(max_length=25)
    CaptureStatus = models.BooleanField()


class PrisonerRecord(models.Model):
    
    
    Prisoner_id = models.AutoField(primary_key=True)
    criminal_ID = models.ForeignKey(CriminalRecord, on_delete=CASCADE)
    DateOfTransfer = models.DateField()
    TimeOftransfer = models.TimeField()
    JailClass = models.CharField(max_length=6)
    TransferStatus = models.BooleanField(default=0)
