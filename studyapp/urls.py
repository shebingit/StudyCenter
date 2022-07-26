from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns =[  path('',views.login,name='login'),
path('base',views.base,name='base'),
path('register',views.register,name='register'),
path('index',views.index,name='index'),

#ADMIN
path('admin_head_dashboard',views.admin_head_dashboard,name='admin_head_dashboard'),
path('admin_profile',views.admin_profile,name='admin_profile'),
path('admin_ithead_page',views.admin_ithead_page,name='admin_ithead_page'),
path('admin_ithead_leads',views.admin_ithead_leads,name='admin_ithead_leads'),
path('admin_councilor_page',views.admin_councilor_page,name='admin_councilor_page'),
path('admin_councilor_leads',views.admin_councilor_leads,name='admin_councilor_leads'),
path('admin_document_page',views.admin_document_page,name='admin_document_page'),
path('admin_leads',views.admin_leads,name='admin_leads'),
path('admin_documents_page_documents',views.admin_documents_page_documents,name='admin_documents_page_documents'),
path('load_admin_client_currentstatus',views.load_admin_client_currentstatus,name='load_admin_client_currentstatus'),

#IT HEAD
path('IT_head_dashboard',views.IT_head_dashboard,name='IT_head_dashboard'),
path('IT_head_profile',views.IT_head_profile,name='IT_head_profile'),
path('IT_head_leads',views.IT_head_leads,name='IT_head_leads'),


#STUDENT COUNCILOR
path('Student_head_dashboard',views.Student_head_dashboard,name='Student_head_dashboard'),
path('Student_Councilor_profile',views.Student_Councilor_profile,name='Student_Councilor_profile'),
path('Leads_Data_Collect',views.Leads_Data_Collect,name='Leads_Data_Collect'),


#DOCUMENT OFFICIER
path('Document_head_dashboard',views.Document_head_dashboard,name='Document_head_dashboard'),
path('Document_head_Profile',views.Document_head_Profile,name='Document_head_Profile'),

#Team_Lead
path('Team_Lead_dashboard',views.Team_Lead_dashboard,name='Team_Lead_dashboard'),
path('Team_Lead_profile',views.Team_Lead_profile,name='Team_Lead_profile'),

#STUDENT
path('studeny_progress_report',views.studeny_progress_report,name='studeny_progress_report'),
path('studeny_progress2_report',views.studeny_progress2_report,name='studeny_progress2_report'),

 
]