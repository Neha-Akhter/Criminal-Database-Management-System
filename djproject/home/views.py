from django.contrib import auth
from django.db.models.fields import BooleanField
from django.http import response, HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime, date
import time
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import (
    CasesRecord,
    ComplainReg,
    Work_force,
    CriminalRecord,
    SuspectRecord,
    Designations,
    PrisonerRecord,
)
from .forms import (
    complainform,
    caseform,
    criminalform,
    desigform,
    prisonerform,
    suspectform,
    workforceform,
)
from django.contrib.auth.decorators import login_required
import datetime
import xlwt, csv


# Create your views here.


def index(request):

    if request.method == "POST":
        current_time = time.strftime("%H:%M:%S", time.localtime())
        complainee_fname = request.POST.get("complainee_fname")
        complainee_lname = request.POST.get("complainee_lname")
        complainee_cnic = request.POST.get("complainee_cnic")
        email_address = request.POST.get("email_address")
        complainee_contactno = request.POST.get("complainee_contactno")
        victim_description = request.POST.get("victim_description")
        crime_description = request.POST.get("crime_description")
        m = "0123456789"

        for i in range(len(complainee_contactno)):
            if complainee_contactno[i] not in m:
                messages.success(request, "invalid phone number")
                return redirect("/")

        complain = ComplainReg(
            complainee_fname=complainee_fname,
            email_address=email_address,
            complainee_lname=complainee_lname,
            complainee_cnic=complainee_cnic,
            complainee_contactno=complainee_contactno,
            timeofcomplain=time.strftime("%H:%M:%S", time.localtime()),
            dateofcomplain=date.today(),
            crime_description=crime_description,
            victim_description=victim_description,
        )

        complain.save()
        messages.success(request, "Your complain has been registered")

        redirect("/")

    return render(request, "index1.html")


@login_required(login_url="/login_user")
def complain_Rec(request):
    data = ComplainReg.objects.all()

    return render(request, "complainrecords.html", {"complains": data})


def adminhome(request):
    if not request.user.is_authenticated:
        return HttpResponse("error 404 you can't access this page")
    return render(request, "adminhomepage.html")


def ad_123_3360(request):
    return render(request, "login.html")


@login_required(login_url="/login_user")
def cases(request):
    case = CasesRecord.objects.all()

    return render(request, "casesrecord.html", {"cases": case})


@login_required(login_url="/login_user")
def suspect_records(request):
    suspect = SuspectRecord.objects.all()
    return render(request, "suspects.html", {"suspects": suspect})


@login_required(login_url="/login_user")
def criminals(request):
    c = CriminalRecord.objects.all()
    return render(request, "criminals.html", {"criminals": c})


@login_required(login_url="/login_user")
def workforce(request):
    people = Work_force.objects.all()
    return render(request, "workforce.html", {"officers": people})


@login_required(login_url="/login_user")
def prisoners(request):
    p = PrisonerRecord.objects.all()
    return render(request, "prisoners.html", {"prisoners": p})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("/ad_123_3360")


def login_user(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")

        user = authenticate(username=uname, password=passw)

        if user is not None:
            login(request, user)
            time.sleep(2)

            return render(request, "adminhomepage.html")

        else:
            messages.error(request, "Access Denied")
            return redirect("/ad_123_3360")

    return HttpResponse("error 404 not found")


@login_required(login_url="/login_user")
def delete(request, id):

    pi = ComplainReg.objects.get(pk=id)
    pi.delete()
    time.sleep(3)
    return redirect("/complain_Rec")


@login_required(login_url="/login_user")
def update(request, id):

    c = ComplainReg.objects.get(pk=id)

    form = complainform(instance=c)
    if request.method == "POST":
        form = complainform(request.POST, instance=c)
        if form.is_valid():

            form.save()

            return redirect("/complain_Rec")

    if c.FIR_status == 0:
        m = True
    else:
        m = False

    context = {"form": form, "val": m}

    return render(request, "update.html", context)


@login_required(login_url="/login_user")
def addrecord(request):
    if request.method == "POST":
        current_time = time.strftime("%H:%M:%S", time.localtime())
        complainee_fname = request.POST.get("complainee_fname")
        complainee_lname = request.POST.get("complainee_lname")
        complainee_cnic = request.POST.get("complainee_cnic")
        email_address = request.POST.get("email_address")
        complainee_contactno = request.POST.get("complainee_contactno")
        victim_description = request.POST.get("victim_description")
        crime_description = request.POST.get("crime_description")
        m = "0123456789"

        for i in range(len(complainee_contactno)):
            if complainee_contactno[i] not in m:
                messages.success(request, "invalid phone number")
                return redirect("/")

        complain = ComplainReg(
            complainee_fname=complainee_fname,
            email_address=email_address,
            complainee_lname=complainee_lname,
            complainee_cnic=complainee_cnic,
            complainee_contactno=complainee_contactno,
            timeofcomplain=time.strftime("%H:%M:%S", time.localtime()),
            dateofcomplain=date.today(),
            crime_description=crime_description,
            victim_description=victim_description,
        )
        print(complain)
        complain.save()
        return redirect("/complain_Rec")

    return redirect("/complain_Rec")


@login_required(login_url="/login_user")
def addcase(request):

    if request.method == "POST":
        complainId = request.POST.get("complain_id")
        CrimeScene = request.POST.get("CrimeScene")
        officer = request.POST.get("officer")
        CaseStatus = request.POST.get("CaseStatus")
        Evidence = request.POST.get("Evidence")

        caseid = [
            (int(record.complain_id))
            for record in ComplainReg.objects.filter(FIR_status=1)
        ]

        officerid = [(offid.officer) for offid in Work_force.objects.all()]

        for i in caseid:
            if i == int(complainId):
                complainid = i
                break
        else:
            return redirect("/cases")

        com = [int(i.complain_id_id) for i in CasesRecord.objects.all()]
        if int(complainId) in com:
            messages.error(request, "Case Already registered against this complain")
            return redirect("/cases")

        for id in officerid:
            if id == int(officer):
                offid = id
                break
        else:
            messages.error(request, "No Officer Found, enter valid officer-ID")
            return redirect("/cases")

        if int(CaseStatus) > 1 or int(CaseStatus) < 0:
            messages.error(request, "unable to register the case")
            return redirect("/cases")

        caserec = CasesRecord(
            complain_id=ComplainReg(int(complainid)),
            officer=Work_force(int(offid)),
            CrimeScene=CrimeScene,
            CaseStatus=bool(CaseStatus),
            Evidence=Evidence,
        )

        caserec.save()
        return redirect("/cases")


@login_required(login_url="/login_user")
def deletecase(request, id):

    pi = CasesRecord.objects.get(pk=id)
    m = int(pi.complain_id_id)
    fir = ComplainReg.objects.get(pk=m)
    fir.FIR_status = 0
    fir.save()
    pi.delete()
    time.sleep(2)
    return redirect("/cases")


@login_required(login_url="/login_user")
def updatecase(request, id):

    c = CasesRecord.objects.get(pk=id)
    form = caseform(instance=c)

    if request.method == "POST":
        form = caseform(request.POST, instance=c)
        # print("on this line")
        # print(form["complain_id"].value())

        if form.is_valid():
            form.save()

            return redirect("/cases")

        else:
            return redirect("/cases")
    context = {"form": form}
    return render(request, "updaterecord.html", context)


@login_required(login_url="/login_user")
def criminals(request):
    criminals = CriminalRecord.objects.all()
    return render(request, "criminals.html", {"criminals": criminals})


@login_required(login_url="/login_user")
def delete_criminal(request, id):
    pi = CriminalRecord.objects.get(pk=id)
    pi.delete()
    time.sleep(3)
    return redirect("/criminals")


@login_required(login_url="/login_user")
def addcriminal(request):
    if request.method == "POST":
        criminal_ID = request.POST.get("criminal_ID")
        CNIC = request.POST.get("CNIC")
        case_id = request.POST.get("case_id")
        Sentence = request.POST.get("Sentence")
        CaptureStatus = request.POST.get("CaptureStatus")

        caseid = [(cid.case_id) for cid in CasesRecord.objects.all()]
        suspect_nic = [(snic.CNIC) for snic in SuspectRecord.objects.all()]

        for i in caseid:
            if int(i) == int(case_id):

                break
        else:
            return redirect("/criminals")

        for j in suspect_nic:
            if CNIC == j:
                break
        else:
            messages.error(request, "Invalid cnic number, Try again")
            return redirect("/criminals")

        criminalrec = CriminalRecord(
            # criminal_Id=criminal_ID
            CNIC=SuspectRecord(CNIC),
            case_id=CasesRecord(case_id),
            Sentence=Sentence,
            CaptureStatus=CaptureStatus,
        )
        criminalrec.save()
        return redirect("/criminals")
    return redirect("/criminals")


@login_required(login_url="/login_user")
def update_criminal(request, id):
    c = CriminalRecord.objects.get(pk=id)
    form = criminalform(instance=c)
    if request.method == "POST":
        form = criminalform(request.POST, instance=c)

        if form.is_valid():
            form.save()

            return redirect("/criminals")

        else:
            m = "Invalid updation"
            context = {"error": m}
            return redirect("/criminals")
    context = {"form": form}
    return render(request, "updaterecord.html", context)


@login_required(login_url="/login_user")
def addsuspect(request):
    if request.method == "POST":

        fname = request.POST.get("suspectlFname")
        lname = request.POST.get("suspectLname")
        bg = request.POST.get("BloodGroup")
        height = request.POST.get("Height")
        dob = request.POST.get("suspect_DOB")
        education = request.POST.get("Education")
        marital = request.POST.get("MaritalStatus")
        address = request.POST.get("address")
        cnic = request.POST.get("CNIC")

        cids = [str(cid.CNIC) for cid in SuspectRecord.objects.all()]

        if str(cnic) not in cids:

            sp = SuspectRecord(
                suspectlFname=fname,
                suspectLname=lname,
                BloodGroup=bg,
                Height=height,
                suspect_DOB=dob,
                MaritalStatus=marital,
                address=address,
                Education=education,
                CNIC=cnic,
            )
            sp.save()
            return redirect("/suspect_records")
        else:
            messages.error(request, "An unknown error occured!, Try again")
            return redirect("/suspect_records")

    return redirect("/suspect_records")


@login_required(login_url="/login_user")
def deletesuspect(request, id):
    pi = SuspectRecord.objects.get(pk=id)
    pi.delete()
    time.sleep(3)
    return redirect("/suspect_records")


@login_required(login_url="/login_user")
def addofficer(request):
    if request.method == "POST":
        fname = request.POST.get("Officerfname")
        lname = request.POST.get("Officerlname")
        dob = request.POST.get("Officer_DOB")
        doj = request.POST.get("Officer_DOJ")
        education = request.POST.get("Officer_Education")
        email = request.POST.get("Officer_email")
        marital = request.POST.get("MaritalStatus")
        taddress = request.POST.get("Temp_address")
        paddress = request.POST.get("Permanent_address")
        pno = request.POST.get("Officer_phoneNo")
        cell = request.POST.get("Officer_cellNo")
        postingno = request.POST.get("PostingNo")
        rank = request.POST.get("Ranking_id")
        cnic = request.POST.get("Officer_CNIC")

    off_cnic = [str(cn.Officer_CNIC) for cn in Work_force.objects.all()]
    ranks = [int(i.Ranking) for i in Designations.objects.all()]

    if (cnic in off_cnic) or (int(rank) not in ranks):
        messages.error(request, "Invalid CNIC or Rank")
        return redirect("/workforce")
    else:
        officer = Work_force(
            Officerfname=fname,
            Officerlname=lname,
            Officer_DOJ=doj,
            Officer_DOB=dob,
            MaritalStatus=marital,
            Officer_phoneNo=pno,
            Officer_cellNo=cell,
            PostingNo=postingno,
            Officer_Education=education,
            Ranking_id=rank,
            Officer_CNIC=cnic,
            Officer_email=email,
            Temp_address=taddress,
            Permanent_address=paddress,
        )
        officer.save()
        return redirect("/workforce")


@login_required(login_url="/login_user")
def deleteofficer(request, id):
    pi = Work_force.objects.get(pk=id)
    pi.delete()
    time.sleep(3)
    return redirect("/workforce")


@login_required(login_url="/login_user")
def updateofficer(request, id):
    c = Work_force.objects.get(pk=id)
    form = workforceform(instance=c)
    if request.method == "POST":
        form = workforceform(request.POST, instance=c)

        if form.is_valid():
            form.save()

            return redirect("/workforce")

        else:
            return redirect("/workforce")
    context = {"form": form}
    return render(request, "updaterecord.html", context)


@login_required(login_url="/login_user")
def updatesuspect(request, id):
    c = SuspectRecord.objects.get(pk=id)
    form = suspectform(instance=c)
    if request.method == "POST":
        form = suspectform(request.POST, instance=c)
        print("\nhelloooo", form["CNIC"].value())

        if form.is_valid():
            form.save()

            return redirect("/suspect_records")

        else:
            return redirect("/suspect_records")
    context = {"form": form}
    return render(request, "updaterecord.html", context)


@login_required(login_url="/login_user")
def complainrecords_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=Complainrecords" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("ComplainReg")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = (
        "complain_id",
        "complainee_fname",
        "complainee_lname",
        "complainee_cnic",
        "Contact No",
        "email_address",
        "dateofcomplain",
        "timeofcomplain",
        "FIR_status",
        "crime_description",
        "Victim_description",
    )

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = ComplainReg.objects.all().values_list(
        "complain_id",
        "complainee_fname",
        "complainee_lname",
        "complainee_cnic",
        "complainee_contactno",
        "email_address",
        "dateofcomplain",
        "timeofcomplain",
        "FIR_status",
        "crime_description",
        "victim_description",
    )

    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def suspects_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=Suspects" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("SuspectRecord")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = (
        "CNIC",
        "Suspect First name",
        "Suspect Last name",
        "Date of birth",
        "Height",
        "Education",
        "BloodGroup",
        "Address",
        "Marital Status",
    )

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = SuspectRecord.objects.all().values_list(
        "CNIC",
        "suspectlFname",
        "suspectLname",
        "suspect_DOB",
        "Height",
        "Education",
        "BloodGroup",
        "address",
        "MaritalStatus",
    )
    print(rows)
    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def workforce_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=WORKFORCE_RECORDS" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Work_force")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = (
        "Officer Frist name",
        "Officer last name",
        "Date of birth",
        "Date of joining",
        "Education",
        "Email address",
        "Marital Status",
        "Temporary address",
        "Permanent address",
        "Officer phoneNo",
        "Officer cellNo",
        "PostingNo",
        "Ranking_id",
        "Officer-CNIC",
    )

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = Work_force.objects.all().values_list(
        "Officerfname",
        "Officerlname",
        "Officer_DOB",
        "Officer_DOJ",
        "Officer_Education",
        "Officer_email",
        "MaritalStatus",
        "Temp_address",
        "Permanent_address",
        "Officer_phoneNo",
        "Officer_cellNo",
        "PostingNo",
        "Ranking_id",
        "Officer_CNIC",
    )

    print(rows)
    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def criminals_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=CriminalRecords" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("CriminalRecord")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ("criminal_ID", "case_id", "CNIC", "Sentence", "CaptureStatus")

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = CriminalRecord.objects.all().values_list(
        "criminal_ID", "case_id", "CNIC", "Sentence", "CaptureStatus"
    )
    print(rows)
    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def cases_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=casesrecords" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("CasesRecord")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = (
        "case_id",
        "complain_id",
        "officer",
        "CrimeScene",
        "CaseStatus",
        "Evidence",
    )

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = CasesRecord.objects.all().values_list(
        "case_id", "complain_id", "officer", "CrimeScene", "CaseStatus", "Evidence"
    )
    print(rows)
    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def delete_prisoner(request, id):
    pi = PrisonerRecord.objects.get(pk=id)
    pi.delete()
    time.sleep(3)
    return redirect("/prisoners")


@login_required(login_url="/login_user")
def update_prisoner(request, id):
    c = PrisonerRecord.objects.get(pk=id)
    form = prisonerform(instance=c)
    if request.method == "POST":
        form = prisonerform(request.POST, instance=c)

        if form.is_valid():
            form.save()

            return redirect("/prisoners")

        else:
            return redirect("/prisoners")
    context = {"form": form}
    return render(request, "updaterecord.html", context)


@login_required(login_url="/login_user")
def prisoners_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=PrisonerRecords" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("PrisonerRecord")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = (
        "Prisoner_id",
        "criminal_ID",
        "DateOfTransfer",
        "TimeOftransfer",
        "JailClass",
        "TransferStatus",
    )

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = PrisonerRecord.objects.all().values_list(
        "Prisoner_id",
        "criminal_ID",
        "DateOfTransfer",
        "TimeOftransfer",
        "JailClass",
        "TransferStatus",
    )
    print(rows)
    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def designations(request):
    d = Designations.objects.all()
    return render(request, "designations.html", {"d": d})


@login_required(login_url="/login_user")
def update_desg(request, id):
    c = Designations.objects.get(pk=id)
    form = desigform(instance=c)
    if request.method == "POST":
        form = desigform(request.POST, instance=c)

        if form.is_valid():
            form.save()

            return redirect("/designations")

        else:
            return redirect("/designations")
    context = {"form": form}
    return render(request, "updaterecord.html", context)


@login_required(login_url="/login_user")
def delete_desig(request, id):
    pi = Designations.objects.get(pk=id)
    pi.delete()
    time.sleep(3)
    return redirect("/designations")


@login_required(login_url="/login_user")
def add_desig(request):
    r = Designations.objects.all()
    ranklist = []
    for i in r:
        ranklist.append(i.Ranking)
    print(ranklist)

    if request.method == "POST":
        rank = request.POST.get("Ranking")

        bs = request.POST.get("BasicSalary")
        d = request.POST.get("Designation")

        if int(rank) in ranklist:
            messages.error(request, "Record already present")
            return redirect("/designations")

        elif 0 < int(rank) < 23:
            d = Designations(Ranking=rank, Designation=d, BasicSalary=bs)
            d.save()
            return redirect("/designations")

        else:
            messages.error(request, "Invalid Data Entries, Try again")
            return redirect("/designations")

    return redirect("/designations")


@login_required(login_url="/login_user")
def designations_csv(request):

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = (
        "attachment; filename=Designations" + str(datetime.datetime.now()) + ".xls"
    )

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Designations")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = (
        "Ranking",
        "BasicSalary",
        "Designation",
    )

    for i in range(len(columns)):
        ws.write(row_num, i, columns[i], font_style)

    font_style = xlwt.XFStyle()
    rows = Designations.objects.all().values_list(
        "Ranking",
        "BasicSalary",
        "Designation",
    )
    for j in rows:
        row_num += 1
        for col in range(len(j)):
            ws.write(row_num, col, str(j[col]), font_style)

    wb.save(response)
    return response


@login_required(login_url="/login_user")
def addprisoner(request):
    if request.method == "POST":

        # Prisoner_id = request.POST.get("Prisoner_id")
        criminal_ID = request.POST.get("criminal_ID")
        DateOfTransfer = request.POST.get("DateOfTransfer")
        TimeOftransfer = request.POST.get("TimeOftransfer")
        JailClass = request.POST.get("JailClass")
        TransferStatus = request.POST.get("TransferStatus")

        criminalid = [(cid.criminal_ID) for cid in CriminalRecord.objects.all()]

        for i in criminalid:
            if int(i) == int(criminal_ID):
                break
        else:
            messages.error(request, "An unknown error occured!, Try again")
            return redirect("/prisoners")

        prisonerrec = PrisonerRecord(
            # Prisoner_id=Prisoner_id,
            criminal_ID=CriminalRecord(criminal_ID),
            DateOfTransfer=DateOfTransfer,
            TimeOftransfer=TimeOftransfer,
            JailClass=JailClass,
            TransferStatus=TransferStatus,
        )

        prisonerrec.save()
        return redirect("/prisoners")
    return redirect("/prisoners")
