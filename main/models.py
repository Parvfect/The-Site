from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    

class StoryCategory(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    slug = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = "Story Categories"

    def __str__(self):
        return self.name


class Story(models.Model):
    category = models.ForeignKey(StoryCategory, default=1, verbose_name="Story Category", on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    content = models.TextField()
    date = models.DateField('date published')
    slug = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.name


class Imp(models.Model):
    name = models.CharField(max_length = 200)
    sub = models.TextField(null = True, blank = True)
    number = models.IntegerField(default = 100)
    status = models.BooleanField()


    class Meta:
        verbose_name_plural = "Impossible List"

    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

class ReadingList(models.Model):
    name = models.CharField(max_length = 200)
    summary = models.TextField()
    img = models.FileField(null = True, blank = True)
    link = models.URLField()


    class Meta:
        verbose_name_plural = "Reading List"

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    img = models.ImageField(null = True, blank = True)

    class Meta:
        verbose_name_plural = "Studio"
    
    def __str__(self):
        return self.name