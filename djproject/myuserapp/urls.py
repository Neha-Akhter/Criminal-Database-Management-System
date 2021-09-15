"""myuserapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("", views.index),
    path("complain_Rec", views.complain_Rec),
    path("ad_123_3360", views.ad_123_3360),
    path("api-auth/", include("rest_framework.urls")),
    path("login_user", views.login_user),
    path("adminhome", views.adminhome),
    path("", include("django.contrib.auth.urls")),
    path("delete/<int:id>/", views.delete),
    path("update/<int:id>/", views.update),
    path("addrecord", views.addrecord),
    path("suspect_records", views.suspect_records),
    path("workforce", views.workforce),
    path("criminals", views.criminals),
    path("logoutuser", views.logoutuser),
    path("addcase", views.addcase),
    path("addofficer", views.addofficer),
    path("addsuspect", views.addsuspect),
    path("cases", views.cases),
    path("prisoners", views.prisoners),
    path("deletecase/<int:id>/", views.deletecase),
    path("delete_criminal/<int:id>/", views.delete_criminal),
    path("updatecase/<int:id>/", views.updatecase),
    path("addcriminal", views.addcriminal),
    path("complainrecords_csv", views.complainrecords_csv),
    path("update_criminal/<int:id>/", views.update_criminal),
    path("updateofficer/<str:id>/", views.updateofficer),
    path("updatesuspect/<str:id>/", views.updatesuspect),
    path("deletesuspect/<str:id>/", views.deletesuspect),
    path("deleteofficer/<int:id>/", views.deleteofficer),
    path("delete_prisoner/<int:id>/", views.delete_prisoner),
    path("complainrecords_csv", views.complainrecords_csv),
    path("workforce_csv", views.workforce_csv),
    path("cases_csv", views.cases_csv),
    path("suspects_csv", views.suspects_csv),
    path("criminals_csv", views.criminals_csv),
    path("update_prisoner/<int:id>/", views.update_prisoner),
    path("designations", views.designations),
    path("add_desig", views.add_desig),
    path("update_desg/<str:id>/", views.update_desg),
    path("delete_desig/<str:id>/", views.delete_desig),
    path("designations_csv", views.designations_csv),
    path("prisoners_csv", views.prisoners_csv),
    path("addprisoner", views.addprisoner),
]
