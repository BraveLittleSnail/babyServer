from django.http import HttpResponse
from django.template import  loader
from django.shortcuts import render
#from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Question
import os
from django.conf import settings


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {'latest_question_list': latest_question_list,}
    #return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    print(request)
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    print(request)
    print(HttpResponse("You're voting on question %s." % question_id))
    return HttpResponse("You're voting on question %s." % question_id)


def GetImageList(request):
    result = []  # 所有的文件
    dirpath = settings.BASE_DIR+'\static'
    files = os.listdir(dirpath)
    for file in files:
        #filepath = settings.WEB_URL + 'static/'+file
        file += ";"
        result.append(file)
    print("result==",result )
    return HttpResponse(result)

def calculate(request):
    formula = request.GET['formula']
    print(formula)
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'
    print(result)
    return HttpResponse(result)


# def add(request):
#     formula1 = request.GET["formula1"]
#     print(formula1)
#     try:
#         result = 1024
#     except:
#         result='error'
#     return HttpResponse(result)

def getimagelist(request):
    dirpath = settings.BASE_DIR + '/static'
    print("dirpath==", dirpath)
    files = os.listdir(dirpath)
    result = ''
    for i, file in enumerate(files):
        if i != len(files) - 1:
            file += ";"
        result += file
        print("file==", file)
    return HttpResponse(result)

