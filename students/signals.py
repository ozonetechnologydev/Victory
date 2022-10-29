
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import Group


from django.dispatch import receiver
from students.models import Student
#===========================================================================


#===========================================================================
@receiver(post_save, sender=Student)
def create_address(sender, instance, created, **kwargs):
    group, group_created = Group.objects.get_or_create(name = "students")
    if group_created:
        group.permissions.add(
            
        )
    if created:
        instance.user.groups.add(group)

    else:
        try:
            instance.user.groups.add(group)
        except:
            instance.user.save()
            


