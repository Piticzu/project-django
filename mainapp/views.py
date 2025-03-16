# views.py
import openai
import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI


@require_GET
def index_view(request):
    return render(request, "index.html")

@csrf_exempt
@require_POST
def send_message_view(request):
    user_message = request.POST.get('message', '')

    client = OpenAI()
    # Get OpenAI response
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
    )

    # Create response HTML
    bot_response = completion.choices[0].message.content
    return HttpResponse(f"""
        <div class="message user-message">{user_message}</div>
        <div class="message bot-message">{bot_response}</div>
    """)