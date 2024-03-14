# django_template


## install

```bash
# in your virtual environment
pip install -U pip pip-tools

make deps
```

## run

```bash
# up database
docker-compose up -d

# run migrations
cd src && ./manage.py migrate

# run server
make start

```

## extra

See `Makefile` for more commands, or how to run any command if you don't have `make` installed.
