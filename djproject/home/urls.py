from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from home import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("complain_Rec", views.complain_Rec, name="complain_Rec"),
    path("ad_123_3360", views.ad_123_3360, name="nead_123_3360"),
    path("/login_user", views.login_user, name="login_user"),
    path("adminhome", views.adminhome, name="adminhome"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("update/<int:id>/", views.update, name="update"),
    path("addrecord", views.addrecord, name="addrecord"),
    path("suspect_records", views.suspect_records, name="suspect_records"),
    path("workforce", views.workforce, name="workforce"),
    path("criminals", views.criminals, name="criminals"),
    path("prisoners", views.prisoners, name="prisoners"),
    path("designations", views.designations, name="designations"),
    path("logoutuser", views.logoutuser, name="logoutuser"),
    path("addcase", views.addcase, name="addcase"),
    path("addofficer", views.addofficer, name="addofficer"),
    path("addsuspect", views.addsuspect, name="addsuspect"),
    path("cases", views.cases, name="cases"),
    path("deletecase/<int:id>/", views.deletecase, name="deletecase"),
    path("delete_criminal/<int:id>/", views.delete_criminal, name="delete_criminal"),
    path("deleteofficer/<int:id>/", views.deleteofficer, name="deleteofficer"),
    path("updatecase/<int:id>/", views.updatecase, name="updatecase"),
    path("addcriminal", views.addcriminal, name="addcriminal"),
    path("update_criminal/<int:id>/", views.update_criminal, name="update_criminal"),
    path("updateofficer/<int:id>/", views.updateofficer, name="updateofficer"),
    path("update_prisoner/<int:id>/", views.update_prisoner, name="update_prisoner"),
    path("updatesuspect/<str:id>/", views.updatesuspect, name="updatesuspect"),
    path("deletesuspect/<str:id>/", views.deletesuspect, name="deletesuspect"),
    path("delete_prisoner/<int:id>/", views.delete_prisoner, name="delete_prisoner"),
    path("cases_csv", views.cases_csv, name="cases_csv"),
    path("complainrecords_csv", views.complainrecords_csv, name="complainrecords_csv"),
    path("workforce_csv", views.workforce_csv, name="workforce_csv"),
    path("suspects_csv", views.suspects_csv, name="suspects_csv"),
    path("criminals_csv", views.criminals_csv, name="criminals_csv"),
    path("add_desig", views.add_desig, name="add_desig"),
    path("update_desg/<str:id>/", views.update_desg, name="update_desg"),
    path("designations_csv", views.designations_csv, name="designations_csv"),
    path("prisoners_csv", views.prisoners_csv, name="prisoners_csv"),
    path("addprisoner", views.addprisoner, name="addprisoner"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
