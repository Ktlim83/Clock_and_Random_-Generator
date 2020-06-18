from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def get_random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['word'] = get_random_string(length=22)
    request.session['count'] += 1
    return render(request, 'random_word_index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')