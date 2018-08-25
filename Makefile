IMAGE = django-test-manager:latest
CONTAINER = django-test-manager
MANAGECMD = docker exec -it $(CONTAINER)
APP_LOCATION = $(PWD)
DJANGO_MANAGER_FOLDER = /deploy/testmanager
DJANGO_MANAGER = "$(DJANGO_MANAGER_FOLDER)/manage.py"

all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: delete-container ## Build the container
	@docker build --tag $(IMAGE) .
	@docker run -dit --name $(CONTAINER) -v $(APP_LOCATION):/deploy -p 8000:8000 -w $(DJANGO_MANAGER_FOLDER) $(IMAGE) /bin/bash

test: ## Run tests
	@$(MANAGECMD) $(DJANGO_MANAGER) test

restart: ## Restart the container
	@docker restart $(CONTAINER)

cmd: ## Access bash
	@$(MANAGECMD) /bin/bash

up: ## Start django server
	@docker start $(CONTAINER)
	@$(MANAGECMD) /bin/bash -c "$(DJANGO_MANAGER) migrate && $(DJANGO_MANAGER) runserver 0.0.0.0:8000"

down: ## Stop container
	@docker stop $(CONTAINER)

delete-container:
	@docker stop $(CONTAINER) || true && docker rm $(CONTAINER) || true

remove: delete-container ## Delete containers and images
	@docker rmi $(IMAGE)

.DEFAULT_GOAL := help
