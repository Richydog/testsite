from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
'''
Category
=========
title, slug

Tag
=========
title, slug

Post
=========
title, slug, author, content, created_at, photo, views, category, tags
'''


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True)
    #author = models.CharField(max_length=75, verbose_name='aвтор',blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,related_name='posts', verbose_name='Автор')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['created_at']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/%Y/%m/%d/')

    def __str__(self):
        return f'{self.user.username} Profile'

   # def save(self):
    #    super().save()

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Comments(models.Model):
    article = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name='Статья', blank = True, null = True,
                                related_name='comments_post' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор комментария', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)
