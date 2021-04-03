with open("text.txt", "r") as input_text:
    with open("edit_text.txt", "w") as output_text:
        output_text.write(input_text.read().replace('\n', ' '))
