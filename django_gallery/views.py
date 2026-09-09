from django.shortcuts import render

def home_view(request):
    user_context = {
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else '',
        'email': request.user.email if request.user.is_authenticated else '',
        'firstName': request.user.firstName if request.user.is_authenticated else '',
    }
    return render(request, 'home.html', {'user_data': user_context})