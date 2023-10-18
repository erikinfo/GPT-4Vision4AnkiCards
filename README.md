# GPT-4Vision4AnkiCards


**Installation Requirements**

    Install Anki: Follow the official installation guide to get Anki on your machine.
    Install AnkiConnect: You can find the installation instructions on the AnkiConnect GitHub repository.

**Usage**
1. Generate Images for ChatGPT

Use the extract_convert_save function in the make_pictures_for_chatgpt.py to create compact pictures. Provide it with the PDF file of your choice.

2. Interact with ChatGPT

Note: Ensure you have ChatGPT Plus to utilize this feature.

After generating the images, manually provide them to ChatGPT with the appropriate prompts (you can see an example in the prompt.txt). ChatGPT will then generate a JSON with the desired format.
3. Create Anki Cards

Pass the generated JSON into make_cards.py to transform them into Anki cards.
