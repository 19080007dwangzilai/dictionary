data = []
count = 0
with open('reviews.txt', 'r')as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
            print(len(data))
wc = {}
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print(len(wc))
while True:
    word = input('enter the key you want to check:')
    if word == 'q':
        break
    else:
        if word in wc:
            print(word,'出现的次数', wc[word])
        else:
            print('not found')
