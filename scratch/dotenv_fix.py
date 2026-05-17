import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    # If os.getenv("GOOGLE_MAPS_API_KEY") is present, ensure dotenv is loaded
    if 'os.getenv("GOOGLE_MAPS_API_KEY")' in content:
        if "from dotenv import load_dotenv" not in content:
            lines = content.split('\n')
            # Find first line that isn't a shebang or docstring
            insert_pos = 0
            if lines and lines[0].startswith("#!"):
                insert_pos = 1
            
            lines.insert(insert_pos, "from dotenv import load_dotenv")
            lines.insert(insert_pos + 1, "load_dotenv()")
            content = '\n'.join(lines)
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    count = 0
    for f in py_files:
        if fix_file(f):
            count += 1
    print(f"Updated {count} files with load_dotenv().")

if __name__ == "__main__":
    main()
