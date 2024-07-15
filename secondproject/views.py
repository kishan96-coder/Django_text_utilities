# This file was created by me and it was not given or not created by default

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    # content = {
    #     "Data": "Youtube is best",
    #     "Roll_number" : [1,2,3,4,5,6,7,8,9],
    #     "first_name": "Kishan",
    #     "last_name": "Kumar",
    #     "variable_name":"This is a eductional video in which we are goint to stidy about templates."
    # }
    return render(request,"textutilities-2.html")
#     return HttpResponse('''<nav style="margin:auto"><a href='http://google.com'>Google</a>
# <a href='http://facebook.com'>Facebook</a>
# <a href='http://youtube.com'>Youtube</a>
# <a href='http://apple.com'>Apple</a></nav>''')

def spaceremover(request):
    return HttpResponse("about this web page")

def capitalize(request):
    return HttpResponse("about this web page")

def removepunctuations(request):
    inputtext = request.POST.get('text','default')
    removepunctuations = request.POST.get('removepunctuations','off')
    capitalize = request.POST.get('capitalize','off')
    spaceremover = request.POST.get('spaceremover','off')
    if removepunctuations == "on":
        punctuations = '''!@$%^&*#()_+-={}[];:><,.?/'''
        analyzed = ""
        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed + char

        user_text = {'Task':'Removed Punctuations', 'analyzed_text': analyzed} 
        inputtext = analyzed
        # return render(request,'analyzed.html',user_text)
    if capitalize == "on":
        analyzed = ""
        for char in inputtext:
            analyzed = analyzed + char.upper()
        user_text = {'Task': 'Capitalized', 'analyzed_text': analyzed} 
        inputtext = analyzed
    
    if spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(inputtext):
            if  (inputtext[index] == " " and inputtext[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char
        user_text = {'Task': 'spaceremover ', 'analyzed_text': analyzed}

    if(removepunctuations !="on" and capitalize != "on" and spaceremover != "on"):
        return HttpResponse(' you have not selected any operations!') 
    return render(request,'analyzed.html',user_text)
        
    # else:
    #     return HttpResponse('Error - Your Text has not been analyzed')      


def about(request):
    return HttpResponse("about this web page")

def home(request):
    return HttpResponse("welcome to the home page of this website")