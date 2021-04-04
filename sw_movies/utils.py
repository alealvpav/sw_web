import os
import uuid
from django.utils.text import slugify

from sw_web.settings import MEDIA_ROOT


def get_file_path(instance, filename):
    """
    This function returns the upload path for any file (image) which will depend on the
    type of the instance object
    :param instance: The instance of the object containing the file (image). Type: obj
    :param filename: File (image) filename. Type: str
    :return: Path to upload the file (image). Type: str
    """
    from sw_movies.models import CharacterImage, Film

    name = slugify(filename.split(".")[0])[:200]
    extension = filename.split(".")[-1]

    # Rename the image using the original name (without dots in case it has more than
    # the mandatory one for the file extension) + some format
    filename = "{}-{}.{}".format(name, uuid.uuid4(), extension)

    if isinstance(instance, Film):
        return os.path.join(
            MEDIA_ROOT, "films", "{}-{}".format(instance.get_slug_title(), filename)
        )
    if isinstance(instance, CharacterImage):
        return os.path.join(
            MEDIA_ROOT,
            "characters",
            "{}-{}".format(instance.character.get_slug_name(), filename),
        )
    else:
        return os.path.join("other_files", filename)
