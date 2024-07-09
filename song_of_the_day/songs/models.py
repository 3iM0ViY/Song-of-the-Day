from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from autoslug import AutoSlugField
from django.utils.text import slugify

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
	slug = AutoSlugField(populate_from='user')

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва категорії")
	slug = AutoSlugField(populate_from='title')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Категорія(ю)"
		verbose_name_plural = "Категорії"
		ordering = ["title"]

class Tag(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва тєгу")
	slug = AutoSlugField(populate_from='title')
	avatar = models.ImageField(upload_to="avatars/%Y/", blank=True, verbose_name="Аватарка")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("tag", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Тег"
		verbose_name_plural = "Теги"
		ordering = ["title"]

def populate_slug(instance):
    return instance.title
def custom_slugify(value):
    return value.replace(' ', '-')

class Song_of_the_Day(models.Model):
	title = models.CharField(verbose_name = "Назва пісні", max_length=150)
	album = models.CharField(verbose_name = "Назва альбому", max_length=150)
	artist = models.CharField(verbose_name = "Назва виконавця", max_length=150)
	cover = models.URLField(verbose_name = "Обкладинка", max_length=500)
	year = models.PositiveSmallIntegerField(verbose_name = "Рік випуску")
	link = models.URLField(verbose_name = "Адреса", max_length=200)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="Дні_пісень", blank=True, verbose_name="Категорія")

	description = models.TextField(verbose_name = "Особистий опис", blank = True)
	emotion = models.CharField(verbose_name = "Емоційка", max_length=10, blank=True)
	day = models.DateField(verbose_name = "День")
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)
	date_added = models.DateTimeField(verbose_name = "Було додано", auto_now_add=True)

	profile = models.OneToOneField(Profile, verbose_name="Профіль", on_delete = models.CASCADE, primary_key=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True, related_name="Дні_пісень", verbose_name="Теги")
	slug = AutoSlugField(populate_from = populate_slug, unique_with = ['day',], slugify = custom_slugify)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("single", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Пісня(ю) дня"
		verbose_name_plural = "Пісні дня"
		ordering = ["profile", "-day"]
