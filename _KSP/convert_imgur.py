# Converts the imgur albums to markdown
# The albums have been downloaded with:
#  gallery-dl --write-metadata --write-info-json <album>
# They are located in /assets/images/KSP/

from pathlib import Path
import json
from urllib.parse import quote
import re

root_dir = Path("../assets/images/KSP/imgur/")
    
# Iterate on the albums
for album in root_dir.iterdir():
    title = '-'.join(album.name.split('-')[1:]).strip()
    title = title.replace('|', '-')

    print(title)
    
    # Buffer to hold the text of the page
    # Start with the header
    text_buffer  =  "---\n"
    text_buffer += f"title: {title}\n"
    text_buffer += f"collection: KSP\n"

    # Get the creation date of the album
    for image in album.iterdir():
        if not image.name.endswith(".json"):
            continue
        file = json.load(open(image.resolve()))
        date = file["album"]["created_at"]
        break

    # Finish the header
    text_buffer += f"date: {date}\n"
    text_buffer += f"---\n\n"

    # Write the page itself now
    for image in sorted(album.iterdir()):
        if not image.name.endswith(".json"):
            continue

        file = json.load(open(image.resolve()))

        description = file["description"]

        image_path = f"{str(image).replace('.json', '')[2:]}"
        image_path = quote(image_path)
        text_buffer += f"\n![]({image_path})\n\n"
        text_buffer += f"{description}\n"

    # Write the page
    title = re.sub(r'[^\w_. -]', '_', title)
    page = open(f'{date.split("T")[0]}_{title}.md', "w")
    page.write(text_buffer)
    page.close()
