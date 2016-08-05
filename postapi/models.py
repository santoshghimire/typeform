from django.db import models


class FormResponse(models.Model):
    """ NoticeCategory module contains the category information for notice.
    """
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        """Default Function."""
        return str(self.id)
