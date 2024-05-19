from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    email = models.EmailField(max_length=150, verbose_name='email')
    password = models.CharField(max_length=150, verbose_name='password')
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='avatar', null=True, blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


