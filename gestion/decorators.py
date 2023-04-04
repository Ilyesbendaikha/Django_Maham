from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request)
    return wrapper


def allowed_roll(allowed_roll=[]):
    def decorator(func):
        def wrapper(request):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roll:
                return func(request)
            else: 
                return HttpResponse('You Are Not Allowed To Access')
        return wrapper
    return decorator

def only_admin(func):
    def wrapper(request):
        group = None
        if request.user.groups.exists():
            pass