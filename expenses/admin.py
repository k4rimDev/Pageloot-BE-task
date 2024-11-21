from django.contrib import admin

from expenses.models import User, Expense


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = list_display


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "amount", "category", "date")
    search_fields = ("title", "amount", "category")
    list_filter = ("category", )
