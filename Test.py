from collections import Counter
import math


# Connects all texts and returns the final string
def get_combined_text(directory,folder_name,file_name,start_file,end_file):
	test_result = ''
	for i in range(start_file,end_file+1,1):
		test = open(directory+folder_name+'/'+file_name+str(i)+'.txt').read()
		test_result = test_result + test
	return test_result

# Returns the product of top 100 words probabilities
def top_common_words_prob(words_dict, total_num_words):
	prob_dict = {}
	prob_total = 1.0
	for k,v in words_dict.most_common(100):
		prob_dict[k] = (words_dict[k]/float(total_num_words))
		prob_total = prob_total * prob_dict[k]
	return prob_total


# Normalizing the length of spam and non-spam trainings
def normalize_data(train_spam_count, train_spam_len, train_non_count, train_non_len):
	if train_spam_len < train_non_len:
		constant = train_non_len/float(train_spam_len)
		for k in train_spam_count.keys():
			train_spam_count[k] = train_spam_count[k] * constant
		return train_spam_count
	else:
		constant = train_spam_len/float(train_non_len)
		for k in train_non_count.keys():
			train_non_count[k]= train_non_count[k] * constant
		return train_non_count

# Final part of printing if it is spam or not
def calculate_prob(words_count,train_spam_words,train_non_words):
	spam_prob = 0
	non_prob = 0
	for k in words_count.keys():
		if((k in train_non_words) and (k in train_spam_words)):
			spam_prob = spam_prob + train_spam_words[k]
			non_prob = non_prob + train_non_words[k]
			print k,train_non_words[k], train_spam_words[k]
		elif (k in train_non_words):
			spam_prob = spam_prob + 0.01
			non_prob = non_prob + train_non_words[k]
			#print spam_prob, non_prob
		elif (k in train_spam_words):
			spam_prob = spam_prob + train_spam_words[k]
			non_prob = non_prob + 0.01
			##print spam_prob, non_prob
	#print spam_prob, non_prob
	if (spam_prob<non_prob):
		print 'not spam'
	else:
		print 'spam'

dir = '/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment04/Data/'

train_non_str = get_combined_text(dir,'NonSpamTrain250','NonSpamTrain',1,250)
train_non_count_words = Counter(train_non_str.split())
train_non_text_len = len(train_non_str.split())
##train_non_common = top_common_words_prob(train_non_count_words, train_non_text_len)


train_spam_str = get_combined_text(dir,'SpamTrain250','spamtrain',1,250)
train_spam_count_words = Counter(train_spam_str.split())
train_spam_text_len = len(train_spam_str.split())
train_spam_common = top_common_words_prob(train_spam_count_words, train_spam_text_len)



if (train_non_text_len < train_spam_text_len):
	train_non_count_words = normalize_data(train_spam_count_words,train_spam_text_len,train_non_count_words, train_non_text_len)
else:
	train_spam_count_words = normalize_data(train_spam_count_words,train_spam_text_len,train_non_count_words, train_non_text_len)

print train_non_count_words.most_common(30)
print train_spam_count_words.most_common(30)

test_str = get_combined_text(dir,'NonSpamTest100','NonSpamTest',10,15)
test_count_words = Counter(test_str.split())
test_text_len = len(test_str.split())


calculate_prob(test_count_words, train_spam_count_words, train_non_count_words)

'''
print train_non_count_words.most_common(20)
print train_spam_text_len, train_non_text_len
print train_spam_text_len/float(train_non_text_len)
'''

'''
test = {}
test = test_count_words.most_common(20)
for k,v in test:
	if(k in train_non_count_words):
		print k,train_non_count_words[k]
print '---------------'
for k,v in test:
	if(k in train_spam_count_words):
		print k,train_spam_count_words[k]
'''
##print train_non_common * math.pow(10,250)
##print train_spam_common * math.pow(10,250)
##print test_total_prob * math.pow(10,240)

