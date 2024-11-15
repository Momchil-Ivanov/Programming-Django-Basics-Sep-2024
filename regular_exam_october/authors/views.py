from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView

from .forms import AuthorProfileForm, AuthorEditForm
from .models import Author
from regular_exam_october.posts.models import Post


class AuthorCreateView(View):
    def get(self, request):
        form = AuthorProfileForm()
        return render(request, 'authors/create-author.html', {'form': form})

    def post(self, request):
        form = AuthorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'authors/create-author.html', {'form': form})


class AuthorDetailsView(View):
    def get(self, request):

        author = get_object_or_404(Author)
        posts = Post.objects.filter(author=author)
        last_updated_post_title = posts.order_by('-updated_at').first().title if posts.exists() else "N/A"
        total_posts = posts.count()

        context = {
            'author': author,
            'total_posts': total_posts,
            'last_updated_post_title': last_updated_post_title,
            'default_image_url': '/static/images/default.png',
        }
        return render(request, 'authors/details-author.html', context)


class EditAuthorProfileView(View):
    def get(self, request):
        author = get_object_or_404(Author)
        form = AuthorEditForm(instance=author)
        return render(request, 'authors/edit-author.html', {'form': form})

    def post(self, request):
        author = get_object_or_404(Author)
        form = AuthorEditForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_details')
        return render(request, 'authors/edit-author.html', {'form': form})


class DeleteAuthorProfileView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):

        author = get_object_or_404(Author)
        return author

    def post(self, request, *args, **kwargs):
        author = self.get_object()
        Post.objects.filter(author=author).delete()
        return super().post(request, *args, **kwargs)
