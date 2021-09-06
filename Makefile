run_local:
	@python manage.py migrate && python manage.py runserver

run_docker:
	@docker-compose up