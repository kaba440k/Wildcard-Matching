import time


def main():
    s_sample = list(input())
    p_sample = list(input())
    flag = True
    counter = 0
    start_time = time.time()
    for symbol in s_sample:
        if len(p_sample) == 0:
            flag = False
            break
        if p_sample[0] == symbol or p_sample[0] == "?" or p_sample[0] == "*" and flag:
            if p_sample[0] == "*":
                if len(p_sample) == 1:
                    flag = True
                    break
                elif p_sample[1] == "?" or p_sample[1] == "*":
                    flag = True
                elif p_sample[1] != "?" and p_sample[1] != "*":
                    flag = False
                    while symbol != p_sample[1] and flag is False and counter + 2 != len(s_sample):
                        if counter + 2 > len(s_sample):
                            flag = False
                            break
                        symbol = s_sample[counter + 2]
                        s_sample.pop(counter)
                    else:
                        flag = True
            p_sample.pop(0)
            counter += 1
        else:
            flag = False
            break

    print(flag)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

