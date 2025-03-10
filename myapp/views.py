from django.shortcuts import render

def home(request):
    pages = {
        "Page 1": "page1",
        "Page 2": "page2",
        "Page 3": "page3",
        "Page 4": "page4",
        "Page 5": "page5",
    }
    return render(request, "myapp/home.html", {"pages": pages, "title": "Home"})

def page1(request):
    return render(request, "myapp/page.html", {"title": "Page 1"})

def page2(request):
    return render(request, "myapp/page.html", {"title": "Page 2"})

def page3(request):
    return render(request, "myapp/page.html", {"title": "Page 3"})

def page4(request):
    return render(request, "myapp/page.html", {"title": "Page 4"})

def page5(request):
    return render(request, "myapp/page.html", {"title": "Page 5"})
