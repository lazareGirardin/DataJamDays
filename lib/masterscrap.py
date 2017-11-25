import requests
import json
import pandas as pd

def fetch_councillor(id_, page):
	url = "http://ws-old.parlament.ch/votes/councillors/" + str(id_)
	print(url)
	params = {
		'format':'json',
		'pageNumber': page}
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
	}
	resp = requests.get(url=url, params=params, headers=headers)
	return resp
	
def fetch_factions(id_):
	url = "http://ws-old.parlament.ch/factions/" + str(id_)
	#print(url)
	params = {
		'format':'json'}
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
	}
	resp = requests.get(url=url, params=params, headers=headers)
	return resp

def masterscrap(conseil_dict , nb_pages):
	"return a beautiful df. Also Lazare coded 3 nested for loops, cheers to that."
	
	votes = []
	maxIdx = nb_pages

	for index, (k, v) in enumerate(conseil_dict.items()):
		pageIdx = 1
		receiving = True
		counselor_votes = []
		while(receiving):
			_vote = fetch_councillor(v, pageIdx)
			if (_vote.status_code != requests.codes.ok or pageIdx >= maxIdx):
				receiving = False
			else:
				counselor_votes.append(_vote)
				pageIdx+=1
		votes.append(counselor_votes)
		percent = index / len(conseil_dict)
		print("{}%".format(percent))

	df = pd.DataFrame()
	for counselor in votes:
		for vote in counselor:
			j = vote.json()
			for eachvote in j['affairVotes']:
				df.loc[eachvote['id'], j['id']] = eachvote['councillorVote']['decision']

	return(df)
