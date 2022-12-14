from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from tickets.models import Expert, Ticket, Branches, Zones
from feedback.models import Feedback
from django.contrib import messages
import time
from datetime import datetime
from .validate import validate_anydesk, validate_email, validate_phone, validate_name


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
    return render(
        request, 'index.html', {"items": items, "experts": experts})


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def services(request):
    return render(request, 'services.html')


@login_required
def bookticket(request):
    branch_list = [item for item in Branches.objects.all().order_by('name')]
    zone_list = [item for item in Zones.objects.all().order_by('name')]
    return render(
        request, 'bookticket.html', {'zone_list': zone_list, 'branch_list': branch_list})


@login_required
def feedback(request):
    return render(request, 'feedback.html')


@login_required
def submit_feedback(request):
    if request.method == 'POST':
        name = validate_name(str(request.POST['name']))
        if name:
            name = name.group(1)
        else:
            messages.info(request, "Invalid Name")
            return redirect("feedback")

        email =validate_email(str(request.POST['email']))
        if email:
            email = email.group(1)
        else:
            messages.info(request, "Invalid Email")
            return redirect("feedback")

        phone = validate_phone(str(request.POST['phone']))
        if phone:
            phone = phone.group(1)
        else:
            messages.info(request, "Invalid Phone Number")
            return redirect("feedback")

        message = request.POST['message']
        _time = time.strftime("%H:%M:%S")

        feed = Feedback(name=name, email=email, phone=phone,
                        message=message, time=_time)
        feed.save()
        return render(request, 'submit_feedback.html')
    else:
        return render(request, 'index.html')


@login_required
def submit_ticket(request):
    if request.method == 'POST':
        zone = request.POST['zone']
        branch = request.POST['branch']
        issue = request.POST['issue']
        date = request.POST['date']
        username = request.user
        date_submitted = datetime.today()
        submitter_name = request.user.get_full_name()
        phone = validate_phone(str(request.POST['phone']))
        if phone:
            phone = phone.group(1)
        else:
            messages.info(request, "Invalid Phone Number")
            return redirect("bookticket")

        anydesk = validate_anydesk(request.POST['anydesk'])
        if anydesk:
            anydesk = anydesk.group(1)
        else:
            messages.info(request, "Invalid Anydesk Address")
            return redirect("bookticket")

        description = request.POST['description']
        image = request.POST['image']
        _time = time.strftime("%H:%M:%S")
        ticket = Ticket(zone=zone, branch=branch, issue=issue, date=date,              date_submitted=date_submitted,username=username, submitter_name=submitter_name, phone=phone, anydesk=anydesk, description=description, image=image, time=_time)

        ticket.save()
        return render(request, 'submit_ticket.html')
    else:
        return render(request, 'index.html')


@login_required
def search(request):
    return render(request, 'search.html')


@login_required
def search_result(request):
    tickets = Ticket.objects.filter(username__startswith=str(request.user))
    return render(request, "search_result.html", {"tickets": tickets})
