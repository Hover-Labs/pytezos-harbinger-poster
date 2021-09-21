import argparse
import os
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from harbinger.cli import create_update_operation
import defaults
import pytezos.rpc.node

def update(config):
    bulk_operation, prices, oracle_timestamp = create_update_operation(config)

    print()
    formatted_timestamp = str(datetime.fromtimestamp(int(oracle_timestamp)))
    print("[+] Data is from {}".format(formatted_timestamp))

    print()
    # Good luck :P
    formatted_prices = '\n'.join([
        "    |- {} : $ {}".format(
            k.ljust(4, ' '),
            str("{:.2f}".format(round(float(v), 2))).rjust(8, ' ')
        )
        for k, v in prices.items()
    ])
    print("[+] Updating oracle with prices:\n{}".format(formatted_prices))

    tries = 1
    while True:
        try:
            result = bulk_operation.autofill().sign().inject()
            break
        except pytezos.rpc.node.RpcError as e:
            print("[Attempt {}] RPC error encountered while posting - {}".format(tries, e))
            print("Sleeping for a couple seconds and trying again.")
            time.sleep(5)
            bulk_operation, prices, oracle_timestamp = create_update_operation(config)
            tries += 1
            if tries > 5:
                raise e

    print("[+] Injected in {}".format(result['hash']))

if __name__ == '__main__':

    environment = os.environ.get('ENVIRONMENT', 'mainnet').lower()

    if environment not in defaults.ENVIRONMENTS:
        raise Exception(
            "The ENVIRONMENT variable is set to '{}', but needs to be one of {}".format(environment, defaults.ENVIRONMENTS.keys())
        )

    env_defaults = defaults.ENVIRONMENTS[environment]

    parser = argparse.ArgumentParser(description='Update Harbinger, now with 100% more Python!')

    parser.add_argument('--node-url', dest='NODE_URL', default=env_defaults['node_url'],
                        help='Which node to connect to')
    parser.add_argument('--poster-key', dest='POSTER_KEY', default=defaults.POSTER_KEY,
                        help='Which key to use to post. Must have a XTZ balance!')
    parser.add_argument('--oracle-contract', dest='ORACLE_CONTRACT', default=env_defaults['oracle_contract'],
                        help='The oracle contract to invoke update operations on')
    parser.add_argument('--normalizer-contract', dest='NORMALIZER_CONTRACT', default=env_defaults['normalizer_contract'],
                        help='The normalizer contract to have the oracle push updates to')
    parser.add_argument('--oracle-data-source', dest='ORACLE_DATA_SOURCE', default=defaults.ORACLE_DATA_SOURCE,
                        help='The oracle data source to retrieve, defaults to the source powering harbinger.live')
    parser.add_argument('--update-interval', dest='update_interval', default=15, type=int,
                        help='The update interval, defaults to 15 mins')

    args = parser.parse_args()

    if args.POSTER_KEY is None:
        raise Exception("The POSTER_KEY environment variable must be set to something!")

    print("Started poster at ", datetime.now())

    scheduler = BlockingScheduler()
    scheduler.add_job(update, 'interval', args=[args], minutes=args.update_interval, next_run_time=datetime.now())

    try:
        print("First update successful, starting scheduler!")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

