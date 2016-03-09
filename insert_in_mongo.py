''' Python script to insert tweets in mongodb
'''
import pymongo
import sys
import json

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.tags
tweets = db.tweets


def main(jsonfile):
	f = open(jsonfile)

	for line in f.readlines():
		try:
			tweet_dict = json.loads(line)
			tweets.insert_one(tweet_dict)
		except 	Exception as e:
			print "Unexpected error:", type(e), e
			sys.exit()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Please provide the json file to insert')
		sys.exit()

	main(sys.argv[1])