from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .models import Contact

def home(request):
    context={'form':ContactForm}
    return render(request, 'home/home.html',context)



def contact_page(request):
    context = {'form': ContactForm()}
    return render(request, 'home/contact.html', context )




def product(request):
    products = [
        {"name": "apple"},
        {"name": "banana"},
        {"name": "cherry"}
    ]
    return JsonResponse({"products": products})



 
#model form view
def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database automatically
            form.save()

            # Return a success message for HTMX
            # if request.htmx:
            #     return JsonResponse({'message': 'Form submitted successfully!'})

            # For non-HTMX requests, render a success page
            return render(request, 'partials/success_message.html', {'name': 'eshat!'})

        # If form is invalid, re-render with errors
        if request.htmx:
            return render(request, 'partials/contact_form.html', {'form': form})
        return render(request, 'contact.html', {'form': form})

    # For GET requests, render an empty form
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})



#regular form view
 
# def contact_form_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database manually
#             name = form.cleaned_data['name']
#             phone = form.cleaned_data['phone']
#             Contact.objects.create(name=name, phone=phone)

#             # Return a success message for HTMX or render success page
#             if request.htmx:
#                 return JsonResponse({'message': 'Form submitted successfully!'})
#             return render(request, 'success.html', {'message': 'Form submitted successfully!'})

#         # If form is invalid, re-render the form with errors
#         if request.htmx:
#             return render(request, 'partials/contact_form.html', {'form': form})
#         return render(request, 'contact.html', {'form': form})

#     # For GET requests, render an empty form
#     form = ContactForm()
#     return render(request, 'contact.html', {'form': form})
