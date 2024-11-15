from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView
from regular_exam_october.authors.models import Author
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create-post.html'

    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)


class EditPostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post)
        return render(request, 'posts/edit-post.html', {'form': form, 'post_id': post.id})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'posts/edit-post.html', {'form': form, 'post_id': post.id})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)
