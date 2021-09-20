TAG := harbinger-pytezos

build-docker:
	docker build -t $(TAG) .

bash:
	docker run --rm -it  -v $$(PWD):/shared --workdir /shared $(TAG) bash

testnet-poster:
	docker run -e POSTER_KEY=$(POSTER_KEY) -e ENVIRONMENT=granadanet --rm -it $(TAG) python run.py

prod-poster:
	docker run -e POSTER_KEY=$(POSTER_KEY) -e ENVIRONMENT=mainnet --rm -it $(TAG) python run.py

sandbox-poster:
    # Note, uses flextesa "Alice" key, which is public and known which is why it's baked in here.
	docker run --rm -it \
		-e POSTER_KEY=edsk3QoqBuvdamxouPhin7swCvkQNgq4jP5KZPbwWNnwdZpSpJiEbq \
		-e ENVIRONMENT=sandbox \
		$(TAG) \
		python run.py --update-interval 5 # Update every 5 mins
