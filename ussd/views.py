from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def ussd_callback(request):
  session_id = request.POST.get('sessionId', None)
  service_code = request.POST.get('serviceCode', None)
  phone_number = request.POST.get('phoneNumber', None)
  text = request.POST.get('text', '')

  if text == '':
    response = "CON What would you like to do?\n"
    response += "1. Check my account\n"
    response += "2. Check my balance\n"
    response += "3. Django works"
  elif text == '1':
    response = "END Your account number is 123456"
  elif text == '2':
    response = "END Your balance is KES 1000"
  elif text == '3':
    response = "END Django really works."
  else:
    response = "END Invalid option"

  return HttpResponse(response, content_type='text/plain')
