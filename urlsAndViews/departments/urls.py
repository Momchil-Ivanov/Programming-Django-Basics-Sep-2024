from xml.etree.ElementInclude import include

from django.urls import path, re_path
from urlsAndViews.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect/', views.redirect_to_view, name='redirect-view'),
    path('softuni/', views.redirect_to_softuni),
    path('<int:pk>/', views.view_with_int_pk),
    path('<int:pk>/<slug:slug>/', views.view_with_slug),
    path('<variable>/', views.view_with_name), # matches till /
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    path('<path:variable>/', views.view_with_name), # matches after the /
    # path ('<uuid:id>, some_view'),
]