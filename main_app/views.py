from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from bug_tracker import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . token import generate_token
from django.core.mail import EmailMessage, send_mail
from .models import Bug_Query
from .forms import BugQueryForm, BugSearchForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, "main_app/index.html")

def userhome(request):
    return render(request, "main_app/userpage.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('signup')
            
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        
        messages.success(request, "Your account has been sucessfully created. We have sent you a confirmation email, please confirm your email in order to activate your account.")
        
        # Welcome email
        
        subject = "Welcome to Bug Hive"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Bug Hive \nThankyou for being a part of us. \nWe have also sent you an another confirmation email, please confirm your email address in order to activate your account. \n\nThanking you \nBug Hive team. "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ BugHive"
        message2 = render_to_string('email_confirmation.html',{
            'name' : myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_token.make_token(myuser),
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
    
    return render(request, "main_app/signup.html")

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'main_app/userpage.html', {'fname': fname})
        
        else:
            messages.error(request, "Bad Credentials@")
            return redirect('signin')
        
    return render(request, "main_app/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        fname = myuser.first_name
        return render(request, 'main_app/userpage.html', {'fname': fname})
    else:
        return render(request, 'activation_failed.html')
    
def bug_list(request):
    form = BugSearchForm()
    searched_bugs_list = []
    bug_searched = ''
    list_of_bugs = Bug_Query.objects.all()
    search_bugs_display = []
    # p = Paginator(Bug_Query.objects.all(), 2)
    # page = request.GET.get('page')
    # bugs_display = p.get_page(page)

    if request.method == "POST":
        bug_searched = request.POST.get('bug_search', None)
        if bug_searched is not '':
            searched_bugs_list = Bug_Query.objects.filter(bug_title__icontains=bug_searched)
            # p2 = Paginator(Bug_Query.objects.filter(bug_title__icontains=bug_searched), 2)
            # search_page = request.GET.get('page')
            # search_bugs_display = p2.get_page(search_page)
        return render(request, 'main_app/bug_list_template.html', {'searched_bugs_list' : searched_bugs_list, 'form' : form, 'bug_searched' : bug_searched, 'list_of_bugs' : list_of_bugs})

    return render(request, 'main_app/bug_list_template.html', {'searched_bugs_list' : searched_bugs_list, 'form' : form, 'bug_searched' : bug_searched, 'list_of_bugs' : list_of_bugs})

def bug_viewer(request, bug_id):
    individual_bug = Bug_Query.objects.get(pk=bug_id)
    return render(request, 'main_app/bug_viewer_template.html', {'individual_bug' : individual_bug})

def bug_form(request):
    submitted = False
    if request.method == "POST":
        form = BugQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bugform?submitted=True')
    else:
        form = BugQueryForm
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'main_app/bug_form_template.html', {'form' : form, 'submitted' : submitted})

def upadte_bug(request, bug_id):
    bug = Bug_Query.objects.get(pk=bug_id)
    form = BugQueryForm(request.POST or None, instance=bug)
    if form.is_valid():
        form.save()
        return redirect('buglist')
    
    return render(request, 'main_app/update_bug_template.html', {'bug' : bug, 'form' : form})

def delete_bug(request, bug_id):
    bug = Bug_Query.objects.get(pk=bug_id)
    bug.delete()
    return redirect('bug_list')
