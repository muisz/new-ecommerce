from django.db import models

class Items(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.TextField()
    rating = models.FloatField(default=0)
    stock = models.IntegerField(default = 10)
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "items"

class ItemMedia(models.Model):
    item_id = models.IntegerField()
    media = models.FileField(upload_to="item/%Y/%m/")

    class Meta:
        db_table = "item_media"

class ItemVariants(models.Model):
    item_id = models.IntegerField()
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = "item_variants"

class ItemReviews(models.Model):
    item_id = models.IntegerField()
    customer_id = models.IntegerField()
    review = models.TextField()
    rating = models.FloatField()
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "item_reviews"

class ItemAdditionalInfo(models.Model):
    item_id = models.IntegerField()
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = "item_additional_info"

class ItemQuestions(models.Model):
    item_id = models.IntegerField()
    customer_id = models.IntegerField()
    question_id = models.IntegerField(null = True, blank=True)
    text = models.TextField()
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "item_questions"

class ItemCategories(models.Model):
    category_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        db_table = "item_categories"

class Categories(models.Model):
    shop_id = models.IntegerField()
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"

class Shops(models.Model):
    customer_id = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(null = True, blank = True)
    url = models.CharField(max_length=100)
    rating = models.FloatField()
    date_created = models.DateField(auto_now_add = True)
    time_created = models.TimeField(auto_now_add = True)

    class Meta:
        db_table = "shops"

class Orders(models.Model):
    item_id = models.IntegerField()
    customer_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    pre_total = models.FloatField()
    total = models.FloatField()
    any_subtraction = models.BooleanField(default = False)
    subtraction_total = models.FloatField(default=0)
    status = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_status_update = models.DateTimeField()
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"

class OrderStatus(models.Model):
    order_id = models.IntegerField()
    status = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_status"

class Promo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.FloatField()
    is_percent = models.BooleanField(default=False)
    start_date = models.DateField()
    start_time = models.TimeField()
    exp_date = models.DateField()
    exp_time = models.TimeField()
    suplier = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = "promo"

class Vouchers(models.Model):
    code = models.CharField(max_length=100, unique=True)
    value = models.FloatField()
    is_percent = models.BooleanField(default=False)
    start_date = models.DateField()
    start_time = models.TimeField()
    exp_date = models.DateField()
    exp_time = models.TimeField()
    suplier = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = "vouchers"

class OrderSubtractions(models.Model):
    order_id = models.IntegerField()
    name = models.CharField(max_length=100)
    value = models.FloatField()
    is_voucher = models.BooleanField(null=False)

    class Meta:
        db_table = "order_suctractions"

class PaymentMethods(models.Model):
    name = models.CharField(max_length=100, unique=True)
    account_number = models.CharField(max_length=100)
    is_cod = models.BooleanField(default=False)
    fee = models.FloatField()

    class Meta:
        db_table = "payment_methods"