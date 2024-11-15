from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('regular_exam_october.web.urls')),
    path('author/', include('regular_exam_october.authors.urls')),
    path('posts/', include('regular_exam_october.posts.urls')),
    path('dashboard/', include('regular_exam_october.dashboards.urls')),
]
