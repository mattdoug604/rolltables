NAME=rolltables

.PHONY: lint

lint:
	isort --line-length 100 --profile black $(NAME)
	black --line-length 100 $(NAME)
