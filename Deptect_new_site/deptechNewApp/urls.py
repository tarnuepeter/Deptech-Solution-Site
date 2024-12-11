from django.urls import path
from . import views

urlpatterns = [
    path("", views.home.as_view(), name="home"),
    path("about/", views.about_us, name="about"),
    path("blog/", views.our_block, name="blog"),
    path("contact/", views.our_contact, name="contact"),
    path("detail/", views.detial_info, name="detail"),
    path("feature/", views.our_feature, name="feature"),
    path("price/", views.price_list, name="price"),
    path("quote/", views.our_quotes, name="quote"),
    path("service/", views.our_services, name="service"),
    path("team/", views.our_team, name="team"),
    path("testimonial/", views.our_testimonial, name="testimonial"),
    path("home/", views.home.as_view(), name="home"), 
    path('talent/', views.talents, name='talent'),
    # Post Urls
    path("bloglist/", views.PostListView.as_view(), name="blogposts"),
    path("postdetai/<int:pk>", views.PostDetailView.as_view(), name="postdetail"),
    path("category/<int:pk>", views.PostCategoryView, name="postcategory"),
    path("uploadImage/", views.ImageView, name="imageload"),
    path("askquestion/", views.InqueryView.as_view(), name="askquestion"),
    path("book/", views.BookingView.as_view(), name="book-now"),
    path("searchbar/", views.searchbar, name="search-bar"),
    path("contact/contact-form", views.inquiryview, name="contact-form"),
]
