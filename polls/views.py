from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Question,Choice
import datetime

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)
def detail(request,question_id):
    try:
        question = Question.objects.get(pk= question_id)
    except Question.DoesNotExist:
        time = datetime.datetime.now()
        question = Question.objects.create(pub_date = time)
        question.id = question_id;
        question.content = question_id      
        print(question.pub_date)
    return render(request,'polls/detail.html',{'question':question})
def vote(request,question_id):
    question = get_object_or_404(Question,pk= 1)
    question.content = request.POST['content']
    question.save()
    ps = request.POST['choice']
 
       
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])       
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'df':ps,'error_message':"you didn't select a choice",})
    else:        
     
        selected_choice.votes+=1
        selected_choice.save()
        return render(request,'polls/detail.html',{'question':question,'df':ps,'error_message':"you didn't select a choice",'request':request})