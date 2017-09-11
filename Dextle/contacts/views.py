from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.urls import reverse

def contactsList(request):
    contact_list = Contact.objects.order_by('contact_first_name')
    context = {'contact_list': contact_list}
    return render(request, 'contacts/index.html', context)

def contactsProfile(request):
    return render(request, 'contacts/profile.html')
