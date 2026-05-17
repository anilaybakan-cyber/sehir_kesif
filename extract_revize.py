import sys

def extract_revize_list(file_path):
    with open(file_path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    
    # Header is: City, Revize, Place Name, Description (TR), Description (EN), Tips (TR), Tips (EN)
    # Total lines: 1950. 1950/7 = 278.5 (Wait, header might be included)
    
    # Let's find "Revize" and the next line "x"
    revize_needed = []
    for i in range(len(lines)):
        if lines[i] == 'x':
            # This is the Revize column
            # Structure is: City (i-1), Revize (i), Place Name (i+1), Desc TR (i+2)...
            city = lines[i-1]
            name = lines[i+1]
            revize_needed.append((city, name))
            
    return revize_needed

revize_list = extract_revize_list('revize_strings.txt')
for city, name in revize_list:
    print(f"{city}|{name}")
