from django.db import models
from django.contrib.auth.models import User
from datetime import date

class AIQuestion(models.Model):
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]
# ===============================
# 1️⃣ MOCK QUESTION MODEL
# ===============================

class MockQuestion(models.Model):
    CATEGORY_CHOICES = [
        ('DSA', 'Data Structures & Algorithms'),
        ('DBMS', 'Database Management'),
        ('OS', 'Operating Systems'),
        ('CN', 'Computer Networks'),
        ('OOPS', 'Object Oriented Programming'),
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    question = models.TextField()

    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=255)

    explanation = models.TextField(blank=True, null=True)  # NEW

    is_ai_generated = models.BooleanField(default=False)  # NEW

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.question[:50]}"


# ===============================
# 2️⃣ MOCK ATTEMPT MODEL
# ===============================

class MockAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)

    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)

    percentage = models.FloatField(default=0.0)  # NEW

    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total_questions}"


# ===============================
# 3️⃣ STORE USER ANSWERS (NEW - IMPORTANT)
# ===============================

class UserAnswer(models.Model):
    attempt = models.ForeignKey(MockAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(MockQuestion, on_delete=models.CASCADE)

    selected_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attempt.user.username} - {self.question.id}"


# ===============================
# 4️⃣ CODING PRACTICE MODEL
# ===============================

class CodingPractice(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)
    problem_name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.problem_name


# ===============================
# 5️⃣ STUDY TOPIC
# ===============================

class StudyTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.topic_name


# ===============================
# 6️⃣ MOCK INTERVIEW FEEDBACK
# ===============================

class MockInterview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interviewer_name = models.CharField(max_length=200)
    feedback = models.TextField()

    rating = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}/5"


# ===============================
# 7️⃣ USER GOALS
# ===============================

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_title = models.CharField(max_length=200)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_title


# ===============================
# 8️⃣ USER STREAK TRACKING
# ===============================

class UserStreak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_practice_date = models.DateField(null=True, blank=True)
    streak_count = models.IntegerField(default=0)

    def update_streak(self):
        today = date.today()

        if self.last_practice_date == today:
            return

        if self.last_practice_date and (today - self.last_practice_date).days == 1:
            self.streak_count += 1
        else:
            self.streak_count = 1

        self.last_practice_date = today
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.streak_count} days"