from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        html = "<html><body>You search: %s</body></html>" %search
        if search:
            return HttpResponse(html)
        else:
            return HttpResponse("BLANK")
    return render(request,'search/search_bar.html')
