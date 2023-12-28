from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    membership_status = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    number_plate = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255)
    Client = models.ManyToManyField(Client,related_name="vehicles",through="ApprovalRequest")
    def __str__(self):
        return self.name

class Test(models.Model):
    pass

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=255,decimal_places=2)
    date = models.DateField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="payments")
    def __str__(self):
        return self.client.name
    
class ApprovalRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE,related_name="approval_request")
    def __str__(self):
        return self.client.name

    