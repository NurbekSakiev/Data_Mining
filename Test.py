from collections import Counter
import math



def get_combined_text(directory,folder_name,file_name,num_files):
	test_result = ''
	for i in range(1,num_files+1,1):
		test = open(directory+folder_name+'/'+file_name+str(i)+'.txt').read()
		test_result = test_result + test
	return test_result

def top_common_words_prob(words_dict, total_num_words):
	prob_dict = {}
	prob_total = 1.0
	for k,v in words_dict.most_common(100):
		prob_dict[k] = (words_dict[k]/float(total_num_words))
		prob_total = prob_total * prob_dict[k]
	return prob_total
	

dir = '/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment04/Data/'

train_non_str = get_combined_text(dir,'NonSpamTrain250','NonSpamTrain',5)
train_non_count_words = Counter(train_non_str.split())
train_non_text_len = len(train_non_str.split())
train_non_common = top_common_words_prob(train_non_count_words, train_non_text_len)

train_spam_str = get_combined_text(dir,'SpamTrain250','spamtrain',5)
train_spam_count_words = Counter(train_spam_str.split())
train_spam_text_len = len(train_spam_str.split())
train_spam_common = top_common_words_prob(train_spam_count_words, train_spam_text_len)

test_str = get_combined_text(dir,'NonSpamTest100','NonSpamTest',7)
test_count_words = Counter(test_str.split())
test_text_len = len(test_str.split())
test_total_prob = top_common_words_prob(test_count_words,test_text_len)

print train_non_common * math.pow(10,250)
print train_spam_common * math.pow(10,250)
##print test_total_prob * math.pow(10,240)

