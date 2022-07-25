from django.shortcuts import render

from .models import Like

def liked(request):
    user = request.user
    like = Like.objects.filter(user=user)
    return render(request, 'basket.html', {'likeds': like})