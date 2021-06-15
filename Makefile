TAG := harbinger-pytezos

build-docker:
	docker build -t $(TAG) .

bash:
	docker run --rm -it  -v $$(PWD):/shared --workdir /shared $(TAG) bash

run:
	docker run -e POSTER_KEY=$(POSTER_KEY) --rm -it $(TAG) python run.py
