from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Review
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def addReviewView(request):
  target = User.objects.get(username=request.POST.get('to'))
  Review.objects.create(source=request.user, target=target, content=request.POST.get('content'))
  return redirect('/')

@login_required
def homePageView(request):
  users = User.objects.exclude(pk=request.user.id)
  return render(request, 'pages/index.html', {'users': users})

def reviewsView(request, userid):
  user = User.objects.get(pk=userid)
  received = Review.objects.filter(target=user)
  given = Review.objects.filter(source=user)
  return render(request, 'pages/reviews.html', {'received': received, 'given': given})