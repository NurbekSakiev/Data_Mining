from collections import Counter
import math
import decimal

spam_train_result = ''
non_train_result = ''
proportion = 0.0
for i in range(240,251,1):
	spam_train = open('/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment04/Data/SpamTrain250/spamtrain'+str(i)+'.txt').read()
	non_spam_train = open('/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment04/Data/NonSpamTrain250/NonSpamTrain'+str(i)+'.txt').read()
	spam_train_result = spam_train_result + spam_train
	non_train_result = non_train_result + non_spam_train

spam_train_count = Counter(spam_train_result.split())
non_train_count = Counter(non_train_result.split())

spam_train_total = len(spam_train_result.split())
non_train_total = len(non_train_result.split())


spam_prob_dict = {}
non_prob_dict = {}

non_prob_total = 1.0
spam_prob_total = 1.0

## Calculating probabilites of top 100 words
for k, v in spam_train_count.most_common(100):
	spam_prob_dict[k] = (spam_train_count[k]/float(spam_train_total))
	spam_prob_total = spam_prob_total * spam_prob_dict[k]
	

for k,v in non_train_count.most_common(100):
	non_prob_dict[k] = (non_train_count[k]/float(non_train_total))
	non_prob_total = non_prob_total * non_prob_dict[k]


## Calculating all words probabilities and mulitplying all of them
'''
for i in spam_train_count:
	spam_prob_dict[i] = (spam_train_count[i]/float(spam_train_total))
	##print spam_prob_dict[i]
	spam_prob_total = spam_prob_total * spam_prob_dict[i]

for j in non_train_count:
	non_prob_dict[j] = (non_train_count[j]/float(non_train_total))
	##print non_prob_dict[j]
	non_prob_total = non_prob_total * non_prob_dict[j]

'''




	##print i,"%1.10f"%(spam_train_count[i]/float(spam_train_total))
