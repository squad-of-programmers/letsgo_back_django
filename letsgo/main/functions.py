from typing import Union
from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode
import random
import string

def get_random_string(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slugify(instance: models.Model, fields: Union[list, str, set, dict]=None, new_slug=None):
    """
    examples: 
        unique_slugify(self, ['first_name', 'last_name']
        unique_slugify(self, 'title')
    """
    if not new_slug:
        fields_type = type(fields)

        if fields_type == str:
            proto_slug = instance.__getattribute__(fields)
            # filter_fields = {fields: slug}
        
        if fields_type in (list, set):
            fields_values = [instance.__getattribute__(field) for field in fields]
            proto_slug = '-'.join(fields_values)

        slug = slugify(unidecode(proto_slug))
    else:
        slug = new_slug

    qs_exists = instance.__class__.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = f'{slug}-{get_random_string(10)}'
        return unique_slugify(instance, new_slug=new_slug)
    
    return slug
