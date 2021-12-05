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


highestBids = []
for index, auction in enumerate(inputData):
	
	# cache the config site info
	siteIndex = getSiteIndex(auction["site"])
	# validate the site
	if siteIndex > -1:
		# add list entry to highestBids for auctions
		highestBids.append([{}])
		
		for bid in auction["bids"]:
			# check if bid: unit is in auction: units list
			# if bid["unit"] in (unit for unit in auction["units"]):

			# how to get the index of the auction units???
			bidIndex = auction["bids"].index(bid["unit"])
			

			for unitIndex, unit in enumerate(auction["units"]):
				bidIndex = auction["bids"].index(bbd["unit"])
				if bidIndex:
					# validate the bidder is in the config file
					# Do I cache the biddrs when getting the site name? each site gets a list of bidders? sacrifice space for potential time?
					bidAdjust = getBidAdjustment(bid["bidder"])
					# calculate bid with adjustment
					adjustedBid = bid["bid"] * bidAdjust + bid["bid"]
					if adjustedBid > config["sites"][siteIndex]["floor"]:
						if highestBids[index][bidIndex] is None:
							highestBids[index][bidIndex] = bid
						elif adjustedBid > highestBids[index][bidIndex]["bid"]:
							highestBids[index][bidIndex] = bid

		print(highestBids)
				# print(adjustedBid)


				# calculate bid
				
				#adjustment = ((if bidder["adjustment"]  for bidder in config["bidders"]) where bidder["adjustment"] == bid["bidder"])
				#bidAmount = bid["bid"] * config["bidders"][???]["name"]

				

				


			# how to store the highest bids in the right order?
			# store the winning bids in a list, if multiple bids per site store as a list
			#highestBids


# store winning bids in list called highestBids, it a list of dictionary values
# For each auction in input (with index)
	# cache site info from config

	# For each bid in auction
		# check bidder in config (next if not exist)
		# check unit in action[units] (next if not exist)

		# if bid["name"] in (bidder[name] for bidder in config[bidders])  -- matches the config bidders[name] to the bid[name]  -- make a function call?
			# return bidder[adjustment]

		# calculate the bid with the adjustment value

		# if adjustedBid > configSiteCache[floor]  (next if not)
			# if adjustedBid > highestBids[index][bid] || highestBids[index] is NULL
				# replace/add bid
