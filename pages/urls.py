from django.urls import path

from .views import homePageView, addReviewView, reviewsView

urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addReviewView, name='add'),

    # FIX: Broken Access Control
    # path("reviews/", reviewsView, name="reviews"),
    path("reviews/<int:userid>/", reviewsView, name="reviews"),
]
