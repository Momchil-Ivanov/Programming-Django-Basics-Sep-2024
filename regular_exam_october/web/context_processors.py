from regular_exam_october.authors.models import Author


def has_author(request):
    return {
        'has_author': Author.objects.exists()
    }
