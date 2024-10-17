from datetime import datetime
from django.forms import modelform_factory
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DeleteView

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


class BaseView:
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'common/index.html'  # static_way

    extra_context = {
        'static_time': datetime.now(),
    }  # static way

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Hello, world!")

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)
        context['dynamic_time'] = datetime.now()
        return context

    def get_template_names(self):  # dynamic_way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


class Index(BaseView):
    def get(self, request, *args, **kwargs):

        context = {
            'dynamic_time': datetime.now()
        }

        return render(request, 'common/index.html', context)

# def index(request):
#     post_form = modelform_factory(
#         Post,
#         fields=('title', 'content', 'author', 'languages'),
#         error_messages={
#             'title': {
#                 'required': 'Title is required!',
#             }
#         }
#     )
#
#     context = {
#         "my_form": post_form(request.POST),
#     }
#
#     return render(request, 'common/index.html', context=context)


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    success_url = reverse_lazy('dash')
    model = Post

    def get_queryset(self):

        queryset = self.model.objects.all()
        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            if query:
                queryset = self.queryset.filter(title__icontains=query)

        return queryset

# def dashboard(request):
#     form = SearchForm()
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         forms = SearchForm(request.GET)
#
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form
#     }

    # return render(request, 'posts/dashboard.html', context=context)


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')

# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#
#     context = {
#         "form": form
#     }
#
#     return render(request, 'posts/add-post.html', context=context)


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages'))
        else:
            return modelform_factory(Post, fields=('content',))

# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = PostEditForm(request.POST, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         "form": form,
#         "post": post
#     }
#
#     return render(request, 'posts/edit-post.html', context=context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        "formset": formset,
    }

    return render(request, 'posts/details-post.html', context=context)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__

# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('dash')
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, 'posts/delete-post.html', context=context)
#
#
class RedirectHomeView(RedirectView):
    url = reverse_lazy('index')  # static way

    def get_redirect_url(self, *args, **kwargs):  # dynamic way
        pass
