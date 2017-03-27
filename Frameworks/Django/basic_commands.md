# Django - Basic Commands

Start env: 
```sh
source venv/bin/activate.fish
```

Start server:
```sh
python manage.py runserver [opt:port]
```

Start shell:
```sh
python manage.py shell
```

Make migration:
```sh
python manage.py makemigrations
```

Run migration:
```sh
python manage.py migrate
```

Dump data into console from database, can be used to create fixtures:
```sh
python manage.py dumpdata [app[.modelName] ...]
```