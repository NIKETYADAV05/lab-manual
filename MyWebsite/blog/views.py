from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .forms import UserForm
from .models import Book, Product
from .serializers import ProductSerializer


def home_view(request):
    return render(request, "blog/home.html")


def about_view(request):
    return render(request, "blog/about.html")


def book_list(request):
    books = Book.objects.all()
    return render(request, "blog/book_list.html", {"books": books})


def contact_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return render(
                request,
                "blog/success.html",
                {
                    "name": form.cleaned_data["name"],
                    "email": form.cleaned_data["email"],
                },
            )
    else:
        form = UserForm()

    return render(request, "blog/form_page.html", {"form": form})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def not_found(request, invalid_path=""):
    return JsonResponse(
        {
            "error": "404 Not Found",
            "message": "The requested API route does not exist."
        },
        status=404
    )