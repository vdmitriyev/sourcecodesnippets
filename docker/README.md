## About

Collection of `docker compose` files for various needs.

## List of `docker compose` files and commands

* go `go-cli-bundle`
	+ go: base
		```
		docker compose -f docker-compose-go.yml up
		```
	+ go: recreate
		```
		docker compose -f docker-compose-go.yml up -d --no-deps --build go-cli-bundle
		```
	+ go: connect to bash
		```
		docker compose -f docker-compose-go.yml exec go-cli-bundle bash
		```
	+ go: stop the docker compose
		```
		docker compose -f docker-compose-go.yml down
		```
