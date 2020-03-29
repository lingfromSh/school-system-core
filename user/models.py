from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class User(models.Model):
    """用户模型
       :param id: id
       :param school_id: 学号/工号
       :param sex: 性别
       :param type: 身份
       :param avatar: 头像
       :param name: 昵称
       :param real_name: 姓名
       :param password: 密码
       :param note: 个性签名
       :param status: 账号状态
       :param updated: 更新时间
       :param created: 创建时间
       :param last_login: 上次登录"""

    SEX_MALE = "male"
    SEX_FEMALE = "female"

    SEX_CHOICES = (
        (SEX_MALE, _("Male")),
        (SEX_FEMALE, _("Female"))
    )

    TYPE_ADMIN = "admin"
    TYPE_STUDENT = "student"
    TYPE_TEACHER = "teacher"

    TYPE_CHOICES = (
        (TYPE_ADMIN, _("Administrator")),
        (TYPE_STUDENT, _("Student")),
        (TYPE_TEACHER, _("Teacher"))
    )

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
        db_table = "school_users"

    id = models.CharField(primary_key=True, max_length=32)
    school_id = models.CharField(max_length=32, unique=True)
    sex = models.CharField(max_length=6,
                           default=SEX_MALE,
                           choices=SEX_CHOICES)
    type = models.CharField(max_length=7,
                            default=TYPE_STUDENT,
                            choices=TYPE_CHOICES)
    avatar = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=32, null=True)
    real_name = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=255, null=False)
    note = models.CharField(max_length=140, null=True)
    status = models.CharField(max_length=9,
                              default=STATUS_ACTIVE,
                              choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    @property
    def registerd_time(self):
        return self.created
