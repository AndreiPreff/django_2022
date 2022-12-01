from django.contrib import admin
from django.urls import path
# from .views import index, done, update_feedback, FeedBackView, UpdateFeedBackView, DoneView
from .views import FeedBackView, UpdateFeedBackView, DoneView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate

urlpatterns = [
    path('done', DoneView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<int:pk>', DetailFeedBack.as_view(), name='feedback_detail'),
    path('update/<int:pk>', FeedBackViewUpdate.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', UpdateFeedBackView.as_view()),
]

# path('detail/<int:id_feedback>', DetailFeedBack.as_view(), name='feedback_detail'),