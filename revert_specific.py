import re

def get_block(content, var_name):
    pattern = re.compile(rf"(static const {var_name} = ''')(.*?)(''';)", re.DOTALL)
    match = pattern.search(content)
    if match:
        return match.group(0)
    return None

vars_to_revert = [
    "_istanbulTR", "_istanbulEN",
    "_hiddenGemsTR", "_hiddenGemsEN",
    "_gastronomyTR", "_gastronomyEN",
    "_romanticTR", "_romanticEN"
]

with open("old_city_blog_content.dart", "r") as f:
    old_content = f.read()

with open("lib/services/city_blog_content.dart", "r") as f:
    current_content = f.read()

for var_name in vars_to_revert:
    old_block = get_block(old_content, var_name)
    if old_block:
        pattern = re.compile(rf"(static const {var_name} = ''')(.*?)(''';)", re.DOTALL)
        curr_match = pattern.search(current_content)
        if curr_match:
            current_content = current_content.replace(curr_match.group(0), old_block)
            print(f"Reverted {var_name}")

with open("lib/services/city_blog_content.dart", "w") as f:
    f.write(current_content)

print("Done.")
