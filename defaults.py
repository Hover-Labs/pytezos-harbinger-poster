import os

# Feel free to override this to hard code a key if you want
POSTER_KEY = os.environ.get('POSTER_KEY', None)

ORACLE_DATA_SOURCE = "https://oracle-data.kolibri.finance/data.json"

# Sandboxnet
# NODE_URL = 'http://host.docker.internal:8732'
# ORACLE_CONTRACT = 'KT1C481Xumc43dwJ6rSQE3VpPtSWdnnqD7qv'
# NORMALIZER_CONTRACT = 'KT1Ug4XjN9FWMbbdi8myx358Uh8DUNyTqoiC'
#
# Florence Testnet
# NODE_URL = 'https://rpctest.tzbeta.net'
# ORACLE_CONTRACT = 'KT1D2F12dbneCAJUXDxzYgoZu8gb5Mjf618m'
# NORMALIZER_CONTRACT = 'KT1RCNpUEDjZAYhabjzgz1ZfxQijCDVMEaTZ'

# Mainnet
NODE_URL = 'https://rpc.tzbeta.net'
ORACLE_CONTRACT = 'KT1Jr5t9UvGiqkvvsuUbPJHaYx24NzdUwNW9'
NORMALIZER_CONTRACT = 'KT1AdbYiPYb5hDuEuVrfxmFehtnBCXv4Np7r'
