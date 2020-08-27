from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(
        verbose_name='Created', auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(verbose_name='modified', auto_now=True)

    class Meta:
        abstract = True


class Movie(TimeStampedModel):
    tittle = models.CharField(max_length=255, null=True, default=None)
    year = models.IntegerField()
    rating = models.FloatField()
    extra_feild = models.TextField()

    def __str__(self):
        return self.tittle
