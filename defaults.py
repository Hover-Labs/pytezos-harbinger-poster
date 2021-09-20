import os

# Feel free to override this to hard code a key if you want
POSTER_KEY = os.environ.get('POSTER_KEY', None)

ORACLE_DATA_SOURCE = "https://oracle-data.kolibri.finance/data.json"

ENVIRONMENTS = {
    'sandbox': {
        'node_url': 'https://sandbox.hover.engineering',
        'oracle_contract': 'KT1KegoDySzN1HbcZfDBtcYXWsNkpffYaYQh',
        'normalizer_contract': 'KT1LV3DjqarkgQ4PvCZCgbAKYi438WYcehTu'
    },
    'florencenet': {
        'node_url': 'https://florencenet.smartpy.io',
        'oracle_contract': 'KT1D2F12dbneCAJUXDxzYgoZu8gb5Mjf618m',
        'normalizer_contract': 'KT1RCNpUEDjZAYhabjzgz1ZfxQijCDVMEaTZ'
    },
    'granadanet': {
        'node_url': 'https://rpctest.tzbeta.net',
        'oracle_contract': 'KT1RCNpUEDjZAYhabjzgz1ZfxQijCDVMEaTZ',
        'normalizer_contract': 'KT1ATEmroDSWQ41U2rxsox5dS9E2biZ9ML52'
    },
    'mainnet': {
        'node_url': 'https://rpc.tzbeta.net',
        'oracle_contract': 'KT1Jr5t9UvGiqkvvsuUbPJHaYx24NzdUwNW9',
        'normalizer_contract': 'KT1AdbYiPYb5hDuEuVrfxmFehtnBCXv4Np7r'
    }
}

