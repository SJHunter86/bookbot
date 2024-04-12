from collections import defaultdict

def my_func():
    char_dict = defaultdict(int)
    only_alpha = {}
    book = "./books/frankenstein.txt"
    with open(book) as file:
        text = file.read()
        words = text.split()
    
    for word in words:
        for char in word:
            char_dict[char.lower()] += 1

    for key in char_dict:
        if key.isalpha():
            only_alpha[key] = char_dict[key]

    sorted_dict = dict(sorted(only_alpha.items(), reverse=True, key=lambda item: item[1]))
    build_report(sorted_dict, len(words), book[2:])

def build_report(dict, num_words, path):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for key, value in dict.items():
        print(f"The {key} character was found {value} times")
    print("--- End report ---")

def main():
    my_func()

main()

