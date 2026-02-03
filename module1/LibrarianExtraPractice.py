with open("down_the_rabbit-hole.txt", "r", encoding="utf-8") as file:

    for line_number, line in enumerate(file,1):
        print(f"Line {line_number}: {line.strip()} ")
       