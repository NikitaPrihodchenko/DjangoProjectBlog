from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=120, unique=True)
    name = models.CharField(max_length=100, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    slug = models.SlugField(max_length=120, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    slug = models.SlugField(max_length=220, unique=True, db_index=True)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    auther = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default=1)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    image = models.URLField(
        default="https://soliloquywp.com/wp-content/uploads/2016/08/How-to-Set-a-Default-Featured-Image-in-WordPress.png")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Коментар')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Коментар від {self.author} до "{self.post.title}"'


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, blank=True)
#     city = models.CharField(max_length=100, blank=True)
#     birth_date = models.DateTimeField(null=True, blank=True)
#     avatar = models.URLField(null=True, blank=True)
#
#     def __str__(self):
#         return f"Profile {self.user.username}"
