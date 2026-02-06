from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = "Crud/movie_list.html"
    context_object_name = "movies"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "Crud/movie_view.html"
    context_object_name = "movie"

class MovieCreateView(CreateView):
    model = Movie
    template_name = "Crud/movie_new.html"
    fields = ['title', 'rating','review']
    success_url = reverse_lazy("movie_list")

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "Crud/movie_edit.html"
    fields = ['title', 'rating','review'] 
    success_url = reverse_lazy("movie_list")

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "Crud/movie_delete.html"
    success_url = reverse_lazy("movie_list")

