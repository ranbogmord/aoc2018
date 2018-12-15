from day1.first import read_input, format_input

def find_multiple_loop(changes):
    acc = 0
    seen = [0]

    while seen.count(acc) < 2:
        acc += changes[0]
        changes = changes[1:] + changes[:1]
        seen.append(acc)
    return acc


if __name__ == "__main__":
    data = read_input()
    data = format_input(data)

    print(find_multiple_loop(data))

