from django.db import models

# Create your models here.
class Position(models.Model):
    position_name = models.CharField(max_length=60, verbose_name='Найменування посади')

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name = 'Посади'
        verbose_name_plural = 'Посади'

class Employee(models.Model):
    name = models.TextField(verbose_name=f'Ім`я')
    surname = models.TextField(verbose_name='Призвище')
    surname_patronymic = models.TextField(verbose_name='По батькові')
    data_admission = models.DateField(verbose_name='Дата прийому')
    email = models.EmailField(verbose_name='Email')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Посада')
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Начальник"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cпівробітник'
        verbose_name_plural = 'Співробітники'

