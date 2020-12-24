import argparse, time, requests, itertools

def main(brute, brute_wordlist, wordlist):
    global start_time
    start_time = time.time()
    if args.brute:
        for char_count in range(1, 50):
            print(f'[BRUTE] -> Character Length: {char_count}')
            gen = itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyz0123456789', int(char_count))
            for directory in gen:
                try:
                    req = requests.get(args.brute + '/' + directory)
                except:
                    pass # Directory does not exist
                else:
                    if req.status_code == 200:
                        print(f'Found Directory: {args.brute}/{directory}')
    elif args.brute_wordlist and args.wordlist:
        print('Loading word list...')
        f = open(args.wordlist, 'r')
        line = f.readline()
        wl = string.split(line)
        print(f'     ', len(wl), 'words loaded!')
        try:
            for word in wl:
                req = requests.get(args.brute_wordlist + '/' + word)
        except:
            pass # Directory does not exist
        else:
            if req.status_code == 200:
                print(f'Found Directory: {args.brute_wordlist}/{word}')
    else:
        print('Invalid argument used!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-brute', required=False, type=str, help='Pure brute force directories')
    parser.add_argument('-brute_wordlist', required=False, type=str, help='Brute force using a word list')
    parser.add_argument('-wordlist', required=False, type=str, help='Location of wordlist file')
    args = parser.parse_args()
    brute = args.brute
    brute_wordlist = args.brute_wordlist
    wordlist = args.wordlist
    main(brute, brute_wordlist, wordlist)
    print('%s seconds' % (time.time() - start_time))
