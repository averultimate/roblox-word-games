'''

	Finalise text files in every directory to contain the
	correct amount of letters in each word
	
	@averultimate

'''

import os
from better_profanity import profanity

current_directory = os.getcwd()

folders = []
word_files = []

for root, directories, files in os.walk(current_directory):
		
	for file_name in files:
		
		if file_name == os.path.basename(__file__):
			continue
		
		file_path = os.path.join(root, file_name)
		parent = os.path.basename(os.path.dirname(file_path))
		
		word_files.append(f"{parent}\\{file_name}")
		
for file_name in word_files:
	
	parts = file_name.split("\\")
	print(f"{parts[0]} | {parts[1]}")
	
	try:
		char_limit = int(parts[0][0])
	except ValueError:
		char_limit = 30
		
	unique_lines = set()
	
	with open(file_name, "r") as file:
		
		content = file.read().split("\n")
		words = [line.strip().lower() for line in content if len(line.strip()) == char_limit or char_limit == 30]
		
	for word in words:
		unique_lines.add(word)
		
	with open(file_name, "w") as file:
		
		for line in sorted(unique_lines):
			file.write(line + "\n")
		
print("\n\nFiltering for use in Roblox...")
		
for file_name in word_files:
	
	parts = file_name.split("\\")
	print(f"{parts[0]} | {parts[1]}")
	
	with open(file_name, "r") as file:
		
		content = file.read().split("\n")
		words = [line.strip() for line in content if not profanity.contains_profanity(line.strip())]
		
	with open(file_name, "w") as file:
		
		for line in sorted(words):
			file.write(line + "\n")
