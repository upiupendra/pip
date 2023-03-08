from django.shortcuts import render
from django.http import HttpResponse

def second(request):
    return HttpResponse('this is secondproject')

def third(request):
    return HttpResponse('this is a thirdproject')