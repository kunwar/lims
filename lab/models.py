from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='M')
    date_visited = models.DateTimeField()

    def __str__(self):
        return self.name


class CompleteBloodCount(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    haemoglobin = models.DecimalField(max_digits=4, decimal_places=2)
    tlc = models.IntegerField()
    neutrophils = models.IntegerField()
    lymphocytes = models.IntegerField()
    monocytes = models.IntegerField()
    eosinophils = models.CharField(max_length=2, default=None)
    basophils = models.CharField(max_length=2, default=None)
    platelets = models.DecimalField(max_digits=3, decimal_places=2)
    rbc = models.DecimalField(max_digits=4, decimal_places=2)
    hct = models.DecimalField(max_digits=4, decimal_places=2)
    mcv = models.DecimalField(max_digits=4, decimal_places=2)
    mch = models.DecimalField(max_digits=4, decimal_places=2)
    mchc = models.DecimalField(max_digits=4, decimal_places=2)
    rdw_cv = models.DecimalField(max_digits=4, decimal_places=2)
    mpv = models.DecimalField(max_digits=4, decimal_places=2)
    pdw = models.DecimalField(max_digits=4, decimal_places=2)
    pct = models.DecimalField(max_digits=4, decimal_places=3)
    lymph = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.patient.name


class LiverFunctionTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sgot = models.IntegerField()
    sgpt = models.IntegerField()
