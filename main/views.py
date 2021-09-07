from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_data(request):
    return render(request,'index.html')

def operation(request):
    first_input = int(request.POST.get('text1'))
    second_input = int(request.POST.get('text2'))
    plus = request.POST.get('operator1','off')
    minus = request.POST.get('operator2','off')
    divide = request.POST.get('operator3','off')
    multiply = request.POST.get('operator4','off')
    input1 = first_input
    input2 = second_input
    if plus == 'on':
        result = input1 + input2
        final = {'results':result} 
    elif minus == 'on':
        result = input1 - input2
        final = {'results':result} 
    elif multiply == 'on':
        result = input1 * input2
        final = {'results':result} 
    elif divide == 'on':
        result = input1 / input2
        final = {'results': result} 
    else:
        return HttpResponse("Error")

    return render(request,'result.html',final)