from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from .forms import ContactForm  # Импортируем форму
from django.http import HttpResponse

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            return HttpResponse("Форма отправлена!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
