from django import forms
from .models import CodingPractice, StudyTopic, MockInterview, Goal

class CodingPracticeForm(forms.ModelForm):
    class Meta:
        model = CodingPractice
        fields = ['platform', 'problem_name', 'difficulty']


class StudyTopicForm(forms.ModelForm):
    class Meta:
        model = StudyTopic
        fields = ['topic_name', 'completed']


class MockInterviewForm(forms.ModelForm):
    class Meta:
        model = MockInterview
        fields = ['interviewer_name', 'feedback', 'rating']


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_title', 'achieved']