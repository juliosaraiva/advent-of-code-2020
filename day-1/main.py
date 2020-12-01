with open('input', 'r') as f:
    content = [j.replace("\n", "") for j in f]


def find_entries(list):
    for j in list:
        for k in list:
            if int(j) != int(k):
                sum = int(j) + int(k)
                if sum == 2020:
                    print(int(j) * int(k))


def find_entries_with_3(list):
    for j in list:
        for k in list:
            for l in list:
                if j != k and k != l and l != j:
                    sum = int(j) + int(k) + int(l)
                    if sum == 2020:
                        print(int(j) * int(k) * int(l))


find_entries_with_3(content)
