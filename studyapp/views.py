from django.shortcuts import render

def base(request):
    return render(request,'base.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


def index(request):
    return render(request,'index.html')

#ADMIN

def admin_head_dashboard(request):
    return render(request,'admin_dashboard.html')

def admin_profile(request):
    return render(request,'admin_profile.html')

def admin_ithead_page(request):  
    return render(request,'admin_ithead_page.html') 
def admin_ithead_leads(request):  
    return render(request,'admin_ithead_leads.html')   
def admin_councilor_page(request):  
    return render(request,'admin_councilor_page.html')  
def admin_document_page(request):  
    return render(request,'admin_document_page.html')         
def admin_councilor_leads(request):  
    return render(request,'admin_councilor_leads.html')   
def admin_documents_page_documents(request):  
    return render(request,'admin_documents_page_documents.html')     
def load_admin_client_currentstatus(request):
    return render(request,'admin_client_status_current.html') 
def admin_leads(request):
    return render(request,'admin_leads.html')              



#IT HEAD
def IT_head_dashboard(request):
    return render(request,'IT_head_dashboard.html')

def IT_head_profile(request):
    return render(request,'IT_head_profile.html')

def IT_head_leads(request):
    return render(request,'IT_head_leads.html')


    
#STUDENT COUNCILOR
def Student_head_dashboard(request):
    return render(request,'StudentCounsilor.html')

def Student_Councilor_profile(request):
    return render(request,'StudentCouncilor_Profile.html')

def Leads_Data_Collect(request):
    return render(request,'Leads_Data_Collects.html')

def Team_Lead_profile(request):
    return render(request,'Team_Lead_profile.html')


#DOCUMENT OFFICIER
def Document_head_dashboard(request):
    return render(request,'Document_Officer_dashboard.html')

def Document_head_Profile(request):
    return render(request,'Document_Officer_Profile.html')

#TEAM LEAD

def Team_Lead_dashboard(request):
    return render(request, 'Team_Lead_dashboard.html')

#STUDENT
def studeny_progress_report(request):
    return render(request,'studentProgress_Report.html')
def studeny_progress2_report(request):
    return render(request,'studentProgress2.html')


