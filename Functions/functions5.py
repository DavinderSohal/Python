

def repeat(text, copies, new_lines = False):  
    new_text = ""
    for i in range(copies):  
        new_text += text 
        if new_lines: 
            new_text += "\n"  
    return new_text

print(repeat("hello World ", 2))   #Without the optional argument
print(repeat("hello", 3, True))

