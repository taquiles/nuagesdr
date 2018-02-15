from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    url(r'^snippets/$', views.RiskTypes_List.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.RiskTypes_Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

