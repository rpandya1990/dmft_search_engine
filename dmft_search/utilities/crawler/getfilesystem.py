import pickle


def getall():
	with open('filesystem.pickle', 'rb') as handle:
		b = pickle.load(handle)
	return b

print getall()
