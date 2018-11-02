import argparse


def compression_func(str_in):
    repeat_count = 1
    last_num_seq = False
    curr_num = str_in[0]
    for i in range(1, len(str_in)):
        if str_in[i - 1] == str_in[i]:
            repeat_count += 1
        else:
            last_num_seq = True
        if last_num_seq or i == len(str_in) - 1 or repeat_count == 9:
            print('%d%s' % (repeat_count, curr_num), end='', flush=True)
            curr_num = str_in[i]
            repeat_count = 1
            last_num_seq = False


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="str_in")
    args = parser.parse_args()
    return args.str_in


def main():
    arguments = get_arguments()
    compression_func(arguments.str_in)


if __name__ == "__main__":
    main()


def decompression(my_str):
    if len(my_str) % 2 != 0:
        raise ValueError('cannot decompress, string is not divideable by 2')
    for i in range(0, len(my_str) - 2, 2):
        current_char = my_str[i]
        times = my_str[i + 1]
        print(current_char * times, end='', flush=True)





