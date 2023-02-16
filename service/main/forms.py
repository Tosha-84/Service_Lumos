from .models import Project, Employee, Props, Order
from django.forms import ModelForm, TextInput, Textarea, FileInput, URLInput, NumberInput, CheckboxInput, DateInput,\
    TimeInput, DateTimeInput


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "base_cost", "avatar", "employee", "props"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите название"
            }),
            "base_cost": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите стоимость"
            }),
            "avatar": FileInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Загрузите аватарку"

            }),

        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "surname", "patronymic", "phone", "vk_link", "telegram_link", "avatar"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите имя"
            }),
            "surname": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите фамилию"
            }),
            "patronymic": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите отчество"
            }),
            "phone": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите номер телефона"
            }),
            "vk_link": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите сслыку на страницу ВК"
            }),
            "telegram_link": URLInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите ссылку на аккаунт telegram"
            }),
            "avatar": FileInput(attrs={
                'class': 'avatar-employee-in-add-employee',
                'placeholder': "Загрузите аватарку"

            }),
        }


class PropsForm(ModelForm):
    class Meta:
        model = Props
        fields = ["name", "state", "avatar"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Введите название"
            }),
            "state": CheckboxInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Укажите целостность (да - выделено)"
            }),
            "avatar": FileInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': "Загрузите аватарку"

            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'time', "place", "customer", "employee", "realization", 'phone', 'realization']
        widgets = {
            'place': TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': 'Введите адрес',
            }),
            'customer': TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': 'Введите ФИО заказчика',
            }),
            'phone': TextInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': 'Введите номер телефона заказчика',
            }),
            'date': DateInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': 'Введите мать его дату',
            }),
            'time': TimeInput(attrs={
                'class': 'field-in-add-project',
                'placeholder': 'Введите мать его дату',
            }),
        }

