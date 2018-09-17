from django.conf.urls import url
from django.urls import path, re_path
from second import views

urlpatterns = [
    path('', views.index, name='sec_database'),
    path('search/', views.search, name='sec_search'),
    path('results/', views.search_results, name='sec_search_results'),
    path('questionnaire/', views.questionnaire, name='sec_questionnaire'),
    path('about/', views.about, name='sec_about'),
    path('signin/', views.Signin.as_view(), name='sec_signin'),
    path('profile/', views.profile, name='sec_profile'),
]
