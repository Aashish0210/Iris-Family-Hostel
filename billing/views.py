from decimal import Decimal, ROUND_HALF_UP
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError, transaction
from .forms import GenerateInvoicesForm
from .models import Invoice
from kids.models import Kid

def staff_required(view_func):
    return user_passes_test(lambda u: u.is_active and u.is_staff)(view_func)

@login_required
@staff_required
def invoice_list(request):
    invoices = Invoice.objects.select_related('kid').all()
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
@staff_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'billing/invoice_detail.html', {'invoice': invoice})

@login_required
@staff_required
def generate_invoices(request):
    if request.method == 'POST':
        form = GenerateInvoicesForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            amount = form.cleaned_data['amount']
            vat_rate = form.cleaned_data['vat_rate']

            kids = Kid.objects.filter(active=True).order_by('name')
            created = 0
            skipped = 0
            with transaction.atomic():
                for kid in kids:
                    # compute total = amount + VAT
                    total = (Decimal(amount) * (Decimal('1') + Decimal(vat_rate)/Decimal('100'))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    inv = Invoice(kid=kid, month=month, year=year, amount=amount, vat_rate=vat_rate, total=total)
                    try:
                        inv.save()
                        created += 1
                    except IntegrityError:
                        skipped += 1
                        continue
            messages.success(request, f'Generated {created} invoices. Skipped {skipped} (already existed).')
            return redirect('invoice_list')
    else:
        form = GenerateInvoicesForm()
    return render(request, 'billing/generate_invoices.html', {'form': form})
