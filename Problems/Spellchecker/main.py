incorr_list = []
dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal', 'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize', 'sign', 'the', 'to', 'uncertain']

sent = input()
sent = sent.split()

for word in sent:
    if word not in dictionary:
        incorr_list.append(word)

if len(incorr_list) == 0:
    print("OK")
else:
    print("\n".join(incorr_list))
