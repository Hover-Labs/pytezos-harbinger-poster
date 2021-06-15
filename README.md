# Pytezos Harbiner Poster

This is just a simple poster that will take the data source from the harbinger.live site and use it to post to the harbiner oracle/normalizer using PyTezos.

# Installation & Usage

Installation is pretty basic, just run `pip install -r requirements.txt`, and then you can use `python run.py`. 

Things default to production and you can specify your poster private key with `--poster-key` or via the `POSTER_KEY` environment variable.

If you want to run things via docker, you can just run `make build-docker` and `make run POSTER_KEY=YOUR_POSTER_KEY` or do whatever docker things you'd like!
