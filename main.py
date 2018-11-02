import argparse

def contract_func():
    str_in = seq_parsing()
    count = 1
    last_num_seq = False
    curr_num = str_in[0]
    for i in range(1, len(str_in)):
        if str_in[i-1] == str_in[i]:
            count+=1
        else:
            last_num_seq = True
        if last_num_seq or i == len(str_in)-1:
            print(curr_num+str(count), end='', flush=True)
            curr_num = str_in[i]
            count = 1
            last_num_seq = False


def seq_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="str_in")
    args = parser.parse_args()
    return args.str_in


if __name__ == "__main__":
    contract_func()

