#!/usr/bin/env python3

import requests
from pytezos import pytezos, micheline_to_michelson, unforge_micheline

def fetch_oracle_data(oracle_data_source):
	return requests.get(oracle_data_source).json()

def parse_oracle_data(oracle_messages, oracle_signatures):
	oracle_bundles = zip(oracle_messages, oracle_signatures)

	data = {}
	for message, signature in oracle_bundles:
		parsed_message = micheline_to_michelson(
			unforge_micheline(
				bytes.fromhex(message)[1:]
			)
		)
		normalized_message = ' '.join(parsed_message.split())

		payload = normalized_message.split(' ')
		asset_name = payload[1].replace('"', '')
		start = int(payload[3])
		end = int(payload[5])
		open = int(payload[7])
		high = int(payload[9])
		low = int(payload[11])
		close = int(payload[13])
		volume = int(payload[14].replace(')', ''))

		data[asset_name] = [
			signature, start, end, open, high, low, close, volume
		]
	return data

def create_update_operation(config):
	client = pytezos.using(shell=config.NODE_URL, key=config.POSTER_KEY)

	oracle = client.contract(config.ORACLE_CONTRACT)
	normalizer = client.contract(config.NORMALIZER_CONTRACT)

	oracle_data = fetch_oracle_data(config.ORACLE_DATA_SOURCE)

	oracle_timestamp = oracle_data['timestamp']
	oracle_messages = oracle_data['messages']
	oracle_signatures = oracle_data['signatures']
	prices = dict(sorted(oracle_data['prices'].items(), key=lambda item: -1 * float(item[1]))) # Sort price results

	parsed_oracle_data = parse_oracle_data(oracle_messages, oracle_signatures)

	print("Examining current normalizer data to filter out un-necessary updates...")
	filtered_data = {}
	for pair, price_data in parsed_oracle_data.items():
		try:
			live_data = normalizer.storage['assetMap'][pair]()
			if live_data['lastUpdateTime'] < price_data[1]:
				filtered_data[pair] = price_data
			else:
				del prices[pair.split('-')[0]]
		except KeyError:
			print("Pair {} not found in normalizer!".format(pair))
			del prices[pair.split('-')[0]]
			pass

	bulk_operation = client.bulk(oracle.update(filtered_data),
								 oracle.push(config.NORMALIZER_CONTRACT + "%update"))

	return bulk_operation, prices, oracle_timestamp
