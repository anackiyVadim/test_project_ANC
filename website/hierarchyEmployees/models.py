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
    surname_patronymic = models.TextField(verbose_name='Побатькові')
    data_admission = models.DateField(verbose_name='Дата прийому')
    email = models.EmailField(verbose_name='Email')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Посада')
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
        verbose_name="Начальник"
    )
    level = models.IntegerField(default=1, verbose_name="Рівень ієрархії")

    def save(self, *args, **kwargs):
        if self.supervisor:
            self.level = self.supervisor.level + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Співробітник"
        verbose_name_plural = "Співробітники"
        ordering = ['name']



