from django.shortcuts import render


# Create your views here.
def my_view(request):
    return render(request, 'hi.html')


def logged_user_view(request):
    return render(request, 'logged_user.html')


def not_logged_user_view(request):
    return render(request, 'not_logged_user.html')
