import sys
import os


def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as fp:
        cnt = 0
        for line in fp:


            print("line {} contents {}".format(cnt, line))
            record_word_cnt(line.strip().split(' '), bag_of_words)
            cnt += 1
    sorted_words = order_bag_of_words(bag_of_words, desc=True)
    print("Most frequent 10 words {}".format(sorted_words[:10]))


if __name__ == '__main__':
    main()