from difflib import SequenceMatcher

with open("demo1.txt") as file1, open("demo2.txt") as file2:

    data_file1 = file1.read()

    data_file2 = file2.read()

matches = SequenceMatcher(None, data_file1, data_file2).ratio()

percentage = matches * 100  

print(f'The plagiarized content is {percentage:.2f}%')
