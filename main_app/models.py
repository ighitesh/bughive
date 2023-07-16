from django.db import models

# Create your models here.

# Created the Bug_Search model which is used for creating the BugSearchForm 
# which is then used for searching the bug among the list of bugs
class Bug_Search(models.Model):
    bug_search = models.CharField('Search the Bug', blank = True, max_length=300)
    
    def __str__(self):
        return self.bug_search

# Created the Bug_Solution model which is used for storing the solutinos to the problem to the bug
class Bug_Solution(models.Model):
    sol_title = models.CharField('Solution Title', max_length=500)
    sol_description= models.TextField('Solution Description')
    
    def __str__(self):
        return self.sol_title

# Created the Bug_Priority model for storing the bug priority pre-defined in our database
class Bug_Priority(models.Model):
    bug_priority = models.CharField('Bug Priority', max_length=20)
    
    def __str__(self):
        return self.bug_priority

# Created the Bug_Status model for storing the bug status pre-defined in our database
class Bug_Status(models.Model):
    bug_status = models.CharField('Bug Status', max_length=20)
    
    def __str__(self):
        return self.bug_status

# Created the Bug_Query model for storing the information about the bug in our database
class Bug_Query(models.Model):
    bug_title = models.CharField('Bug Title', max_length=300)
    project_name = models.CharField('Project Name', max_length=300)
    tester_code = models.TextField('Tester code', blank=True, null=True)
    contact = models.CharField('Phone Number', max_length=15)
    bug_priority = models.ForeignKey(Bug_Priority, on_delete=models.DO_NOTHING)
    bug_status = models.ForeignKey(Bug_Status, on_delete=models.DO_NOTHING)
    bug_date = models.DateTimeField('Bug Date')
    query_department = models.CharField('Bug Department', max_length=50)
    bug_description = models.TextField('Bug Description')
    bug_solution = models.ForeignKey(Bug_Solution, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.bug_title