# views.py
from .utils import call_gpt
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

def scroll_anchor_view(request):
    return HttpResponse()

@require_GET
def index_view(request):
    return render(request, "index.html")

@csrf_exempt
@require_POST
def send_message_view(request):
    user_message = request.POST.get('message', '')
    bot_response = call_gpt(user_message)

    return HttpResponse(f"""
        <div class="flex justify-end">
            <div class="bg-neutral-700 text-white px-4 py-2 rounded-l-full rounded-tr-full max-w-xs">
                {user_message}
            </div>
        </div>
        <div class="text-left text-white">{bot_response}</div>

        <script>
            const form = document.querySelector('form');
            if (form) {{
                form.reset();
                form.querySelector('input[name=message]').focus();
            }}
        </script>
    """)