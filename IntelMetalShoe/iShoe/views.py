from django.shortcuts import render ,HttpResponse

# Create your views here.
def shoelist(request):
    context = {'v':1}
    # return HttpResponse('ss')
    return render(request, 'iShoe/index.html',context)

def shoemanage(request):
    context = {'v':1}
    return render(request, 'iShoe/shoemanage.html',context)
