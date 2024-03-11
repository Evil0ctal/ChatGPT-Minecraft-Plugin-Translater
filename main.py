import os
import json

from pkvpm.parser import Parser
from ChatGPT_Prompts import ChatGPT_Prompts
from datetime import datetime
from openai import OpenAI

# 初始化PKVPM解析器/Initialize PKVPM parser
parser = Parser()


# 读取指定目录下的文件/Read files in the specified directory
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


# 保存文件到指定目录/Save files to the specified directory
def save_file(path, content):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)


# 拆分文件内容为多个部分/Split the file content into multiple parts
def split_content(content, max_size):
    # 检查文件内容长度是否超过最大长度/Check if the file content length exceeds the maximum length
    if len(content) < max_size:
        print(f"文件内容长度{len(content)}未超过最大长度{max_size}，无需拆分。")
        print(f"File content length {len(content)} does not exceed the maximum length {max_size}, no need to split.")
        return [content]
    else:
        print(f"文件内容长度{len(content)}超过最大长度{max_size}，开始使用PKVPM算法拆分内容...")
        print(f"File content length {len(content)} exceeds the maximum length {max_size}, start splitting the content using PKVPM algorithm...")
        # 使用PKVPM算法拆分内容/Use PKVPM algorithm to split the content
        pkvpm_content = parser.parse(content)
        # print(f"YAML to PKVPM:\n{pkvpm_content}")
        # 将PKVPM内容按行分割/Divide the PKVPM content into lines
        lines = pkvpm_content.split('\n')
        parts = []
        current_part = ''
        for line in lines:
            # 检查加上当前行（加上换行符）后是否会超过最大长度限制
            # Check if adding the current line (plus the newline character) will exceed the maximum length limit
            if len(current_part + line + '\n') > max_size:
                # 如果当前部分非空，则保存当前部分
                # If the current part is not empty, save the current part
                if current_part:
                    parts.append(current_part)
                    current_part = ''
                # 如果当前行本身就超过最大长度，直接忽略.
                # If the current line itself exceeds the maximum length, ignore it directly.
                if len(line + '\n') <= max_size:
                    current_part = line + '\n'
            else:
                # 如果不超过长度限制，则加入当前行到当前部分
                # If it does not exceed the length limit, add the current line to the current part
                current_part += line + '\n'

        # 保存最后的部分（如果有）
        # Save the last part (if any)
        if current_part:
            parts.append(current_part)
        return parts


# 与openai交互/Interact with openai
def openai_interact(prompt, part,
                    model="gpt-3.5-turbo-16k-0613",
                    temperature=1, max_tokens=4096,
                    top_p=1, frequency_penalty=0,
                    presence_penalty=0):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": part
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    # 返回翻译结果
    # print(f"响应：{response}")
    # 读取ChatCompletion对象中的choices字段中的message字段中的content字段
    return response.choices[0].message.content


# 更新翻译日志文件/Update the translation log file
def update_translation_log(log_path, file_name):
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            log = json.load(f)
    else:
        log = {}

    log[file_name] = str(datetime.now())
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=4, ensure_ascii=False)


# 检查文件是否已翻译/Check if the file has been translated
def check_translation_log(log_path, file_name):
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            log = json.load(f)
            if file_name in log:
                return True
    return False


# 处理单一文件的翻译并保存/Process the translation of a single file and save it
def process_file(file_path, _model, _output_language, _max_tokens, output_folder, log_path) -> int:
    """
    :return: 1表示翻译成功，0表示翻译失败/1 for success, 0 for failure
    """
    # 提示词类对象/Class object of prompts
    ChatGPT_Prompt = ChatGPT_Prompts(_output_language)
    prompt_for_short_file = ChatGPT_Prompt.prompts["short_file"]
    prompt_for_long_file = ChatGPT_Prompt.prompts["long_file"]

    file_name, file_extension = os.path.basename(file_path).rsplit('.', 1)
    content = read_file(file_path)
    parts = split_content(content, _max_tokens)
    print(f"原始文件内容长度：{len(content)}")
    print(f"共拆分为{len(parts)}部分进行翻译")

    # print(f"Original file content length: {len(content)}")
    # print(f"Split into {len(parts)} parts for translation")

    # print(f"拆分后的部分：{parts}")
    # print(f"Split parts: {parts}")

    # 根据文件内容长度选择不同的提示词/Choose different prompts based on the length of the file content
    _prompt = prompt_for_short_file if len(content) < _max_tokens and len(parts) == 1 else prompt_for_long_file
    # print(f"使用提示词：{_prompt}")
    # print(f"Using prompt: {_prompt}")

    # 逐个部分翻译/Translate each part
    translated_parts = []
    parts_count = 0
    for part in parts:
        parts_count += 1
        print(f"翻译第{parts_count}部分...")
        print(f"Translating the {parts_count} part...")

        if len(parts) == 1:
            translated_part = openai_interact(prompt=_prompt, part=part, model=_model, max_tokens=_max_tokens)
            # print(f"第{parts_count}部分翻译结果：{translated_part}")
            # print(f"The {parts_count} part of the translation result: {translated_part}")
            translated_parts.append(translated_part)
        else:
            # 确认ChatGPT的翻译是否成功，如果失败则再次尝试/Confirm if the translation by ChatGPT is successful, if failed then try again
            try:
                translated_part = openai_interact(prompt=_prompt, part=part, model=_model, max_tokens=_max_tokens)
                # print(f"第{parts_count}部分翻译结果：{translated_part}")
                # print(f"The {parts_count} part of the translation result: {translated_part}")
                translated_content = parser.to_yaml(translated_part)
                translated_parts.append(translated_part)
            except Exception as e:
                print(f"第{parts_count}部分翻译失败：{e}")
                print(f"如果再次失败，请检查文件内容。")
                print(f"The {parts_count} part of the translation failed: {e}")
                print(f"If it fails again, please check the file content.")
                translated_part = openai_interact(prompt=_prompt, part=part, model=_model, max_tokens=_max_tokens)
                # print(f"第{parts_count}部分翻译结果：{translated_part}")
                # print(f"The {parts_count} part of the translation result: {translated_part}")
                translated_content = parser.to_yaml(translated_part)
                translated_parts.append(translated_part)

    print(f"翻译完成，共{len(translated_parts)}部分")
    print(f"Translation completed, {len(translated_parts)} parts in total")

    # 重组翻译后的内容
    if len(translated_parts) == 1:
        translated_content = "".join(translated_parts)
    else:
        # 使用PKVPM算法翻译内容成为原始格式/Translate the content back to the original format using PKVPM algorithm
        final_content = '\n'.join(translated_parts)
        translated_content = parser.to_yaml(final_content)

    # print(f"翻译结果：{translated_content}")
    print(f"翻译结果长度{len(translated_content)}")

    # print(f"Translation result: {translated_content}")
    print(f"Length of translation result: {len(translated_content)}")

    # 保存文件
    output_file_path = os.path.join(output_folder, f"{file_name}.{file_extension}")
    save_file(output_file_path, translated_content)
    update_translation_log(log_path, os.path.basename(file_path))
    print(f"文件翻译完成: \n{os.path.basename(file_path)}\n结果已保存到：\n{output_file_path}")
    print(f"File translation completed: \n{os.path.basename(file_path)}\nResult has been saved to: \n{output_file_path}")

    return 1


# 遍历文件夹并处理每个文件
def process_directory(directory_path, _model, _output_language, _max_tokens, output_folder, log_path) -> int:
    """
    :return: 返回已翻译的文件数量
    """
    translated_count = 0
    for file in os.listdir(directory_path):
        print(f"当前正在处理文件：{file}")
        print(f"Currently processing file: {file}")
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path) and not check_translation_log(log_path, file):
            translated_count += 1
            process_file(file_path, _model, _output_language, _max_tokens, output_folder, log_path)
        else:
            print(f"文件 {file} 已被翻译或不是文件，跳过...")
            print(f"File {file} has been translated or is not a file, skipping...")
    return translated_count


# 主函数逻辑
def main(_output_language, _model, _max_tokens, _input_path, _output_path):
    # 确保输出文件夹存在/Ensure the output folder exists
    os.makedirs(_output_path, exist_ok=True)
    log_path = os.path.join(_output_path, "translation_log.json")

    # 处理输入路径或文件/Process the input path or file
    translated_count = 0
    if os.path.isdir(_input_path):
        print("输入路径是文件夹，开始批量处理...")
        print("Input path is a directory, start batch processing...")
        translated_count = process_directory(_input_path, _model, _output_language, _max_tokens, _output_path, log_path)
    elif os.path.isfile(_input_path):
        print("输入路径是单一文件，开始处理...")
        print("Input path is a single file, start processing...")
        translated_count = process_file(_input_path, _model, _output_language, _max_tokens, _output_path, log_path)
    else:
        print("输入路径不是有效的文件或文件夹。")
        print("The input path is not a valid file or directory.")

    print(f"翻译完成，共翻译{_input_path}下的{translated_count}个文件。")
    print(f"Translation completed, {translated_count} files have been translated under {_input_path}.")

    # 删除JSON日志文件(可选)/Delete the JSON log file (optional)
    # if os.path.exists(log_path):
    #     os.remove(log_path)


if __name__ == '__main__':
    # 初始化openai客户端/Initialize openai client
    api_key = input("请输入OpenAI API密钥/Please enter your OpenAI API key: ")
    client = OpenAI(api_key=api_key)

    # 模型名称/Model name
    model = "gpt-3.5-turbo-16k-0613"

    # 你可以在这自定义输出语言/You can customize the output language here
    output_language = "Simplified Chinese"

    # Use English as the output language
    # output_language = "English"

    # 输入文件路径/Path of input files
    input_file_path = r".\Input_Files"

    # 输出文件路径(不要包含\结尾)/Path of output files (without \ at the end)
    output_file_path = r".\Output_Files"

    # 主函数/Main function
    main(_output_language=output_language,
         _model=model,
         _max_tokens=4096,
         _input_path=input_file_path,
         _output_path=output_file_path)
