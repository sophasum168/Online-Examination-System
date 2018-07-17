"""
import neccessary module
"""
from rest_framework import serializers
from .models import Test, Question, Option

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serialize questions from Question Model
    """
    class Meta:
        model = Question
        fields = ('test_id', 'question_type', 'question_name')

class TestSerializer(serializers.ModelSerializer):
    """
    Serialize test_id from Test Model
    """
    class Meta:
        model = Test
        fields = ('test_id', 'test_name')

class OptionSerializer(serializers.ModelSerializer):
    """
    Serialize options of QCM questions from Option Model
    """
    class Meta:
        model = Option
        fields = ('question_id', 'option_name', 'answer')
