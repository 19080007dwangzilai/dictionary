import time
import progressbar


def read_file(filename):
    data = []
    count = 0
    bar=progressbar.ProgressBar(max_value=1000000)
    with open(filename, 'r')as f:
        for line in f:
            data.append(line.strip())
            count += 1
            bar.update(count)
    return data


def dic(data):
    start_time = time.time()
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
    end_time = time.time()
    print(len(wc))
    print(end_time - start_time)

    return wc


def user_check(wc):
    while True:
        word = input('enter the key you want to check:')
        if word == 'q':
            break
        else:
            if word in wc:
                print(word, '出现的次数', wc[word])
            else:
                print('not found')


def main():
    data = read_file('reviews.txt')
    wc = dic(data)
    user_check(wc)


main()
