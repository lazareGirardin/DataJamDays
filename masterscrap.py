def masterscrap(conseil_dic , nb_pages):
	"return a beautiful df. Also Lazare coded 3 nested for loops, cheers to that."
	
	votes = []
	maxIdx = nb_pages

	for index, (k, v) in enumerate(conseil_dict.items()):
		pageIdx = 1
		receiving = True
		counselor_votes = []
		while(receiving):
			_vote = fetch_councillor(v, pageIdx)
			print (pageIdx)
			if (_vote.status_code != requests.codes.ok or pageIdx >= maxIdx):
				receiving = False
			else:
				counselor_votes.append(_vote)
				pageIdx+=1
		votes.append(counselor_votes)
		print(votes)


	df = pd.DataFrame()
	for counselor in votes:
		for vote in counselor:
			j = vote.json()
			for eachvote in j['affairVotes']:
				df.loc[eachvote['id'], j['id']] = eachvote['councillorVote']['decision']

	return(df)
