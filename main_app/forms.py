from django import forms
from django.forms import ModelForm
from .models import Bug_Query, Bug_Search

class BugQueryForm(ModelForm):
    class Meta:
        model = Bug_Query
        fields =  ('bug_title', 'project_name', 'contact', 'bug_date', 'bug_priority', 'bug_status', 'query_department', 'bug_description', 'tester_code')
        widgets = {'bug_date' : forms.TextInput(attrs={'placeholder' : 'YYYY-MM-DD HH:MM:SS'},)}
        
class BugSearchForm(ModelForm):
    class Meta:
        model = Bug_Search
        labels = {'bug_search' : '',}
        widgets = {'bug_search' : forms.TextInput(attrs={'placeholder' : 'Enter the title of bug you want to search...'},)}
        fields = ('bug_search',)