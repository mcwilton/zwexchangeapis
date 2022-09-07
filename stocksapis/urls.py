from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.api_overview, name='zimbabwean-stocks-api'),
    # path('company-list/', views.company_list, name='company-list'),
    # path('company-detail/<int:pk>/', views.company_detail, name='company-detail'),
    path('companies/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)