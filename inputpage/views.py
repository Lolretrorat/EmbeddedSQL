# views.py
from django.shortcuts import render, redirect
from .forms import AddressForm, PatientForm, PractitionerForm, ServiceForm, ConsultationForm

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')  # Redirect to the same page after submission
    else:
        form = AddressForm()
    return render(request, 'inputpage/add_data.html', {'form': form})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = PatientForm()
    return render(request, 'inputpage/add_data.html', {'form': form})

def add_practitioner(request):
    if request.method == 'POST':
        form = PractitionerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = PractitionerForm()
    return render(request, 'inputpage/add_data.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = ServiceForm()
    return render(request, 'inputpage/add_data.html', {'form': form})

def add_consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = ConsultationForm()
    return render(request, 'inputpage/add_data.html', {'form': form})
