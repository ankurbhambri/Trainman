# from django.shortcuts import render
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from movies.models import Movie


def try_or(fn, default, *args, **kwargs):
    """
    Usage: try_or(lambda: request_user.email, None, *args, **kwargs)
    """
    try:
        return fn(*args, **kwargs)
    except Exception:
        return default


class HomePageView(TemplateView):

    template_name = "movies/index.html"
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_data'] = Movie.objects.all()
        context['login_user'] = self.request.user.username
        return context
