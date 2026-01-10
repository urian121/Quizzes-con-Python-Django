from django.shortcuts import render
from .models import QuizQuestion

def index(request):
    return render(request, 'index.html')

def _session_answers(request):
    return request.session.get('answers', {})

def _counts(questions, answers):
    m = {str(q.id): q.respuesta_correcta for q in questions}
    correct = sum(1 for k, v in answers.items() if m.get(k) == v)
    wrong = sum(1 for k, v in answers.items() if k in m and m.get(k) != v)
    return correct, wrong

def quiz_question(request):
    questions = list(QuizQuestion.objects.order_by('id'))
    total = len(questions)
    answers = _session_answers(request)
    allowed = min(len(answers) + 1, total or 1)
    try:
        idx = int(request.GET.get('q', 1))
    except ValueError:
        idx = 1
    idx = max(1, min(idx, allowed))
    q = questions[idx - 1] if questions else None
    selected = answers.get(str(q.id)) if q else None
    letters = ['A','B','C','D','E','F']
    options = [{'label': letters[i] if i < len(letters) else str(i + 1), 'text': t} for i, t in enumerate(q.opciones if q else [])]
    correct, wrong = _counts(questions, answers)
    return render(request, 'quizzes/partials/question.html', {
        'test_name': 'Prueba Técnica de Django',
        'total_questions': total,
        'current_index': idx,
        'segments': list(range(total)),
        'current_question': {'id': q.id if q else None, 'pregunta': q.pregunta if q else ''},
        'selected_answer': selected,
        'current_options': options,
        'wrong_count': wrong,
        'correct_count': correct,
        'at_end': idx >= total,
    })

def quiz_submit(request):
    if request.method != 'POST':
        return quiz_question(request)
    questions = list(QuizQuestion.objects.order_by('id'))
    total = len(questions)
    try:
        idx = int(request.POST.get('q', 1))
    except ValueError:
        idx = 1
    idx = max(1, min(idx, total or 1))
    opt = request.POST.get('option')
    answers = _session_answers(request)
    if opt:
        q = questions[idx - 1] if questions else None
        if q:
            answers[str(q.id)] = opt
            request.session['answers'] = answers
        if idx >= total:
            return quiz_results(request)
        request.GET = request.GET.copy()
        request.GET['q'] = str(min(idx + 1, total or 1))
        return quiz_question(request)
    request.GET = request.GET.copy()
    request.GET['q'] = str(idx)
    return quiz_question(request)

def quiz_results(request):
    questions = list(QuizQuestion.objects.order_by('id'))
    answers = _session_answers(request)
    correct, wrong = _counts(questions, answers)
    total = len(questions)
    details = []
    for q in questions:
        sel = answers.get(str(q.id))
        details.append({
            'id': q.id,
            'pregunta': q.pregunta,
            'selected': sel,
            'correcta': q.respuesta_correcta,
            'is_correct': sel == q.respuesta_correcta,
        })
    score = int((correct / total) * 100) if total else 0
    return render(request, 'quizzes/partials/results.html', {
        'test_name': 'Prueba Técnica de Django',
        'total_questions': total,
        'correct_count': correct,
        'wrong_count': wrong,
        'score': score,
        'details': details,
    })
