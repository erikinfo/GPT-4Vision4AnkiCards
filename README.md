# GPT-4Vision4AnkiCards

30.11.2023: Archived since ChatGPT now allows direct interaction with PDFs.

This tool allows to automatically create Anki Cards for any topic you like. Basic programming experience is needed to run the two functions and a ChatGPT-Plus Subscription (by Oct 18, 2023), as well as some time for inserting the Prompts with the ready-made pictures.

## Installation Requirements

1. **Anki**: Follow the [official installation guide](https://apps.ankiweb.net/) to get Anki on your machine.
2. **AnkiConnect**: Easy Installation instructions can be found on the [AnkiConnect GitHub repository](https://github.com/FooSoft/anki-connect).
3. **Python Programming Environment**

## Usage

### 1. Generate Images for ChatGPT

Use the `extract_convert_save` function in the `make_pictures_for_chatgpt.py` script. Provide it with the PDF file of your choice.

**Note**: ChatGPT Plus is required for this functionality.

### 2. Interact with ChatGPT

After generating the images, manually provide them to ChatGPT with your prompts. ChatGPT will then produce a JSON in the desired format.

### 3. Create Anki Cards

With the generated JSON, run `make_cards.py` to create the Anki cards.
