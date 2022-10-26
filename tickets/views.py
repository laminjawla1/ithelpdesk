from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from tickets.models import Expert, Ticket
from feedback.models import Feedback
from django.contrib import messages
import time
# Create your views here.


def get_pending_tickets(tickets):
    t = 0
    for ticket in tickets:
        if ticket.cycle == "Pending":
            t += 1
    return f"{t:,}"


def get_open_tickets(tickets):
    t = 0
    for ticket in tickets:
        if ticket.cycle == "Open":
            t += 1
    return f"{t:,}"


def get_progress_tickets(tickets):
    t = 0
    for ticket in tickets:
        if ticket.cycle == "Progress":
            t += 1
    return f"{t:,}"


def get_closed_tickets(tickets):
    t = 0
    for ticket in tickets:
        if ticket.cycle == "Closed":
            t += 1
    return f"{t:,}"


@login_required
def index(request):
    tickets = Ticket.objects.all()
    tickets_booked = len(tickets)
    tickets_pending = get_pending_tickets(tickets)
    tickets_open = get_open_tickets(tickets)
    tickets_progress = get_progress_tickets(tickets)
    tickets_closed = get_closed_tickets(tickets)

    items = {
        "tickets_booked": tickets_booked,
        "tickets_pending": tickets_pending,
        "tickets_open": tickets_open,
        "tickets_progress": tickets_progress,
        "tickets_closed": tickets_closed
    }
    experts = Expert.objects.all()
    return render(request, 'index.html', {"items": items, "experts": experts})


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def services(request):
    return render(request, 'services.html')


@login_required
def bookticket(request):
    return render(request, 'bookticket.html')


@login_required
def feedback(request):
    return render(request, 'feedback.html')


@login_required
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(str(name)) > 50:
            messages.info(request, "Name too long")
            return redirect("feedback")
        email = request.POST['email']
        if len(str(email)) > 100:
            messages.info(request, "Invalid Email")
            return redirect("feedback")
        phone = request.POST['phone']
        if len(str(phone)) > 12:
            messages.info(request, "Invalid Phone Number")
            return redirect("feedback")
        message = request.POST['message']
        _time = time.strftime("%H:%M:%S")

        feed = Feedback(name=name, email=email, phone=phone,
                        message=message, time=_time)
        feed.save()
    return render(request, 'submit_feedback.html')


@login_required
def submit_ticket(request):
    if request.method == 'POST':
        zone = request.POST['zone']
        branch = request.POST['branch']
        issue = request.POST['issue']
        date = request.POST['date']
        name = request.user
        phone = request.POST['phone']
        if len(phone) > 12:
            messages.info(request, "Invalid Phone Number")
            return redirect("bookticket")
        anydesk = request.POST['anydesk']
        if len(anydesk) > 9:
            messages.info(request, "Invalid Anydesk Address")
            return redirect("bookticket")
        description = request.POST['description']
        image = request.POST['image']
        _time = time.strftime("%H:%M:%S")
        ticket = Ticket(zone=zone, branch=branch, issue=issue, date=date,
                        name=name, phone=phone, anydesk=anydesk, description=description, image=image, time=_time)

        ticket.save()
    return render(request, 'submit_ticket.html')


@login_required
def search(request):
    return render(request, 'search.html')


@login_required
def search_result(request):
    tickets = Ticket.objects.filter(name__startswith=str(request.user))
    return render(request, "search_result.html", {"tickets": tickets})
