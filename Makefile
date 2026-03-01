.PHONY: container-build container-up container-down container-test-profile

container-build:
	docker compose build

container-up:
	docker compose up --build app

container-down:
	docker compose down

container-test-profile:
	docker compose --profile tests up --build --abort-on-container-exit
