# Arquivo: tasks/admin.py
from django.contrib import admin
from .models import Task

class ListTask(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'priority', 'created_at_formatado', )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user__username', 'priority', 'status')
    list_filter=('status', 'priority', )
    list_editable = ('status', 'priority', )
    list_select_related = True
    list_per_page = 10

    def created_at_formatado(self, obj):
        if obj.created_at:
            dias_semana = {
            0: 'Segunda-feira',
            1: 'Terça-feira',
            2: 'Quarta-feira',
            3: 'Quinta-feira',
            4: 'Sexta-feira',
            5: 'Sábado',
            6: 'Domingo',
        }
            dia_semana = dias_semana[obj.created_at.weekday()]
            data_hora = obj.created_at.strftime('%d/%m/%Y %H:%M')
            return f'{dia_semana} - {data_hora}'
        return '-'
    created_at_formatado.short_description = 'Data Cadastro'
    created_at_formatado.admin_order_field = 'created_at'

admin.site.register(Task, ListTask)




