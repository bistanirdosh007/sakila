from django.db import models

# Actor table
class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'actor'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Address table
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    
    class Meta:
        db_table = 'address'

    def __str__(self):
        return self.address


# Category table
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


# City table
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    
    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.city


# Country table
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.country


# Customer table
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    active = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Film table
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='films')
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.IntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=5, blank=True, null=True)
    special_features = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title


# FilmActor junction table
class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        unique_together = ('actor', 'film')


# FilmCategory junction table
class FilmCategory(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        unique_together = ('film', 'category')


# Inventory table
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return f"Inventory {self.inventory_id}"


# Language table
class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


# Payment table
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f"Payment {self.payment_id}"


# Rental table
class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'rental'

    def __str__(self):
        return f"Rental {self.rental_id}"


# Staff table
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Store table
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='managed_store')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'store'

    def __str__(self):
        return f"Store {self.store_id}"
