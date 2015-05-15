critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

def metric_euclidian(user,other,prefs):
	distance = sqrt(sum([pow(prefs[user][prefUser] - prefs[other][prefUser],2) for prefUser in prefs[user] if prefUser in prefs[other]]))
	return 1/(1+distance) if distance != 0 else 0

def topMatches(prefs,user,limit = 5,metric = metric_euclidian):
	matches = [(metric(user,userTmp,prefs),userTmp) for userTmp in prefs if userTmp != user]
	matches.sort(reverse=True)
	return matches[0:limit]

def recommendEasyWay(prefs,user):
	similar_users = topMatches(prefs,user)
	items = []
	for similar_score, name in similar_users:
		items.extend([item for item in prefs[name] if item not in prefs[user] and item not in items])
	return items

def getRecommendations(prefs,user):
	similar_users = topMatches(prefs,user,limit=3)
	items_dissimilar = []
	for _,name in similar_users:
		for item in prefs[name]:
			if item not in prefs[user] and item not in items_dissimilar:
				items_dissimilar.append(item)

	recommended_item = []
	for item in items_dissimilar:
		print item
		similar_sum = 0
		total = 0
		for similar,name in similar_users:
			if item in prefs[name]:
				similar_sum += similar
				total += prefs[name][item] * similar
		recommended_item.append((total/(1+similar_sum),item))
	recommended_item.sort(reverse=True)
	return recommended_item   