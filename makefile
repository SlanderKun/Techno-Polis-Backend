migrations:
	@read -p "🔧 Введите сообщение для миграции: " MSG; \
	docker-compose -f docker-compose.yml run fastapi-app alembic revision --autogenerate -m "$$MSG"

migrate:
	docker-compose -f docker-compose.yml run fastapi-app alembic upgrade head

build:
	docker-compose -f docker-compose.yml build

up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down