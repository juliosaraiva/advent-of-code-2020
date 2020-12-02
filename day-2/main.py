with open('input.txt', 'r') as f:
    content = [fc.replace('\n', '') for fc in f]


def part_one(input):
    passwords_valid = 0
    for j in input:
        pattern, letter, password = j.split(' ')
        l_number, h_number = pattern.split('-')
        is_valid = password.count(letter.replace(':', ''))
        if is_valid >= int(l_number) and is_valid <= int(h_number):
            print(f'The Password {password} is valid')
            passwords_valid += 1
    print(passwords_valid)


def part_two(input):
    passwords_valid = 0
    for j in input:
        pattern, letter, password = j.split(' ')
        lower, higher = pattern.split('-')
        letter = letter.replace(':', '')
        if password[int(lower) - 1] == letter and password[int(higher) - 1] != letter:
            passwords_valid += 1
        elif password[int(lower) - 1] != letter and password[int(higher) - 1] == letter:
            passwords_valid += 1

    print(passwords_valid)

part_two(content)
