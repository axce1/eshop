build:
	docker-compose build

daemon:
	docker-compose up -d

up:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti eshop_nginx bash

shell-web:
	docker exec -ti eshop_django bash

shell-db:
	docker exec -ti eshop_mysql bash

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec eshop_django /bin/sh -c "python manage.py collectstatic --noinput"

test:
	docker-compose run --rm web /bin/sh -c "coverage run --source='.' manage.py test && coverage report"
