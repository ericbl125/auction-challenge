# python3 vesion 3.8.10

# Auction challenge for Freestar
import json


def getBidAdjustment(bidName):
	"""
	Description: Searches the config file for the bidder with a matching name returns the adjustment
	:param siteName: string value of the name of the bidder
	:return: adjustment value of bidder
	"""	
	for bidder in config["bidders"]:
		if bidder["name"] == bidName:
			return bidder["adjustment"]
		else:
			return None


def getSiteIndex(siteName):
	"""
	Description: Searches the config file for the site with a matching name returns the index
	:param siteName: string value of the name of the site
	:return: index value of the site in the config file
	"""
	for index, configSite in enumerate(config["sites"]):
		# print(configSite["name"])
		if configSite["name"] == siteName:
			return index
	return -1
	

with open('config.json') as file:
	config = json.load(file)


with open('input.json') as file:
	inputData = json.load(file)

# create key:value for units for every site
# {sidebar:0, banner:1}

highestBids = []
for index, auction in enumerate(inputData):
	# create unit dictionary for faster ordering of winning bids
	# unitDict = {unit: idx for idx, unit in enumerate(auction["units"])}

	maxBids = dict.fromkeys(auction["units"])
	winningBids = {}
	
	# cache the config site info
	siteIndex = getSiteIndex(auction["site"])

	# validate the site
	if siteIndex > -1:
		# add list entry to highestBids for auctions
		# highestBids.append([None]*len(unitDict))
		
		for bid in auction["bids"]:
			# check if bid: unit is in auction: units list
			
			# when do I check the bidder?
			if bid["unit"] in maxBids.keys():
				bidAdjust = getBidAdjustment(bid["bidder"])
				if bidAdjust is not None:
					adjustedBid = (bid["bid"] * bidAdjust) + bid["bid"]

					if adjustedBid > config["sites"][siteIndex]["floor"]:
						# always get the value of the unit index from dictioanry
						if maxBids[bid["unit"]] is None:
							maxBids[bid["unit"]] = adjustedBid
							winningBids.update({bid["unit"]: bid})
						if adjustedBid > maxBids[bid["unit"]]:
							maxBids[bid["unit"]] = adjustedBid
							winningBids[bid["unit"]] = bid
				print(winningBids)
				print(maxBids)			
	print(" ")


