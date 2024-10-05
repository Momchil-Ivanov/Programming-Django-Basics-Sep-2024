from django import template

register = template.Library()


@register.inclusion_tag('common/user_info.html', takes_context=True)
def user_info(context):
    request = context['request']
    if request.user.is_authenticated:
        return {
            'username': request.user.username
        }
    else:
        return {
            'username': 'Anonymous'
        }
