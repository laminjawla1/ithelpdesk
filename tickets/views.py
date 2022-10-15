from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tickets.models import Expert, Ticket
from feedback.models import Feedback
import time
# Create your views here.


# def get_pending_tickets(tickets):
#     t = 0
#     for ticket in tickets:
#         if ticket.cycle == "Pending":
#             t += 1
#     return f"{t:,}"


# def get_open_tickets(tickets):
#     t = 0
#     for ticket in tickets:
#         if ticket.cycle == "Open":
#             t += 1
#     return f"{t:,}"


# def get_progress_tickets(tickets):
#     t = 0
#     for ticket in tickets:
#         if ticket.cycle == "Progress":
#             t += 1
#     return f"{t:,}"


# def get_closed_tickets(tickets):
#     t = 0
#     for ticket in tickets:
#         if ticket.cycle == "Closed":
#             t += 1
#     return f"{t:,}"


@login_required
def index(request):
    # tickets = Ticket.objects.all()
    # tickets_booked = len(tickets)
    # tickets_pending = get_pending_tickets(tickets)
    # tickets_open = get_open_tickets(tickets)
    # tickets_progress = get_progress_tickets(tickets)
    # tickets_closed = get_closed_tickets(tickets)
    # print(f"b-{tickets_booked} p-{tickets_pending} o-{tickets_open} pr-{tickets_progress} c-{tickets_closed}")
    items = {
        "tickets_booked": f"{len(Ticket.objects.all()):,}",
        "tickets_pending": f"{len(Ticket.objects.filter(name__startswith='Pending')):,}",
        "tickets_open": f"{len(Ticket.objects.filter(name__startswith='Open')):,}",
        "tickets_progress": f"{len(Ticket.objects.filter(name__startswith='Progress')):,}",
        "tickets_closed": f"{len(Ticket.objects.filter(name__startswith='Closed')):,}",
    }
    # items = {
    #     "tickets_booked": tickets_booked,
    #     "tickets_pending": tickets_pending,
    #     "tickets_open": tickets_open,
    #     "tickets_progress": tickets_progress,
    #     "tickets_closed": tickets_closed
    # }
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
        email = request.POST['email']
        phone = request.POST['phone']
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
        anydesk = request.POST['anydesk']
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
