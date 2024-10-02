# --> PROGRAM FOR TEXT TO SPEECH <-- #
from gtts import gtts
from pypdf import PdfReader
import os

reader = PdfReader("pdf_file_name or path")
print(f"Total Pages: {len(reader.pages)}")  # --> If you want to check total number of pages
page = 0
my_text=""
while page < len(reader.pages):
    paper=reader.pages[page]
    my_text = paper.extract_text()
    print(my_text)
    page += 1

language = 'en'

speaker = gTTS(text=my_text, lang=language, slow=False) # If want slow can put 'True' <--
speaker.save("any_name.mp3")
os.system("start any_name.mp3")
