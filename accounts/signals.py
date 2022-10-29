from PIL import Image
from pathlib import Path
from django.db.models.signals import post_save, pre_delete
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from  django.core.files.storage import FileSystemStorage
from django.conf import settings


from django.dispatch import receiver
from accounts.models import User,Address
#===========================================================================


#===========================================================================
@receiver(post_save, sender=User)
def create_address(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)

    else:
        try:
            instance.address.save()
        except:
            Address.objects.create(user=instance)
            

        
#===========================================================================
@receiver(post_save, sender=User)
def create_user_images(sender, instance, created, **kwargs):
    fss = FileSystemStorage(location=f"{settings.MEDIA_ROOT}/user/")
    if created and fss.exists("profile_image.png") and fss.exists("cover_image.jpg"):
        cover_image_path = Path(f"{settings.MEDIA_ROOT}/user/cover_image.jpg")
        profile_image_path = Path(f"{settings.MEDIA_ROOT}/user/profile_image.png")
        with profile_image_path.open(mode='rb') as prof:
            instance.userimage_set.create(image=ImageFile(prof, name=profile_image_path.name) , role="profile_image")
        with cover_image_path.open(mode='rb') as cov:
            instance.userimage_set.create(image=ImageFile(cov, name=cover_image_path.name) , role="cover_image")
    
    elif fss.exists("profile_image.png") and fss.exists("cover_image.jpg"):
        profile_image = instance.userimage_set.filter(role="profile_image")
        cover_image = instance.userimage_set.filter(role="profile_image")
        
        if not profile_image.exists():
            profile_image_path = Path(f"{settings.MEDIA_ROOT}/user/profile_image.png")
            with profile_image_path.open(mode='rb') as prof:
                instance.userimage_set.create(image=ImageFile(prof, name=profile_image_path.name) , role="profile_image")
        else:
            profile_image.first().save()
            
        if not cover_image.exists():
            cover_image_path = Path(f"{settings.MEDIA_ROOT}/user/cover_image.jpg")
            with cover_image_path.open(mode='rb') as cov:
                instance.userimage_set.create(image=ImageFile(cov, name=cover_image_path.name) , role="cover_image")
    
        else:
            cover_image.first().save()
    