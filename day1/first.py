def read_input():
    with open("input.txt") as f:
        return f.read()

def format_input(data):
    data = data.replace("+", "")

    data = data.split("\n")
    return list(map(int, data))

def first():
    data = read_input()
    data = format_input(data)

    return sum(data)


if __name__ == "__main__":
    print(first())