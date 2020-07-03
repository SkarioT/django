from .models import Profile

def create_profile(sender,instance, **kwargs):
    obj, created = Profile.objects.get_or_create(
        user=instance,
        defaults={},
    )
    if created:
        #при создании накидываю сразу группу 2= Customers
        instance.groups.add(2)
        print("Профиль создан")
    else:
        print("Создние профиля не происхотило.")
