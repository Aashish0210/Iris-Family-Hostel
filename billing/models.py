from django.db import models
from django.utils import timezone
from kids.models import Kid

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]

    kid = models.ForeignKey(Kid, on_delete=models.CASCADE, related_name='invoices')
    month = models.PositiveIntegerField()  # 1-12
    year = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text='VAT % e.g. 13 for 13%')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('kid', 'month', 'year')
        ordering = ['-year', '-month', 'kid__name']

    def __str__(self):
        return f"Invoice {self.month:02d}/{self.year} - {self.kid.name}"
