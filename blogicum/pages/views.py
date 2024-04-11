from django.shortcuts import render


app_name = 'pages'


# Create your views here.
def about(request):
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')
