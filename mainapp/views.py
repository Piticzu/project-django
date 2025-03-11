from django.shortcuts import render
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def chatgpt_view(request):
    context = {}

    if request.htmx or request.method == 'POST':
        prompt = request.POST.get('prompt')

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            print(response)
            context['response'] = response.choices[0].message.content
        except Exception as e:
            context['error'] = str(e)

    return render(request, 'chat.html', context)