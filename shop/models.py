from django.db import models
from django.contrib.auth.models import AbstractUser

# CustomUser Model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Add unique related_name to prevent clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Change related_name to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Change related_name to avoid clash
        blank=True
    )

# Order Model
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    design_service = models.ForeignKey('services.DesignService', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
