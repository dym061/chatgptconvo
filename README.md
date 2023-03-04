# ChatGPT Conversation

This project connects to the ChatGPT model and allows you to have a conversation with it. It uses a defined API key from a file and saves message conversations in a pickle file. You can quit the chat by using the `exit()` command, and the conversation will be loaded from the pickle file the next time you run the script.

## Features

1. Connects to ChatGPT model
2. Uses defined API KEY from file
3. Saves message conversations in pickle file
4. Use exit() to quit chat
5. Loads message conversations in next run from pickle file

## Usage

To use this project, you will need to have an API key for the ChatGPT model. You can obtain one by following the instructions on the OpenAI website.

Once you have your API key, create a file called `api_key.txt` in the root directory of this project and paste your API key into it.

To start a conversation with ChatGPT, simply run the `main.py` script:

You can type your message into the console and ChatGPT will respond with its own message. To quit the chat, simply type `exit()`.

When starting anew if it has previous conversations, it will show all of them before your first new prompt.

## Important Note

Please keep in mind that the longer conversations go, the more tokens will be used up and it might reach its token limit. This script is meant for demonstration purposes only to illustrate accessing the capabilities of ChatGPT with Python.

## License

This project is licensed under the MIT License - see the LICENSE file for details.