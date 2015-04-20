from collections import Counter
import math
import decimal

spam_train_result = ''
non_train_result = ''
proportion = 0.0
for i in range(1,251,1):
	spam_train = open('/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment04/Data/SpamTrain250/spamtrain'+str(i)+'.txt').read()
	non_spam_train = open('/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment04/Data/NonSpamTrain250/NonSpamTrain'+str(i)+'.txt').read()
	spam_train_result = spam_train_result + spam_train
	non_train_result = non_train_result + non_spam_train
spam_train_count = Counter(spam_train_result.split())
non_train_count = Counter(non_train_result.split())
print non_train_count
spam_train_total = len(spam_train_result.split())
non_train_total = len(non_train_result.split())
print non_train_total
print spam_train_total
##print total_num_words
'''
for i in non_spam_test:
	print i,"%1.5f"%(non_spam_test[i]/float(total_num_words))
'''
