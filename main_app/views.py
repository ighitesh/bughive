from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Used for displaying the error messages
from django.contrib import messages
# Used for authentication and registration of the users
from django.contrib.auth import authenticate, login, logout
# Following are used for encoding our custom activation link for the user and for sending the Email to the user
from bug_tracker import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . token import generate_token
from django.core.mail import EmailMessage, send_mail
# Imported custom made model from models.py file
from . models import Bug_Query
# Imported custom made BugQueryForm and BugQueryForm from forms.py file
from . forms import BugQueryForm, BugQueryForm
# Used for making the page redirect after submitting the form
from django.http import HttpResponseRedirect

# from django.core.paginator import Paginator

# Create your views here.

# This home view is used to render the main home page of the website
def home(request):
    return render(request, "main_app/index.html")

# This userhome view is used to render the user home page when they are logged un
def userhome(request):
    return render(request, "main_app/userpage.html")

# This signup view is used for making the user signup using the Django authentication functionality
def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Here, I am filtering the username of user in my databse, so that it will be unique for a particualr user
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('signup')
            
        # Here, I am filtering the email of user in my databse, so that it will be unique for a particualr user
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')
        
        # Length of username should not be greater than 10
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            
        # For making password and confirm password functionality
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            
        # For checking whether username is alphanumeric or not
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('signup')
        
        # Creating a Django user and saving the user using the details filled by the user in the registration form
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        
        messages.success(request, "Your account has been sucessfully created. We have sent you a confirmation email, please confirm your email in order to activate your account.")
        
        # The following is the code for sending Welcome Email to the user
        
        subject = "Welcome to Bug Hive"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Bug Hive \nThankyou for being a part of us. \nWe have also sent you an another confirmation email, please confirm your email address in order to activate your account. \n\nThanking you \nBug Hive team. "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # The following is the code for sending Confirmation Email to the user about their account
        
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

# This signin view is used for making the user signin using the Django login functionality
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

# This signout view is used for making the user signout using the Django logout functionality
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

# This activate view is used for making the user account activate after they click the link which will be send to them via the email
# Here, passed the id of the user and the token so that by using the id of the user as primary key, we then able
# to activate the account of that particular user
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        # Finds the user with the primary key as 'uid'
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    # Used tokens for making the activation link unique
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        fname = myuser.first_name
        return render(request, 'main_app/userpage.html', {'fname': fname})
    else:
        return render(request, 'activation_failed.html')
    
# This bug_list view is used for displaying the list of bugs which are present in the database
# Also added the search functionality among the list of bugs which is displayed so that 
# user can find the bug with respect to theit bug title
def bug_list(request):
    form = BugSearchForm()
    searched_bugs_list = []
    bug_searched = ''
    list_of_bugs = Bug_Query.objects.all()
    search_bugs_display = []
    
    # Tried to use paginator in my code
    # p = Paginator(Bug_Query.objects.all(), 2)
    # page = request.GET.get('page')
    # bugs_display = p.get_page(page)

    # This is the code for making the search functionality
    if request.method == "POST":
        bug_searched = request.POST.get('bug_search', None)
        if bug_searched is not '':
            searched_bugs_list = Bug_Query.objects.filter(bug_title__icontains=bug_searched)
            # p2 = Paginator(Bug_Query.objects.filter(bug_title__icontains=bug_searched), 2)
            # search_page = request.GET.get('page')
            # search_bugs_display = p2.get_page(search_page)
        return render(request, 'main_app/bug_list_template.html', {'searched_bugs_list' : searched_bugs_list, 'form' : form, 'bug_searched' : bug_searched, 'list_of_bugs' : list_of_bugs})

    return render(request, 'main_app/bug_list_template.html', {'searched_bugs_list' : searched_bugs_list, 'form' : form, 'bug_searched' : bug_searched, 'list_of_bugs' : list_of_bugs})

# This bug_viewer view is used for viewing the details of the individual bug which are present in the database
# Here, I passed the id of the bug query so that by using the id as primary key, we then able
# to view that particular bug query
def bug_viewer(request, bug_id):
    individual_bug = Bug_Query.objects.get(pk=bug_id)
    return render(request, 'main_app/bug_viewer_template.html', {'individual_bug' : individual_bug})

# This bug_form is used for submitting the bug query to the database, which then will appears on the list_of_bugs page
def bug_form(request):
    # Used the submitted variable for making sure that the form is submitted
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

# This upadte_bug view calls the BugQueryForm which then update the bug information
# Here, I passed the id of the bug query so that by using the id as primary key, we then able
# to update that particular bug query
def upadte_bug(request, bug_id):
    bug = Bug_Query.objects.get(pk=bug_id)
    form = BugQueryForm(request.POST or None, instance=bug)
    if form.is_valid():
        form.save()
        return redirect('buglist')
    
    return render(request, 'main_app/update_bug_template.html', {'bug' : bug, 'form' : form})

# This delete_bug view is used for deleting the bugs from the database using the frontend
# Here, I passed the id of the bug query so that by using the id as primary key, we then able
# to delete that particular bug query
def delete_bug(request, bug_id):
    bug = Bug_Query.objects.get(pk=bug_id)
    bug.delete()
    return redirect('bug_list')
