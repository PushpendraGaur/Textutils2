
from django import http
from django.shortcuts import render





def index(request):
    
    return render(request, 'index.html')

def analyze(request):
    
    djtext = request.POST.get('text', 'default')
    check = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
   
    params = {'purpose' : '', 'analyzed_text': ""}
    if(djtext != ''):
        if(check == 'on'):
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed += char
            params['purpose'] = "Removed Punctuation"
            params['analyzed_text'] = analyzed
            
            djtext = analyzed
            
        if(upper == 'on'):
            analyzed = ""
            analyzed = djtext.upper()
            params['purpose'] = 'UPPERCASE'
            params['analyzed_text'] = analyzed
            djtext = analyzed
            
        if(newlineremove == 'on'):
            analyzed = ""
            for char in djtext:
                if not(char == '\n' or char =='\r'):
                    analyzed += char
                
                    
                params['purpose'] = 'Removed New Lines'
                params['analyzed_text'] = analyzed 
                djtext = analyzed  

            
        if(extraspaceremove == 'on'):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] ==" " and djtext[index+1]==" "):
                    analyzed += char
                
                    
            params['purpose'] = 'Removed Extra Spaces'
            params['analyzed_text'] = analyzed
            djtext = analyzed
            
        if(charcount == 'on'):
            analyzed = ""
            params['purpose'] = 'Total character in Paragraph'
            params['charcount'] = 'No. of charcters in text :' +str(len(djtext))
            params['analyzed_text'] = djtext
            
        if(check != 'on' and upper != 'on' and newlineremove != 'on' and extraspaceremove != 'on' and charcount != 'on'):
            return http.HttpResponse("Error!! Please select any operation.")
        return render(request, 'analyze.html', params)
    else:
        params = {"djtext":"","errorResponse":"Please enter the Text in above textarea !!"}
        return render(request, 'index.html', params)