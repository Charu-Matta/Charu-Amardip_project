from django.shortcuts import render
from django.shortcuts import HttpResponse   
from django.template import RequestContext  #getting request context in your templates.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def main_page(request):
    return render_to_response('main.html',{},context_instance=RequestContext(request))

# def finance(request):
    