# Container-First Dev Scaffold

## Run app

```bash
docker compose up --build app
```

## Run test profile

```bash
docker compose --profile tests up --build --abort-on-container-exit
docker compose run --rm test-3
```

## Stop

```bash
docker compose down
```

CI workflow: `.github/workflows/compose-tests.yml`
