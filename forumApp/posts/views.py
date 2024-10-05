from django.forms import modelform_factory
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


def index(request):
    post_form = modelform_factory(
        Post,
        fields=('title', 'content', 'author', 'languages'),
        error_messages={
            'title': {
                'required': 'Title is required!',
            }
        }
    )

    context = {
        "my_form": post_form(request.POST),
    }

    return render(request, 'common/index.html', context=context)


def dashboard(request):
    form = SearchForm()
    posts = Post.objects.all()

    if request.method == "GET":
        forms = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form
    }

    return render(request, 'posts/dashboard.html', context=context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form
    }

    return render(request, 'posts/add-post.html', context=context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = PostEditForm(instance=post)

    context = {
        "form": form,
        "post": post
    }

    return render(request, 'posts/edit-post.html', context=context)


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


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dash')

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/delete-post.html', context=context)
