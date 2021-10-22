import os

# Feel free to override this to hard code a key if you want
POSTER_KEY = os.environ.get('POSTER_KEY', None)

ORACLE_DATA_SOURCE = "https://oracle-data.kolibri.finance/data.json"

ENVIRONMENTS = {
    'sandbox': {
        'node_url': 'https://sandbox.hover.engineering',
        'oracle_contract': 'KT1WibJ3Jw5mjgdqVjFBUVR5V4Vq2g7w1Uci',
        'normalizer_contract': 'KT18xT2hAWdyihbZ5Hw1bYSszGE2NwHpSxUF'
    },
    'florencenet': {
        'node_url': 'https://florencenet.smartpy.io',
        'oracle_contract': 'KT1D2F12dbneCAJUXDxzYgoZu8gb5Mjf618m',
        'normalizer_contract': 'KT1RCNpUEDjZAYhabjzgz1ZfxQijCDVMEaTZ'
    },
    'granadanet': {
        'node_url': 'https://rpctest.tzbeta.net',
        'oracle_contract': 'KT1ATEmroDSWQ41U2rxsox5dS9E2biZ9ML52',
        'normalizer_contract': 'KT1AQuWowr3WKwF69oTGcKaJrMajic3CKwR2'
    },
    'mainnet': {
        'node_url': 'https://mainnet.api.tez.ie',
        'oracle_contract': 'KT1Jr5t9UvGiqkvvsuUbPJHaYx24NzdUwNW9',
        'normalizer_contract': 'KT1AdbYiPYb5hDuEuVrfxmFehtnBCXv4Np7r'
    }
}

