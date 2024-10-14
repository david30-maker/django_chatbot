from django.http import JsonResponse
import random

def chatbot_response(request):
    user_message = request.GET.get('message', '')
    responses = [
        "Hello, how can I assist you?",
        "I'm here to help!",
        "What would you like to know?",
        "Ask me anything!"
    ]
    return JsonResponse({'response': random.choice(responses)})
