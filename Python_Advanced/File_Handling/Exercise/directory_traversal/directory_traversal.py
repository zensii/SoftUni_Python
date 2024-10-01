import os

files = os.listdir('.')
print(files)
extensions = {}

for file in files:
    extension = file.split('.')[-1]
    extensions.setdefault(f"{extension}.", []).append(file)

with open('result.txt', 'w') as file:
    # double-sorting the dictionary. First the list with files alphabetically and then the dict by keys alphabetically
    for extension, files_with_extension in dict(sorted({key: sorted(value) for key, value in extensions.items()}.items(), key=lambda x: x[0])).items():
        file.write(extension + '\n')
        for full_file_name in files_with_extension:
            file.write(f"- - - {full_file_name}\n")