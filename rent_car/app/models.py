from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class CarModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    count_in_stock = models.IntegerField(null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)

    class Meta:
        db_table = 'Cars'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name


class OrdersModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    lease_start = models.TimeField(null=False, blank=False)
    lease_end = models.TimeField(null=False, blank=False)
    order_time = models.TimeField(null=False, blank=False)

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.user.name + ":" + self.car.name


class CarReviewModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    review = models.TextField(null=False, blank=False)
    star_rating = models.FloatField(null=False, blank=False,
                                    validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_time = models.TimeField(null=False, blank=False)

    class Meta:
        db_table = 'Review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.user.name + ":" + self.car.name
