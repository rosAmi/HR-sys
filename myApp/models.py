from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    created = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    details = models.TextField(blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.name)


class Applicant(models.Model):  # Candidate
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    job_id = models.CharField(max_length=50, default="0")
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=10)
    linkedin_profile = models.URLField()
    personal_website = models.URLField()
    personal_note = models.TextField()
    resume = models.FileField()
#     # cover_letter = models.FileField()
#     # portfolio = models.FileField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
