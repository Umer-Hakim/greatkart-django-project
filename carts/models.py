from django.db import models
from store.models import Product, Variation



class Cart(models.Model):
    cart_id      = models.CharField(max_length=200, blank=True)
    date_added   = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name        = "cart"
        verbose_name_plural = "carts"


    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    variations    = models.ManyToManyField(Variation, blank=True)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart          = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity      = models.IntegerField()
    is_available  = models.BooleanField(default=True)


    class Meta:
        verbose_name        = "cartitem"
        verbose_name_plural = "cartitems"

    def sub_total(self):
        return self.product.price * self.quantity



    def __unicode__(self):
        return self.product