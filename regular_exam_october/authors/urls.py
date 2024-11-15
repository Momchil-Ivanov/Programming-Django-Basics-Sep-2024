from django.urls import path
from .views import AuthorCreateView, AuthorDetailsView, EditAuthorProfileView, DeleteAuthorProfileView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='create_author'),
    path('details/', AuthorDetailsView.as_view(), name='author_details'),
    path('edit/', EditAuthorProfileView.as_view(), name='edit_author'),
    path('delete/', DeleteAuthorProfileView.as_view(), name='delete_author'),
]
