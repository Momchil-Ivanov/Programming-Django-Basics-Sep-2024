from django.urls import path, include
from .views import CreatePostView, PostDetailsView, EditPostView, DeletePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<int:post_id>/', include([
        path('details/', PostDetailsView.as_view(), name='post_details'),
        path('edit/', EditPostView.as_view(), name='edit_post'),
        path('delete/', DeletePostView.as_view(), name='delete_post'),
    ])),
]
