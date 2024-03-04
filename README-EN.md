# Minecraft Plugin Configuration File ChatGPT Translation Tool 🌐

Readme Language: [English](./README-EN.md) | [简体中文](./README.md)

## What is this? 🤔

This tool helps you translate Minecraft Java server plugin configuration yml files into different languages. It is based on OpenAI's ChatGPT 3.5 model and comes with built-in prompts in both Chinese and English, ready to use right out of the box with an accuracy rate of up to 99%. Additionally, it supports splitting and merging large files, as well as batch processing files, to improve your work efficiency.

## Features 🚀

- **High-Accuracy Translation**: Powered by OpenAI's ChatGPT 3.5 model, achieving an accuracy rate of 99%.
- **Multilingual Support**: Comes with built-in Chinese and English prompts, supporting translations into more languages.
- **Large File Handling**: Supports the splitting and merging of large files.
- **Batch File Processing**: Processes multiple configuration files at once.
- **User-Friendly**: Simple and easy to use, ready to go.

## How to Use 📖

1. **Preparation**:
   
   - Ensure your system has Python 3.6 or higher installed.
   - Install necessary Python libraries: `pip install -r requirements.txt`.
2. **Set Up OpenAI API Key**:
   
   - Visit [OpenAI API](https://openai.com/api/) to obtain your API key.
   - Configure your API key in the script, or enter your API key when running the script.
3. **Run the Script**:
   
   - `python3 main.py`
   - Place one or more yml configuration files into the specified input folder `Original_Files`.
   - Run the script and check the output folder `ChatGPT_Translater_Output`.
4. **Check Translation Results**:
   
   - After translation, check the files in the output folder.
   - Confirm that the translation results meet expectations.
5. **Switch Languages (Optional)**
   
   - The default output language is: `English -> Chinese`
   
   You can edit in `main.py` to switch between the original and target languages:
   
   ```python
   # Use Chinese prompts
   prompt = ChatGPT_Prompts.prompts["zh"]
   
   # Use English prompts
   _prompt = ChatGPT_Prompts.prompts["en"]
   ```
## Notes ⚠️

* Translation results may require manual review to ensure accuracy of terminology and context.
* Processing large files may take a long time, depending on file size and system performance.
* Modify`main.py` to limit the number of tokens used, with a default maximum token count of`10240`.

## Contact Me 📧

If you encounter any issues or have suggestions while using this tool, feel free to contact us via:

* **Email**:[evil0ctal1985@gmail.com]()
* **GitHub Issues**:[https://github.com/Evil0ctal/ChatGPT-Minecraft-Plugin-Translater/issues](https://github.com/Evil0ctal/ChatGPT-Minecraft-Plugin-Translater/issues)

We highly welcome feedback and contributions from the community!

If this project has been helpful to you, consider giving it a ⭐️ to show your support!
