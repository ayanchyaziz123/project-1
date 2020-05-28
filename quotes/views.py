from django.shortcuts import render
from django.views.generic import ListView
from . models import Album
from . models import Song



class HomeView(ListView):
    template_name = "index.html"
    model = Song

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('album_cat')