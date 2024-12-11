from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Post, Category, Inquery, Booking
from django.views import generic
from .forms import ImageForm, InqueryForm, BookingForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# Blog list view
class PostListView(generic.ListView):
    model = Post
    paginate_by = 4
    template_name = "blog_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_list"] = Category.objects.all()
        context["post_list"] = Post.objects.all()
        context["categories"] = Category.objects.all()
        return context


# Post detail View
class PostDetailView(generic.DetailView):
    model = Post
    paginate_by = 4
    template_name = "blog_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_list"] = Category.objects.all()
        context["post_list"] = Post.objects.all()
        return context


def PostCategoryView(request, pk):
    category = Category.objects.get(pk=pk)
    category_context = {"category": category}
    return render(request, "category.html", category_context)


def ImageView(request, pk):
    photo = Post.objects.get(pk=pk)
    context = {"photo": photo}
    return render(request, "post_image.html", context)


class InqueryView(generic.CreateView):
    model = Inquery
    form_class = InqueryForm
    template_name = "make_inquery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = Inquery.objects.all()
        return context


# function to send contact form to backend
def inquiryview(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact_form = Inquery.objects.create(
            name=name, email=email, contact=contact, subject=subject, message=message
        )

        return render(request, "contact.html")
    else:
        return render(request, "contact.html")


class BookingView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking.html"


def searchbar(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        blogs = Post.objects.filter(title__contains=searched)
        context_dictionary = {"searched": searched, "blogs": blogs}
        return render(request, "searchbar.html", context_dictionary)
    else:
        return render(request, "searchbar.html", {"search": searched})


class home(generic.ListView):
    model = Post
    paginate_by = 6
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_list"] = Category.objects.all()
        context["post_list"] = Post.objects.all()
        return context


# def home_index(request):
#     return render(request, "index.html")


def about_us(request):
    return render(request, "about.html")


def our_block(request):
    return render(request, "blog_post.html")


def our_contact(request):
    return render(request, "contact.html")


def detial_info(request):
    return render(request, "blog_details.html")


def our_feature(request):
    return render(request, "feature.html")


def price_list(request):
    return render(request, "price.html")


def our_quotes(request):
    return render(request, "quote.html")


def our_services(request):
    return render(request, "service.html")


def our_team(request):
    return render(request, "team.html")


def our_testimonial(request):
    return render(request, "testimonial.html") 

def talents(request):
    return render(request, "talents.html")
