from rest_framework import serializers
from .models import Question, Choice
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
    queryset = User.objects.all(),
    )
    class Meta:
        model = Question
        fields = ('id', 'user', 'question_text', 'pub_date',)

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ( 'id', 'choice_text', 'votes',)

class ChoiceQuestionSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(
    queryset = Question.objects.all(),
    slug_field = 'question_text'
    )
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes', )

class QuestionListSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source = 'choice_set', many = True)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices',)


"""
class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length = 120)
    pub_date = serializers.DateTimeField()
#    user = serializers.IntegerField()
"""
"""
class ChoiceSerializer(serializers.Serializer):
    choice_text = serializers.CharField(max_length = 120)
    votes = serializers.IntegerField()
#    user = serializers.IntegerField()
    question = serializers.IntegerField()
"""
#class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Choice
#        fields = ('choice_text', 'votes')
