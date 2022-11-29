RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)

DATABASE_URL := sqlite:///database.sqlite3
MIGRATIONS_PATH := ./migrations

run:
	pw_migrate migrate --database $(DATABASE_URL) --directory ${MIGRATIONS_PATH}
	python app.py

db_revision:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} ${RUN_ARGS}

db_upgrade:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
