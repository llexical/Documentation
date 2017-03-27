# Django - Shell: User Scripts

- Adding a Django superuser
```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_superuser('NAME', email='EMAIL', password='PASSWORD')
>>> user.save()
>>> user
<User: NAME>
>>> quit()
```

- Updating existing users password
```python
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(email="EMAIL")
>>> u.set_password("PASSWORD")
>>> u.save()
>>> quit()
```

- Making normal user superuser
```python
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(email="EMAIL")
>>> u.is_staff = True  # basic access rights
>>> u.is_admin = True  # admin access rights
>>> u.is_superuser = True  # superuser access rights
>>> u.save()
```