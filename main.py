import time


def main():
    user_input = list(input())
    pattern = list(input())
    flag = True
    counter = 0
    start_time = time.time()
    for symbol in user_input:
        if len(pattern) == 0 or pattern > user_input:
            flag = False
            break
        if pattern[0] == symbol or pattern[0] == "?" or pattern[0] == "*" and flag:
            if pattern[0] == "*":
                if len(pattern) == 1:
                    flag = True
                    break
                elif pattern[1] == "?" or pattern[1] == "*":
                    flag = True
                elif pattern[1] != "?" and pattern[1] != "*":
                    flag = False
                    while symbol != pattern[1] and flag is False and counter + 2 != len(user_input):
                        if counter + 2 > len(user_input):
                            flag = False
                            break
                        symbol = user_input[counter + 2]
                        user_input.pop(counter)
                    else:
                        flag = True
            pattern.pop(0)
            counter += 1
        else:
            flag = False
            break

    print(flag)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

