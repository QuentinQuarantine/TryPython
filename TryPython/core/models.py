from django.db import models


class Step(models.Model):
    title = models.TextField()
    content = models.TextField()

    def to_dict(self):
        return {
            'content': self.content,
            'title': self.title
        }
