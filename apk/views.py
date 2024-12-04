from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Set OpenAI API key
openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def chatbot(request):
    if request.method == 'GET':
        return render(request, 'chatbot.html')  # Just renders the page for GET request

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            # Making the call to OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4",  # You can use other models too (gpt-3.5-turbo, etc.)
                messages=[{"role": "user", "content": user_message}],
                max_tokens=150
            )

            chatbot_reply = response['choices'][0]['message']['content'].strip()
            return JsonResponse({'response': chatbot_reply})

        except Exception as e:
            return JsonResponse({'response': f"Error: {str(e)}"})

    return JsonResponse({'response': 'Invalid request method'}, status=405)
