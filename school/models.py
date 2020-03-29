from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class ClassRoom(models.Model):
    """教室
       :param id: 编号
       :param name: 教室
       :param status: 教室状态"""

    STATUS_APPENDING = "appending"
    STATUS_ACTIVE = "active"
    STATUS_DECLINED = "declined"
    STATUS_DELETED = "deleted"

    STATUS_CHOICES = (
        (STATUS_APPENDING, _("Appending")),
        (STATUS_ACTIVE, _("Active")),
        (STATUS_DECLINED, _("Declined")),
        (STATUS_DELETED, _("Deleted"))
    )

    class Meta:
        db_table = "school_classrooms"

    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(unique=True, max_length=32)

    status = models.CharField(max_length=9,
                              default=STATUS_ACTIVE,
                              choices=STATUS_CHOICES)
