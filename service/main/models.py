import datetime

from django.db import models
from django.core.validators import RegexValidator


# Сотрудники
class Employee(models.Model):
    # Номер телефона, разобраться, какой тип данных использовать
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=12, unique=True)
    name = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30, null=True, blank=True)
    login = models.CharField("Логин", max_length=30, null=True, blank=True, unique=True)
    password = models.CharField("Пароль", max_length=30, null=True, blank=True)
    vk_link = models.SlugField("Ссылка на Вк", max_length=30, null=True, blank=False)
    telegram_link = models.SlugField("Пароль", max_length=30, null=True, blank=True)
    avatar = models.ImageField("Аватарка", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

    def get_absolute_url(self):
        return '/employees'

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Task(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField("Описание", null=True, blank=True)
    comment = models.TextField("Комментарий", null=True, blank=True)

    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")

    major = models.OneToOneField(Employee, verbose_name="Назначивший", on_delete=models.SET_NULL, null=True)

    employee = models.ManyToManyField(Employee, verbose_name="Ответственные", related_name="Task_Employee")

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Props(models.Model):
    name = models.CharField("Название", max_length=50)
    state = models.BooleanField("Состояние", default=True)
    comment = models.BooleanField("Комментарий", null=True, blank=True)
    avatar = models.ImageField("Аватарка", null=True, blank=True)

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/props'

    class Meta:
        verbose_name = "Реквизит"
        verbose_name_plural = "Реквизит"


class Order(models.Model):
    # datetime = models.DateTimeField("Дата и время")
    date = models.DateField("Дата", default=datetime.date.today)
    time = models.TimeField("Время", default=datetime.time)
    place = models.CharField("Адрес", max_length=60)
    customer = models.CharField("ФИО Заказчика", max_length=50)

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=12)
    comment = models.TextField("Комментарий", null=True, blank=True)

    realization = models.BooleanField(null=True, blank=True, default=False)

    employee = models.ManyToManyField(Employee, verbose_name="Работники", related_name="Order_Employee",
                                      null=True, blank=True)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Project(models.Model):
    name = models.CharField("Название", max_length=30)
    base_cost = models.SmallIntegerField("Стоимость")
    avatar = models.ImageField("Аватарка", upload_to="project's avatars", null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)


    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url


    task = models.ForeignKey(
        Task, verbose_name="Задачи", related_name="Project_Task", on_delete=models.SET_NULL, null=True, blank=True
    )

    employee = models.ManyToManyField(Employee, verbose_name="Сотрудники", related_name="Project_Employee",
                                      null=True, blank=True)

    props = models.ManyToManyField(Props, verbose_name="Реквизит", related_name="Project_Props",
                                   null=True, blank=True)

    order = models.ManyToManyField(Order, verbose_name="orders", related_name="Project_Order",
                                   null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/projects/{self.id}'

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
