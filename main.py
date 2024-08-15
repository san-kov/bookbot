def main() -> None:
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

        words = num_words(file_contents) 
        d = get_chars_dict(words)
        print_chars_count(d)


def num_words(str) -> int:
    return str.split()

def get_chars_dict(words): 
    d = {}
    for w in words: 
        for c in list(w):
            if c.isalpha():
                c_lower = c.lower()
                if c_lower in d: d[c_lower] += 1
                else: d[c_lower] = 1 
    return d

def print_chars_count(d):
    for c in d:
        print(f'The {c} character was found {d[c]} times')

main()