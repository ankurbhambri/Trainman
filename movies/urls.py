from django.urls import path
from movies.views import HomePageView, MovieDetails

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('movie/<int:pk>', MovieDetails.as_view(), name='movie'),
]
