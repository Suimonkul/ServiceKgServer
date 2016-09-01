# Create your views here
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Advertisement


@csrf_exempt
def post_register(request):
    try:
        name = request.POST.get("name")
        title = request.POST.get("title")
        description = request.POST.get("description")
        phone = request.POST.get("phone")
        phone_two = request.POST.get("phone_two")
        phone_three = request.POST.get("phone_three")
        order = request.POST.get("order")
        category_id = request.POST.get("category_id")
        position = request.POST.get("position")

        post_request = Advertisement.objects.create(name=name, title=title, description=description, phone=phone,
                                                    phone_two=phone_two, phone_three=phone_three, order=order,
                                                    position=position, category_id=category_id)

        post_request.save()
        return JsonResponse(dict(result="OK"))
    except:
        return JsonResponse(dict(result="ERROR"))
