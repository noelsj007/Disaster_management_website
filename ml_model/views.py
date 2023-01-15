from django.shortcuts import render,redirect
from disaster_report.forms import DisasterForm

# Create your views here.

def Validate_disaster(request):
    if request.method == 'POST':
        form = DisasterForm(request.POST)
        if form.is_valid():
            form.save()
            print ("Reporting is True")
            validation_image = form.cleaned_data.get('images')
            return redirect('home')
        else:
            print ("Reporting is False")
    else:
        
        form = DisasterForm()
    return render(request, 'validate_disaster.html', {'form': form})
