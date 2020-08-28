from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
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

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = {
            "movies_data": Movie.objects.all(),
            "login_user": self.request.user.username,
        }
        return render(request, self.template_name, {"context": context})


class MovieDetails(DetailView):

    template_name = "movies/movie_details.html"
    model = Movie

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MovieDetails, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MovieDetails, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = {
            "movie_data": get_object_or_404(Movie, pk=kwargs['pk']),
            "login_user": self.request.user.username
        }
        return render(request, self.template_name, {"context": context})
