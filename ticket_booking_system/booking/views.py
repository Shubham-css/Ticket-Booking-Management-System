from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import Show
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import HttpResponseBadRequest
from .models import Show
from .models import Booking

class HomeView(TemplateView):
    template_name = 'booking/home.html'

class RegisterView(View):
    def get(self, request):
        return render(request, 'booking/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([username, email, password1, password2]):
            messages.error(request, "All fields are required.")
            return render(request, 'booking/register.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'booking/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'booking/register.html')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'booking/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')  # or any other page like 'shows'
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'booking/login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect('login')

class ShowListView(ListView):
    model = Show
    template_name = 'booking/show_list.html'
    context_object_name = 'shows'


class ShowDetailView(View):
    def get(self, request, *args, **kwargs):
        show = Show.objects.get(pk=kwargs['pk'])
        return render(request, 'booking/show_detail.html', {'show': show})

    def post(self, request, *args, **kwargs):
        show = Show.objects.get(pk=kwargs['pk'])
        quantity = int(request.POST.get('quantity', 0))
        if request.user.is_authenticated:
            Booking.objects.create(
                user=request.user,
                show=show,
                quantity=quantity
    )
        if quantity <= 0 or quantity > show.available_seats:
            messages.error(request, "Invalid quantity.")
            return redirect('show_detail', pk=show.pk)

        bookings = request.session.get('bookings', [])
        bookings.append({
            'show_id': show.id,
            'title': show.title,
            'quantity': quantity,
        })
        request.session['bookings'] = bookings

        show.available_seats -= quantity
        show.save()

        return render(request, 'booking/booking_confirm.html', {
            'title': show.title,
            'quantity': quantity,
        })

class BookingHistoryView(View):
    def get(self, request):
        bookings = request.session.get('bookings', [])
        return render(request, 'booking/booking_history.html', {'bookings': bookings})
    
class AdminShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'booking/admin_show_list.html', {'shows': shows})

class AdminAddShowView(View):
    def get(self, request):
        return render(request, 'booking/admin_add_show.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        seats = request.POST.get('available_seats')

        Show.objects.create(
            title=title,
            description=description,
            date=date,
            time=time,
            available_seats=int(seats)
        )
        return redirect('admin_show_list')

class AdminEditShowView(View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request, 'booking/admin_edit_show.html', {'show': show})

    def post(self, request, pk):
        show = Show.objects.get(pk=pk)
        show.title = request.POST.get('title')
        show.description = request.POST.get('description')
        show.date = request.POST.get('date')
        show.time = request.POST.get('time')
        show.available_seats = int(request.POST.get('available_seats'))
        show.save()
        return redirect('admin_show_list')

class AdminDeleteShowView(View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request, 'booking/admin_delete_show.html', {'show': show})

    def post(self, request, pk):
        show = Show.objects.get(pk=pk)
        show.delete()
        return redirect('admin_show_list')

class AdminBookingListView(View):
    def get(self, request):
        bookings = Booking.objects.select_related('user', 'show').order_by('-booking_time')
        return render(request, 'booking/admin_booking_list.html', {'bookings': bookings})