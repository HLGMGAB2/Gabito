from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

class User(User):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('family', 'Family Member'),
        ('visitor', 'Visitor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='visitor')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"


class Memorial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    # image = models.ImageField(upload_to='memorials/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('memorial_detail', args=[str(self.id)])


class MemorialPage(models.Model):
    title = models.CharField(max_length=255)
    deceased_first_name = models.CharField(max_length=100)
    deceased_last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    biography = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Family member or admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    memorial_slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Memorial Page for {self.deceased_first_name} {self.deceased_last_name}"

    def get_absolute_url(self):
        return reverse("memorialpage_detail", kwargs={"pk": self.pk})

class Tribute(models.Model):
    memorial_page = models.ForeignKey(MemorialPage, on_delete=models.CASCADE, related_name='tributes')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Author can be family or visitor
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"Tribute by {self.author} on {self.date_posted.strftime('%Y-%m-%d')}"

class Photo(models.Model):
    memorial_page = models.ForeignKey(MemorialPage, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='memorial_photos/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.caption or 'Untitled'} uploaded on {self.uploaded_at.strftime('%Y-%m-%d')}"

class VisitorComment(models.Model):
    memorial_page = models.ForeignKey(MemorialPage, on_delete=models.CASCADE, related_name='visitor_comments')
    visitor_name = models.CharField(max_length=255)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.visitor_name} on {self.posted_at.strftime('%Y-%m-%d')}"

class MemorialPageSettings(models.Model):
    memorial_page = models.OneToOneField(MemorialPage, on_delete=models.CASCADE, related_name='settings')
    is_public = models.BooleanField(default=True)
    allow_tributes = models.BooleanField(default=True)
    allow_photos = models.BooleanField(default=True)
    custom_theme_color = models.CharField(max_length=7, blank=True)
    def __str__(self):
        return f"Settings for {self.memorial_page.title}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memorial_page = models.ForeignKey(MemorialPage, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} on {self.date_sent.strftime('%Y-%m-%d')}"
