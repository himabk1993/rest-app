# polls/urls.py
from django.urls import path

from .views import QuestionViewSet, ChoiceViewSet, QuestionChoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'question', QuestionViewSet, base_name='questions')
router.register(r'choices', ChoiceViewSet, base_name='choices')
router.register(r'question-list', QuestionChoiceViewSet)
urlpatterns = router.urls
