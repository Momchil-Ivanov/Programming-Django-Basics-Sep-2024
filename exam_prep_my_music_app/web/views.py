from django.shortcuts import render, redirect

from exam_prep_my_music_app.common.profile_helpers import get_profile
from exam_prep_my_music_app.profiles.models import Profile
from exam_prep_my_music_app.web.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        "no_nav": True,
    }
    return render(request, 'web/home-no-profile.html', context)


def index(request):
    profile = get_profile()
    if profile is None:
        return create_profile(request)

    context = {
        'albums': profile.albums.all(),
    }

    return render(request, 'web/home-with-profile.html', context)


# class IndexView(views.TemplateView):
#     def get_template_names(self):
#         if get_profile() is None:
#             return ['web/home-no-profile.html']
#
#         return ['web/home-with-profile.html']
