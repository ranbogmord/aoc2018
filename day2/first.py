def read_data():
    with open("input.txt") as f:
        return f.read().split("\n")


def count_letters(letters):
    letters = list(letters)
    found = {}
    for letter in letters:
        if letter not in found:
            found[letter] = 0
        found[letter] += 1

    return found

def count_occurances(word):
    found = count_letters(word)
    doubles = False
    tripples = False

    for letter, count in found.items():
        if count == 2:
            doubles = True
        if count == 3:
            tripples = True

    return doubles, tripples

def calculate_checksum(data):
    doubles = 0
    tripples = 0

    for word in data:
        found_doubles, found_tripples = count_occurances(word)

        if found_doubles:
            doubles += 1
        if found_tripples:
            tripples += 1

    return doubles * tripples


if __name__ == "__main__":
    data = read_data()
    print(calculate_checksum(data))
