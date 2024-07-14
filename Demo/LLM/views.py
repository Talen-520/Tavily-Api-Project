from django.http import JsonResponse
from rest_framework.decorators import api_view
from .chatAPI import get_response

@api_view(['POST'])
def chat(request):
    company = request.data.get('company', '')
    quarter = request.data.get('quarter', '')
    year = request.data.get('year', '')
    
    user_input = f'{company} Q{quarter} {year} earning report'
    data = get_response(user_input)
    return JsonResponse(data, safe=False)