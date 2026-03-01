import re
import os

files = ['index.html', 'menu.html', 'reservations.html', 'events.html']
base_path = r"c:\Users\кяеи\OneDrive - Икономически университет - Варна\Desktop\stitch\lumina-app"

for filename in files:
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replace for href="#" matching nearby texts
    content = re.sub(r'href="#"([^>]*>)\s*Home', r'href="index.html"\1Home', content, flags=re.IGNORECASE)
    content = re.sub(r'href="#"([^>]*>)\s*Menu', r'href="menu.html"\1Menu', content, flags=re.IGNORECASE)
    content = re.sub(r'href="#"([^>]*>)\s*Reservations', r'href="reservations.html"\1Reservations', content, flags=re.IGNORECASE)
    content = re.sub(r'href="#"([^>]*>)\s*Events', r'href="events.html"\1Events', content, flags=re.IGNORECASE)

    # Some files use an active state class but no href, or a href='#'
    # Make sure text for "Lumina Bistro" or "Lumière" header goes home
    content = content.replace('href="#"', 'href="index.html"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Links updated successfully.")
