from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from .utils import get_file_path


class Character(models.Model):
    """
    This class will represent a SW Character
    """

    name = models.CharField(
        verbose_name="Name", max_length=200, blank=False, null=False
    )

    def get_slug_name(self):
        """
        This function will return a lower non-spaced version of the attribute "name"
        :return: Non-spaced name (Luke Skywalker -> luke_skywalker). Type: str
        """

        return slugify(self.name)

    def get_main_image(self):
        """
        This will return the first image (lower pk) related to this character in case
        it exists. Otherwise it will return the base character image.
        :return:
        """
        return self.characterimage_set.first()


class CharacterImage(models.Model):
    """
    This class will represent a picture of a SW character
    """

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, blank=False, null=False
    )
    image = models.ImageField(verbose_name="Image", upload_to=get_file_path)


class Film(models.Model):
    """
    This class will represent a SW Movie
    """

    title = models.CharField(
        verbose_name="Title",
        max_length=200,
        blank=False,
        null=False,
        default="",
    )
    episode_id = models.IntegerField(
        verbose_name="Episode",
        validators=[MinValueValidator(1)],
        blank=False,
        null=False,
    )
    characters = models.ManyToManyField(
        Character, verbose_name="Characters", blank=True
    )
    director = models.CharField(
        verbose_name="Director",
        max_length=200,
        blank=False,
        null=False,
        default="",
    )
    image = models.ImageField(
        verbose_name="Image",
        blank=True,
        null=True,
        upload_to=get_file_path,
    )

    def get_slug_title(self):
        """
        This function will return a lower non-spaced version of the attribute "title"
        :return: Non-spaced title (Star Wars -> star-wars). Type: str
        """

        return slugify(self.title)
