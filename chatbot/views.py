from django.http import JsonResponse
import random

def chatbot_response(request):
    responses = [
         "Hello, how can I assist you?",
         "Good to see you! How can I help you today?",
         "What would you like to know?",
         "Ask me anything!",
    ]
    response = random.choice(responses)
    return JsonResponse({'response': response})

# Create your views here.
