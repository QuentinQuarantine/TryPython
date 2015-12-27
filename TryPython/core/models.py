from django.db import models


class Step(models.Model):
    content = models.TextField()

    def to_dict(self):
        return {
            'content': self.content
        }
