from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam, Question, Choice, Result
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams/exam_list.html', {'exams': exams})

@login_required
def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        score = 0
        for question in exam.question_set.all():
            selected_choice = request.POST.get(f'question_{question.id}')
            if selected_choice:
                choice = Choice.objects.get(id=selected_choice)
                if choice.is_correct:
                    score += 1
        result = Result(user=request.user, exam=exam, score=score)
        result.save()
        return redirect('exam_result', result_id=result.id)
    return render(request, 'exams/take_exam.html', {'exam': exam})

@login_required
def exam_result(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    return render(request, 'exams/exam_result.html', {'result': result})
