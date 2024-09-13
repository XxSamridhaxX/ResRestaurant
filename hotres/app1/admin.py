from django.contrib import admin
from .models import Customer, Table, Reservation

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')
    search_fields = ('table_number',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'reservation_date', 'reservation_time', 'number_of_guests')
    search_fields = ('customer__first_name', 'customer__last_name')
    list_filter = ('reservation_date', 'table')
