from django.urls import path
from .views import HomeView, RegisterView, LoginView, LogoutView
from .views import ShowListView
from .views import ShowDetailView
from .views import BookingHistoryView
from .views import AdminShowListView
from .views import AdminAddShowView
from .views import AdminEditShowView
from .views import AdminDeleteShowView
from .views import AdminBookingListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('shows/', ShowListView.as_view(), name='show_list'),
    path('shows/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),
    path('bookings/', BookingHistoryView.as_view(), name='booking_history'),
    path('admin-panel/shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('admin-panel/shows/add/', AdminAddShowView.as_view(), name='admin_add_show'),
    path('admin-panel/shows/<int:pk>/edit/', AdminEditShowView.as_view(), name='admin_edit_show'),
    path('admin-panel/shows/<int:pk>/delete/', AdminDeleteShowView.as_view(), name='admin_delete_show'),
    path('admin-panel/bookings/', AdminBookingListView.as_view(), name='admin_booking_list'),
]
