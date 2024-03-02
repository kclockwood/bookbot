def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    letters = get_letter_count(text)
    letters_list = dict_to_list(letters)
    letters_list.sort(key=sort_on, reverse=True)
    report = report_on(letters_list) 
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print(" ")
    for result in report:
        print(result)
    print("--- End report ---")
    return text
    

def get_word_count(text):
    word_count = text.split()
    return len(word_count)

def get_letter_count(text):
    lower = text.lower()
    count_letters = {}
    for i in lower:
        if i.isalpha():
            if i not in count_letters:
                count_letters[i] = 1
            else: 
                count_letters[i] += 1
    return count_letters

def dict_to_list(count_letters):
    return [{"key": letter, "value": count} for letter, count in count_letters.items()] 

def sort_on(dict):
    return dict["value"] 

def report_on(letters_list):
    report_list =[]
    for items in letters_list:
        report_list.append(f"The '{items["key"]}' character was found '{items["value"]}' times")
    return report_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

