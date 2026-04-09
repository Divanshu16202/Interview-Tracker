from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings

def home(request):
    return render(request, 'tracker/home.html')

from .models import (
    CodingPractice,
    MockQuestion,
    MockAttempt,
    AIQuestion,
    UserStreak
)
from .forms import CodingPracticeForm

import google.generativeai as genai
import json


# ------------------- AI MOCK GENERATOR -------------------

@login_required
def generate_ai_mock(request):
    if request.method == "POST":
        category = request.POST.get("category")
        difficulty = request.POST.get("difficulty")

        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-3-flash-preview")

        prompt = f"""
        Generate 10 multiple choice interview questions 
        for Computer Science students 
        on {category} with {difficulty} difficulty.

        Return strictly in JSON format like:
        [
          {{
            "question": "...",
            "option1": "...",
            "option2": "...",
            "option3": "...",
            "option4": "...",
            "correct_answer": "..."
          }}
        ]
        """

        try:
            response = model.generate_content(prompt)
            questions = json.loads(response.text)

            AIQuestion.objects.all().delete()

            for q in questions:
                AIQuestion.objects.create(
                    category=category,
                    difficulty=difficulty,
                    question=q["question"],
                    option1=q["option1"],
                    option2=q["option2"],
                    option3=q["option3"],
                    option4=q["option4"],
                    correct_answer=q["correct_answer"],
                )

            return redirect("ai_mock")

        except Exception as e:
            return render(request, "tracker/error.html", {"error": str(e)})

    return render(request, "tracker/generate_mock.html")


@login_required
def ai_mock(request):
    questions = AIQuestion.objects.all()

    if request.method == "POST":
        score = 0
        total = questions.count()

        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_answer:
                score += 1

        return render(request, "tracker/mock_result.html", {
            "score": score,
            "total": total
        })

    return render(request, "tracker/ai_mock.html", {
        "questions": questions
    })


# ------------------- NORMAL MOCK -------------------

@login_required
def start_mock(request):
    questions = MockQuestion.objects.all()[:10]

    if request.method == "POST":
        score = 0
        total = questions.count()

        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_answer:
                score += 1

        MockAttempt.objects.create(
            user=request.user,
            score=score,
            total_questions=total
        )

        return render(request, 'tracker/mock_result.html', {
            'score': score,
            'total': total
        })

    return render(request, 'tracker/mock_interview.html', {
        'questions': questions
    })


# ------------------- CODING PRACTICE -------------------

@login_required
def dashboard(request):
    coding_list = CodingPractice.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {
        'coding_list': coding_list
    })


@login_required
def add_coding(request):
    form = CodingPracticeForm(request.POST or None)

    if form.is_valid():
        coding = form.save(commit=False)
        coding.user = request.user
        coding.save()

        streak, _ = UserStreak.objects.get_or_create(user=request.user)
        streak.update_streak()

        return redirect('dashboard')

    return render(request, 'tracker/add_coding.html', {'form': form})


@login_required
def edit_coding(request, pk):
    coding = get_object_or_404(CodingPractice, pk=pk, user=request.user)
    form = CodingPracticeForm(request.POST or None, instance=coding)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'tracker/add_coding.html', {'form': form})


@login_required
def delete_coding(request, pk):
    coding = get_object_or_404(CodingPractice, pk=pk, user=request.user)

    if request.method == "POST":
        coding.delete()
        return redirect('dashboard')

    return render(request, 'tracker/confirm_delete.html', {'coding': coding})


# ------------------- AUTH -------------------

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')

    return render(request, 'tracker/register.html', {'form': form})


@login_required
def viva_page(request):
    return render(request, 'tracker/viva.html')

from django.contrib.auth import logout

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # or 'login' if you have a login page