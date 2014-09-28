#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter11/djbank/views.py
# A function for each view in our Django application.

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_safe
from .models import Payment, PaymentForm

def make_payment_views(payments, username):
    for p in payments:
        yield {'dollars': p.dollars, 'memo': p.memo,
               'prep': 'to' if (p.debit == username) else 'from',
               'account': p.credit if (p.debit == username) else p.debit}

@require_safe
@login_required
def index_view(request):
    username = request.user.username
    payments = Payment.objects.filter(Q(credit=username) | Q(debit=username))
    payment_views = make_payment_views(payments, username)
    return render(request, 'index.html', {'payments': payment_views})

@require_http_methods(['GET', 'POST'])
@login_required
def pay_view(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        payment = form.save(commit=False)
        payment.debit = request.user.username
        payment.save()
        messages.add_message(request, messages.INFO, 'Payment successful.')
        return redirect('/')
    return render(request, 'pay.html', {'form': form})

@require_safe
def logout_view(request):
    logout(request)
    return redirect('/')
