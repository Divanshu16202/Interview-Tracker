from django.contrib import admin
from .models import (
    CodingPractice,
    StudyTopic,
    MockInterview,
    Goal,
    MockQuestion,
    MockAttempt,
    UserAnswer,
    UserStreak
)


# ==============================
# Mock Question Admin
# ==============================

@admin.register(MockQuestion)
class MockQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'difficulty',
        'question',
        'is_ai_generated',
        'created_at'
    )
    list_filter = ('category', 'difficulty', 'is_ai_generated')
    search_fields = ('question',)


# ==============================
# Mock Attempt Admin
# ==============================

@admin.register(MockAttempt)
class MockAttemptAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category',
        'difficulty',
        'score',
        'total_questions',
        'percentage',
        'started_at'
    )
    list_filter = ('category', 'difficulty')
    search_fields = ('user__username',)


# ==============================
# User Answer Admin
# ==============================

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'selected_answer', 'is_correct')
    list_filter = ('is_correct',)


# ==============================
# Other Models
# ==============================

@admin.register(CodingPractice)
class CodingPracticeAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'problem_name', 'difficulty', 'date')
    list_filter = ('difficulty', 'platform')
    search_fields = ('problem_name', 'user__username')


@admin.register(StudyTopic)
class StudyTopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic_name', 'completed')
    list_filter = ('completed',)


@admin.register(MockInterview)
class MockInterviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'interviewer_name', 'rating', 'date')
    list_filter = ('rating',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_title', 'achieved')
    list_filter = ('achieved',)


@admin.register(UserStreak)
class UserStreakAdmin(admin.ModelAdmin):
    list_display = ('user', 'streak_count', 'last_practice_date')