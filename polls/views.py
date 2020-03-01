from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Question
from django.urls import reverse
from django.shortcuts import render
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except ObjectDoesNotExist:
        # checks if the the question exists or not
        raise Http404("Question Does not exist")
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        # request.POST.get() returns the value from form inputs using their names
        selected_choice = question.choice_set.get(
            pk=request.POST.get('choice'))
    except ObjectDoesNotExist:
        # checks if the the property selected or not
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
