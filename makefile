migrations-o:
	@read -p "🔧 Введите сообщение для миграции: " MSG; \
	docker-compose -f docker-compose.yml run fastapi-app alembic revision --autogenerate -m "$$MSG"

migrate-o:
	docker-compose -f docker-compose.yml run fastapi-app alembic upgrade head

build-o:
	docker-compose -f docker-compose.yml build

up-o:
	docker-compose -f docker-compose.yml up -d

down-o:
	docker-compose -f docker-compose.yml down

migrations:
	@read -p "🔧 Введите сообщение для миграции: " MSG; \
	docker compose -f docker-compose.yml run fastapi-app alembic revision --autogenerate -m "$$MSG"

migrate:
	docker compose -f docker-compose.yml run fastapi-app alembic upgrade head

build:
	docker compose -f docker-compose.yml build

up:
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down

up-network:
	docker network create shared-net || true

down-network:
	docker network rm shared-net || true