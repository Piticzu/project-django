# views.py
from .utils import call_gpt
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

@require_GET
def index_view(request):
    chat_history = request.session.get('chat_history', [])
    return render(request, "index.html", {'chat_history': chat_history})

@csrf_exempt
@require_POST
def send_message_view(request):
    user_message = request.POST.get('message', '')

    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    request.session['chat_history'].append({
        'role': 'user',
        'content' : user_message
    })
    request.session.modified  = True

    html = render_to_string('user_message_block.html', {
        'user_message': user_message,
        'hash' : hash(user_message)
    })

    return HttpResponse(html)
@require_GET
def bot_response_view(request):
    user_message = request.GET.get('message', '')
    bot_response = call_gpt(user_message)

    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    request.session['chat_history'].append({
        'role': 'assistant',
        'content' : bot_response
    })
    request.session.modified  = True

    html = render_to_string('bot_response_block.html', {
        'bot_response': bot_response
    })

    return HttpResponse(html)
