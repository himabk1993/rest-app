from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Prefetch
from . import models
from . import serializers
from django.db import connection
#from query_logger import DatabaseQueryLoggerMixin


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceQuestionSerializer


class QuestionChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionListSerializer

"""
class QuestionView(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many = True)
        return Response({'question' : serializer.data})

    def post(self,request):
        question = Question.data.get('question_text')
        serializer = QuestionSerializer(data = question)
        if serializer.is_valide(raise_exception = True):
            question_saved = serializer.save()
        return Response({'success' : "question '{}' created successfully".format(question_saved.title)})

    def create(self, validated_data):
        return question.Objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance

    def put(self, request, pk):
        saved_question = get_object_or_404(Question.objects.al(), pk = pk)
        data = request.data.get('question')
        serializer =QuestionSerializer(instance = saved_question, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            question_saved = serializer.save()
        return Response({"success" : "Question '{}' updated successfully".format(question_saved.question_text) })

    def delete(self, request, pk):
        question = get_object_or_404(Question.objects.all(), pk = pk)
        question.delete()
        return Response({"message" : "Question with id '{}' has been deleted".format(pk)}, status = 204)
"""
"""
class ChoiceView(APIView):
    def get(self, request, question_id):
        question = Question.objects.filter(pk = question_id)
        choices = question.choice_set.all()
        serializer = ChoiceSerializer(choices, many = True)
        return Response({'question' : serializer.data})

    def post(self,request, question_id):
        choice = Choice.data.get('choice_text')
        serializer = ChoiceSerializer(data = choice)
        if serializer.is_valide(raise_exception = True):
            choice_saved = serializer.save()
        return Response({'success' : "question '{}' created successfully".format(choice_saved.title)})

    def create(self, validated_data):
        return Choice.Objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.choice_text = validated_data.get('choice_text', instance.choice_text)
        instance.votes = validated_data.get('votes', instance.votes)
#        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance

    def put(self, request, pk):
        saved_choice = get_object_or_404(Question.objects.al(), pk = pk)
        data = request.data.get('choice')
        serializer =ChoiceSerializer(instance = saved_choice, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            choice_saved = serializer.save()
        return Response({"success" : "Choice '{}' updated successfully".format(choice_saved.question_text) })

    def delete(self, request, pk):
        choice = get_object_or_404(Question.objects.all(), pk = pk)
        choice.delete()
        return Response({"message" : "Choice with id '{}' has been deleted".format(pk)}, status = 204)
"""
#class ChoiceViewSet(viewsets.ModelViewSet):
#    API endpoint that allows users to be viewed or edited.
#    """
#    choiceset = Choice.objects.all()
#    serializer_class = ChoiceSerializer
