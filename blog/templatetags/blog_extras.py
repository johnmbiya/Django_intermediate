from django import template

register = template.Library()


@register.filter
def model_type(instance):
    return type(instance).__name__

@register.simple_tag
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username

@register.filter
def get_posted_at_display(time):
    pass


