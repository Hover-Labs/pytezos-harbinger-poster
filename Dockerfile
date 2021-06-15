FROM python

RUN apt-get update && apt-get install -y libsodium-dev libsecp256k1-dev libgmp-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
