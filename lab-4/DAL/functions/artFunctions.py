import os

from assets.font import chars

def getInput():
    user_input = input('Enter the phrase: ')

    return user_input

def changeSymbol(art, symbol):
    updated_art = ""
    for char in art:
        if char != '\n' and char != ' ':
            updated_art += symbol
        else:
            updated_art += char
    return updated_art


def askToSaveArt(folderToSave, art):
    isArtToSave = input('Do you want to save your art? (y/n): ')

    if isArtToSave == 'y':
        saveArt(folderToSave, art)
    else:
        pass

def saveArt(folderToSave, art):
    file_name = input('Give a file name: ')
    formated_file_name = folderToSave + file_name + '.txt'

    with open(formated_file_name, 'w') as file:
        file.write(art)

def previewArt(art):
    print(art)


def scaleArt(ascii_art, width_factor, height_factor):
    width_factor = int(width_factor)
    height_factor = int(height_factor)

    scaled_lines = []
    for line in ascii_art.splitlines():
        scaled_line = "".join(char * width_factor for char in line)
        for _ in range(height_factor):
            scaled_lines.append(scaled_line)
    return "\n".join(scaled_lines)

def draw_char(text, symbol="*"):
    result = [""] * 6  # Assuming each character ASCII art is 6 lines high

    for char in text.upper():
        if char in chars:  # Check if character exists in our ASCII template dictionary
            for i in range(6):  # Iterate over each line of the ASCII character
                line = chars[char][i].replace("*", symbol)  # Replace default symbol with the specified one
                result[i] += line + "  "  # Add spacing between characters
        else:
            for i in range(6):  # If character is not found, add spaces
                result[i] += " " * (len(chars.get('A', [''])[0]) + 2)

    return "\n".join(result)



def align_art(ascii_art, width, alignment):
    aligned_lines = []
    for line in ascii_art.splitlines():
        if alignment == "left":
            aligned_lines.append(line.ljust(width))
        elif alignment == "center":
            aligned_lines.append(line.center(width))
        elif alignment == "right":
            aligned_lines.append(line.rjust(width))
        else:
            aligned_lines.append(line)
    return "\n".join(aligned_lines)


