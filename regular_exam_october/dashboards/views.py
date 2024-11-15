from django.views import View
from django.shortcuts import render
from regular_exam_october.posts.models import Post


class DashboardView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-updated_at')
        return render(request, 'dashboards/dashboard.html', {'posts': posts})
