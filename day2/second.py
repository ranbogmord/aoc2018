from day2.first import read_data

def find_candidates(words):
    candidates = []
    matched_words = []
    for word in words:
        for cmp in words:
            if cmp == word:
                continue

            diff = 0
            diff_index = None

            for i, letter in enumerate(word):
                if cmp[i] != letter:
                    diff += 1
                    diff_index = i

            if diff == 1 and word not in matched_words and cmp not in matched_words:
                matched_words.append(word)
                matched_words.append(cmp)
                candidates.append((word, cmp, diff_index))

    return candidates

def compose_answer(candidates):
    words = []
    for candidate in candidates:
        word = candidate[0][:candidate[2]] + candidate[0][candidate[2]+1:]
        words.append(word)
    return words


if __name__ == "__main__":
    data = read_data()

    candidates = find_candidates(data)
    words = compose_answer(candidates)
    print(words)
