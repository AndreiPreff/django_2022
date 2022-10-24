from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


class FeedBackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class UpdateFeedBackView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ListFeedBack(TemplateView):
    template_name = 'feedback/list_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_feedback = Feedback.objects.all()
        context['list_fb'] = all_feedback
        context['all_fb'] = all_feedback.count()

        return context

# class DoneView(View):
#     def get(self, request):
#         return render(request, 'feedback/done.html')


# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})


# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})


# def done(request):
#     return render(request, 'feedback/done.html')
