# views.py
from openai import OpenAI

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import linebreaksbr

@require_GET
def index_view(request):
    chat_history = request.session.get('chat_history', [])
    has_chat = len(chat_history) > 0
    return render(request, "index.html", {
        'chat_history': chat_history,
        'has_chat': has_chat
    })

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

    html = render_to_string('partials/user_message.html', {
        'content': user_message,
        'hash' : hash(user_message)
    })

    response = HttpResponse(html)
    response.headers['HX-Trigger'] = "generateBotResponse"

    return response


@require_GET
def bot_response_view(request):
    client = OpenAI()

    # Continue chat history
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=request.session['chat_history'],
    )

    # Add response to chat history
    request.session['chat_history'].append({
        'role': 'assistant',
        'content' : response.choices[0].message.content
    })

    request.session.modified  = True

    html = render_to_string('partials/bot_message.html', {
        'content': linebreaksbr(request.session['chat_history'][-1]['content']),
    })

    return HttpResponse(html)


@csrf_exempt
@require_POST
def clear_chat_view(request):
    request.session['chat_history'] = []
    request.session.modified = True
    html = """
    <div
    id="typing-indicator"
    class="italic text-neutral-400 px-2 hidden [&.htmx-request]:block order-last"
    >
    Assistant is typing...
    </div>
    """

    return HttpResponse(html)
