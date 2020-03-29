from django.db import models
from django.utils.translation import gettext as _
from user.models import User
from school.models import ClassRoom
# Create your models here.


class Lesson(models.Model):
    """课程
       :param id: 编号
       :param name: 课程名称
       :param description: 描述
       :param status: 课程状态
       :param updated: 更新时间
       :param created 创建时间"""

    STATUS_ACTIVE = "active"
    STATUS_APPENDING = "appending"
    STATUS_DECLINED = "declined"
    STATUS_DELETED = "deleted"

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _("Active")),
        (STATUS_APPENDING, _("Appending")),
        (STATUS_DECLINED, _("Declined")),
        (STATUS_DELETED, _("Deleted"))
    )

    class Meta:
        db_table = "school_lessons"

    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32)
    description = models.TextField(null=True)
    status = models.CharField(max_length=9,
                              default="active",
                              choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class TimeTable(models.Model):
    """课程表
       :param id: 编号
       :param lesson: 课程
       :param teacher: 教师
       :param students: 学生
       :param classroom: 教室
       :param start: 上课开始时间
       :param end: 下课时间
       :param status: 此堂课状态
       :param updated: 更新时间
       :param created: 创建时间"""

    STATUS_ACTIVE = "active"
    STATUS_APPENDING = "appending"
    STATUS_DECLINED = "declined"
    STATUS_DELETED = "deleted"

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _("Active")),
        (STATUS_APPENDING, _("Appending")),
        (STATUS_DECLINED, _("Declined")),
        (STATUS_DELETED, _("Deleted"))
    )

    class Meta:
        db_table = "school_timetables"

    id = models.CharField(primary_key=True, max_length=32)
    lesson = models.ForeignKey(to=Lesson,
                               on_delete=models.PROTECT,
                               related_name="started")

    teacher = models.ForeignKey(to=User,
                                limit_choices_to={
                                    'status': User.STATUS_ACTIVE,
                                    'type': User.TYPE_TEACHER
                                },
                                on_delete=models.PROTECT)
    students = models.ManyToManyField(to=User,
                                      related_name="lessons",
                                      limit_choices_to={
                                          'status': User.STATUS_ACTIVE,
                                          'type': User.TYPE_STUDENT
                                      })
    classroom = models.ForeignKey(to=ClassRoom,
                                  related_name="lessons",
                                  limit_choices_to={
                                      'status': ClassRoom.STATUS_ACTIVE,
                                  },
                                  on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=9,
                              default="appending",
                              choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
