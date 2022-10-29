
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import Group


from django.dispatch import receiver
from teachers.models import Teacher
#===========================================================================


#===========================================================================
@receiver(post_save, sender=Teacher)
def create_address(sender, instance, created, **kwargs):
    group, group_created = Group.objects.get_or_create(name = "teachers")
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
            


