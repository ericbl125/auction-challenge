#!/usr/bin/python

# Auction challenge for Freestar
import json
import sys
import os


def getBidAdjustment(bidName, config):
	"""
	Description: Searches the config file for the bidder with a matching name returns the adjustment
	:param siteName: string value of the name of the bidder
	:param config: dictionary containing the configuration values
	:return: adjustment value of bidder
	"""	
	for bidder in config["bidders"]:
		if bidder["name"] == bidName:
			return bidder["adjustment"]
	return None


def getSiteIndex(siteName, config):
	"""
	Description: Searches the config file for the site with a matching name returns the index
	:param siteName: string value of the name of the site
	:param config: dictionary containing the configuration values
	:return: index value of the site in the config file
	"""
	for index, configSite in enumerate(config["sites"]):
		# print(configSite["name"])
		if configSite["name"] == siteName:
			return index
	return -1
	

def main(argv):

	with open("config.json") as file:
		config = json.load(file)


	with open(argv[0]) as file:
		inputData = json.load(file)

	# create key:value for units for every site
	highestBids = []
	for auction in inputData:

		# store and validate the site
		siteIndex = getSiteIndex(auction["site"], config)

		if siteIndex > -1:
			# dictionaries to store maxBids and the current winning bidder information
			maxBids = dict.fromkeys(auction["units"])
			winningBids = {}
			
			for bid in auction["bids"]:
				# validate the bidder in the to config list of approved bidders
				if bid["bidder"] in config["sites"][siteIndex]["bidders"]:
					if bid["unit"] in maxBids.keys():

						bidAdjust = getBidAdjustment(bid["bidder"], config)
						if bidAdjust is not None:
							adjustedBid = (bid["bid"] * bidAdjust) + bid["bid"]

							if adjustedBid > config["sites"][siteIndex]["floor"]:
								# always get the value of the unit index from dictioanry
								if maxBids[bid["unit"]] is None:
									maxBids[bid["unit"]] = adjustedBid
									winningBids.update({bid["unit"]: bid})
								if adjustedBid > maxBids[bid["unit"]]:
									maxBids[bid["unit"]] = adjustedBid
			highestBids.append(list(winningBids.values()))
	# make it JSON
	output = json.dumps(highestBids)
	print(output)

if __name__ == '__main__':
	# How to read the input files.
	print(sys.argv)
	main(sys.argv)
