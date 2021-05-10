from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

"""
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class Post:
    def __int__(self, request):
        if request.method == 'POST':
            message_name = request.Post['message-name']
            message_email = request.Post['message-email']
            message = request.Post['message']
            return render(request, 'contact.html', {})
        else:
            return render(request, 'contact.html', {})


class ContactPageView(TemplateView):
    model = Post
    template_name = 'contact.html'


class ServicePageView(TemplateView):
    template_name = 'service.html'


class PricingPageView(TemplateView):
    template_name = 'pricing.html'
"""


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,
            message,
            message_email,
            ['deinmodeiwaterway@gmail.com'],
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        # send an email
        appoint = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " \
                  + your_address + " Schedule: " + your_schedule + " Date: " + your_date + " Message: " + your_message
        send_mail(
            'Appointment Request',  # subject
            appoint,  # message
            your_email,  # from
            ['deinmodeiwaterway@gmail.com'],    # To Email
        )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message})
    else:
        return render(request, 'home.html', {})
