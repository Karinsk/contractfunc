import argparse

def contract_func():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="str_in")
    args = parser.parse_args()
    str_in = args.str_in
    str_input = str(str_in)

    dict_hist = {}
    lst = [i for i in str_input]
    for i in lst:
        if i in dict_hist:
            dict_hist[i]+=1
        else:
            dict_hist[i]=1
    for key_hist in dict_hist.keys():
        print(key_hist+str(dict_hist[key_hist]), end='', flush=True)


if __name__ == "__main__":
    contract_func()

