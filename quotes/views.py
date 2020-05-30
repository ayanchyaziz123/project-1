from django.shortcuts import render
from django.views.generic import ListView
from . models import tbl_category
from . models import tbl_adminPost



class HomeView(ListView):
    template_name = "index.html"
    model = tbl_adminPost

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('post_cat')