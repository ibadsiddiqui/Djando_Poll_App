from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Question
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.ListView):
    model  = Question
    template_name = 'polls/details.html'

class ResultsView(generic.ListView):
    model = Question
    template_name = 'polls/results.html'

# def indexView(generic.ListView):
#     template_name = 'pollls/index.html'
#     contet_object_name = "latest_question_list"
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
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
