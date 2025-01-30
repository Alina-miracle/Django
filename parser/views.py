from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.send_email()  # Логика отправки
        return super().form_valid(form)
