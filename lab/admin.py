from django.contrib import admin

from .models import Patient, CompleteBloodCount, LiverFunctionTest


class CompleteBloodCountAdmin(admin.StackedInline):
    model = CompleteBloodCount
    extra = 0


class LiverFunctionTestAdmin(admin.TabularInline):
    model = LiverFunctionTest
    extra = 0


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'date_visited')

    inlines = [CompleteBloodCountAdmin, LiverFunctionTestAdmin]


admin.site.register(Patient, PatientAdmin)
