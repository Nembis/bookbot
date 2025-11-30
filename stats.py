def get_num_words(content):
    lines = content.split("\n")
    count = 0
    for line in lines:
        words = line.split(" ")
        for word in words:
            if word != "":
                count += 1
    return count

def count_character_frequency(content):
    lines = content.split(" ")
    characters = {}
    for line in lines:
        for char in line:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    return characters

def sort_char_dict(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"char": key, "num": char_dict[key]})

    def sort_on(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list