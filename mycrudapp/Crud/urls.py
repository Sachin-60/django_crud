from django.urls import path
from .views import (
    MovieListView, MovieDetailView, MovieCreateView,
    MovieUpdateView, MovieDeleteView
)

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("new", MovieCreateView.as_view(), name="movie_new"),
    path("view/<int:pk>", MovieDetailView.as_view(), name="movie_view"),
    path("edit/<int:pk>", MovieUpdateView.as_view(), name="movie_edit"),
    path("delete/<int:pk>", MovieDeleteView.as_view(), name="movie_delete"),
]
