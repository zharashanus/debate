from django.http import JsonResponse
from django.shortcuts import render
import random
from vis_auth.list_of_resolution import list

def random_topic(request):
    topics = list  # Assuming 'list' is a list of topics
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        selected_topic = random.choice(topics)
        return JsonResponse({'topic': selected_topic})
    context = {'user': request.user}
    return render(request, 'random_topic.html', context)