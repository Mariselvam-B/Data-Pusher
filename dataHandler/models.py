from django.db import models
import uuid

class Account(models.Model):
    account_id = models.CharField(max_length=255, unique=True, primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.account_id

class Destination(models.Model):
    destination_id = models.CharField(max_length=255, unique=True, primary_key=True, default=uuid.uuid4)
    account_id = models.ForeignKey(Account, related_name='destinations', on_delete=models.CASCADE)
    url =  models.CharField(max_length=255)
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

class Incoming(models.Model):
    incoming_id = models.CharField(max_length=255, unique=True, primary_key=True, default=uuid.uuid4)
    destination_id = models.ForeignKey(Destination, related_name='incomings', on_delete=models.CASCADE)
    data = models.TextField()

    def __str__(self):
        return self.data
