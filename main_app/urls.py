from django.contrib import admin
from django.urls import path, include
from . import views

# Here, I created the urls of the different pages
urlpatterns = [
    path('', views.home, name="home"),
    path('userhome', views.userhome, name="userhome"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('bug_list', views.bug_list, name="bug_list"),
    path('bugdetails/<bug_id>', views.bug_viewer, name="bugdetails"),
    path('bugform', views.bug_form, name="bugform"),
    path('updatebug/<bug_id>', views.upadte_bug, name="upadtebug"),
    path('deletebug/<bug_id>', views.delete_bug, name="deletebug"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
