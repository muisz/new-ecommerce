from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    picture = models.ImageField(upload_to = 'profile/', null = True, blank = True)
    phone = models.CharField(max_length = 20)
    provinsi = models.CharField(max_length = 100)
    kabupaten = models.CharField(max_length = 100)
    kecamatan = models.CharField(max_length = 100)
    kode_pos = models.CharField(max_length = 5)
    alamat = models.TextField(null = True)
    is_shop_owner = models.BooleanField(default = False)
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "customers"

class Carts(models.Model):
    customer_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "customer_carts"

class Favorites(models.Model):
    customer_id = models.IntegerField()
    item_id = models.IntegerField()
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "customer_favorites"