from django.shortcuts import render
from .models import Comments
from recaptcha import recaptcha_check

from .forms import CommentForm


def index(request):
    comments = Comments.objects.all()
    comment_form = CommentForm(request.POST or None)
    recaptcha_response = request.POST.get('g-recaptcha-response')
    recaptcha_response_result = recaptcha_check(recaptcha_response)
    if recaptcha_response_result is True and comment_form.is_valid():
        comment_form.save()
    context = {
        'form': comment_form,
        'comments': comments
    }
    return render(request, 'index.html', context)
