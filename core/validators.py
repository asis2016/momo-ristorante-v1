from django.core.exceptions import ValidationError

def validate_blog(value):
    """
    Raise a ValidationError if the value doesn't ends with the word 'blog'.
    """
    if not value.endswith(u'blog'):
        msg = u'You must end with a word "blog".'
        raise ValidationError(msg)
    