from django.urls import path,re_path
from django.conf.urls import url
from cbv_app import views
app_name="cbv_app"
urlpatterns = [
  path('register/',views.register_school,name="register"),
  path('school_list/',views.SchoolListView.as_view(),name="school_list"),
  path('register_student/',views.register_student,name="register_student"),
  re_path(r'^school_list/(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
  re_path(r'^school_list/(?P<pk>\d+)/update/$',views.SchoolUpdateView.as_view(),name='update'),
  re_path(r'^school_list/(?P<pk>\d+)/delete/$',views.SchoolDeleteView.as_view(),name='delete'),
  ]
