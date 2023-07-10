from django.shortcuts import render, redirect
from .forms import QuotationForm

def create_quotation(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quotation_success')
    else:
        form = QuotationForm()
    
    return render(request, 'tenderbillproject/create_quote.html', {'form' : form})