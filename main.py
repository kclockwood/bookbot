def main():
    # the below sets the variable 'book_path' variable that will replace 'path'
    # in the below function, and sets up the 'text' variable that will return the
    # final text being read by the function
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # the below sets up the variable that we can return at any time to get the 
    # word count we're looking for from the below function
    words = get_word_count(text)

    # below defines the variable we can return at any time to 
    # pull the dictionary of the letters and their count
    letters = get_letter_count(text)

    # below: calls letters list as the list of dictionaries, followed 
    # by the .sort() method by the dictionary key in reverse order. 
    # The report variable returns the sentence with the key and count value 
    # for each item in the list. The print statements build the visual report.
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
    
# the below takes the text that we returned from 
# get_book_text(book_path) and splits it with a space as a delimiter 
# and counts each item in the length of the list returned
def get_word_count(text):
    word_count = text.split()
    return len(word_count)

# below: lowercases all of the text so that we don't separate capital letters.
# For each letter in the text, if it's alphabetical, add it to the list with count 1. 
# If it's already in the list, just add 1 to the count.
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

#the dict to list function defines the key and value that the list populates
def dict_to_list(count_letters):
    return [{"key": letter, "value": count} for letter, count in count_letters.items()] 

# since the count of the letters was set as "value" in the function above, 
# we can now use the below function to sort based on "value".
def sort_on(dict):
    return dict["value"] 

# The below function takes each item in the list and formats it into the sentences 
# to return one at a time when the main function prints the report
def report_on(letters_list):
    report_list =[]
    for items in letters_list:
        report_list.append(f"The '{items["key"]}' character was found '{items["value"]}' times")
    return report_list

# the below sets up the formula to read from the path. 
# The (path) item doesn't actually exist without the main function above. 
# It's a placeholder
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

