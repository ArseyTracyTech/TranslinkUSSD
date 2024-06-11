# USSD CODE USING DJANGO 
### HOW TO USE ON REPLIT
1. Signup on replit
2. Create a repl with django template
3. In your repl, open up the shell in replit and type in this command
`pthyon manage.py startapp ussd`
4. A new folder will appear in your repl directory named `ussd`
5. Open the `ussd` folder and in it create a new file named `urls.py`
6. Add this code below in the `urls.py` file you created on replit.
```
from django.urls import path
from .views import ussd_callback

urlpatterns = [
    path('ussd/', ussd_callback, name='ussd'),
]

```

7. Copy the code in `views.py` **code is provided in the github repl of this project**  and paste in your `views.py` in replit
8. Then in the django_project folder there is another urls.py file, open it and make some changes in, for reference, look at my urls.py file in the ussdproject folder make sure you edit this section in your code as provided below
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ussd.urls')),
]
```
After run your code, point your app to ussd/ and hit enter in the urlbar of replit "it's in a green text at the top right when the webview loads." click on the that link the one in the green text and copy it.
then on africastalking set as the call back urland don't forget to point your app to ussd save the changes and test your code.

