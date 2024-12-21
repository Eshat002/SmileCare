from django.shortcuts import render




def home(request):
    context={'form':ContactForm}
    return render(request, 'home/home.html',context)

def contact_page(request):
    context = {'form': ContactForm()}
    return render(request, 'home/contact.html', context )



from django.http import JsonResponse

def product(request):
    products = [
        {"name": "apple"},
        {"name": "banana"},
        {"name": "cherry"}
    ]
    return JsonResponse({"products": products})



from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return JsonResponse({'message': 'Form submitted successfully!'})
        else:
            # Return the form with errors for HTMX to re-render
            return render(request, 'partials/contact_form.html', {'form': form})

    # Render the form for GET requests
    form = ContactForm()
    return render(request, 'partials/contact_form.html', {'form': form})
