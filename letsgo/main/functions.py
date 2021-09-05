from typing import Union
from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


def unique_slugify(model_obj: models.Model, fields: Union[list, str, set, dict]):
    """
        for example: 
        unique_slugify(self, ['first_name', 'last_name']
    """

    fields_type = type(fields)

    if fields_type == str:
        field_value = model_obj.__getattibute__(fields)
        fields = {fields: field_value}
    
    if fields_type in (list, set):
        field_value = '-'.join(fields)
        fields = {field: model_obj.__getattibute__(field) for field in fields}
            
    index = model_obj.__class__.objects.filter(**fields).count()
    slug = slugify(unidecode(field_value)) + (index or '')
    return slug
