from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ZWExchange API",
      default_version='v1',
      description="Zimbabwe stock exchange API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@exchangeapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', views.api_overview, name='zimbabwean-stocks-api'),
    # path('company-list/', views.company_list, name='company-list'),
    # path('company-detail/<int:pk>/', views.company_detail, name='company-detail'),
    path('companies/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetail.as_view()),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)