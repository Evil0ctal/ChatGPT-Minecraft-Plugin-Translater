# Minecraft 插件配置文件ChatGPT翻译工具 🌐

自述文档语言: [English](./README-EN.md) | [简体中文](./README.md)

## 这是什么? 🤔

这个工具能够帮助您将Minecraft Java服务器插件的配置yml文件翻译成不同的语言。它基于OpenAI的ChatGPT 3.5模型，并内置了中文和英文两套提示词，开箱即用，准确率高达99%。此外，它还支持大型文件的拆分与合并，以及批量处理文件，提高您的工作效率。

## 功能特点 🚀

- **高准确率翻译**：基于OpenAI ChatGPT 3.5模型，准确率达99%。
- **多语言支持**：内置中文和英文提示词，支持更多语言的翻译。
- **大型文件处理**：支持大型文件的拆分与合并。
- **批量文件处理**：一次性处理多个配置文件。
- **用户友好**：简单易用，开箱即用。

## 使用指南 📖

1. **准备工作**：
   
   - 确保您的系统已安装Python 3.6或更高版本。
   - 安装必要的Python库：`pip install -r requirements.txt`。
2. **设置OpenAI API密钥**：
   
   - 访问[OpenAI API](https://openai.com/api/)获取您的API密钥。
   - 在脚本中配置您的API密钥，或在运行脚本后输入你的API密钥。
3. **运行脚本**：

- `python3 main.py`
- 将单个或多个yml配置文件放入指定的输入文件夹`Original_Files`
- 执行脚本，查看输出文件夹`ChatGPT_Translater_Output`

5. **检查翻译结果**：
   
   - 翻译完成后，检查输出文件夹中的文件。
   - 确认翻译结果符合预期。

6.**切换语言（可选）**

- 默认的输出语言为： `英文 -> 中文`

在`main.py`中编辑可以进行切换原始语言和目标语言：

```python
# 使用中文提示词
prompt = ChatGPT_Prompts.prompts["zh"]

# Use English prompts
_prompt = ChatGPT_Prompts.prompts["en"]
```

## 注意事项 ⚠️

- 翻译结果可能需要手动审核，以确保专业术语和上下文的准确性。
- 大型文件处理可能需要较长时间，具体取决于文件大小和系统性能。
- 修改`main.py`以限制Token的使用数量，默认最大Token为`10240`。

## 联系方式 📧

如果您在使用过程中遇到任何问题，或者有任何建议，欢迎通过以下方式联系我们：

- **Email**: evil0ctal1985@gmail.com
- **GitHub Issues**: [https://github.com/Evil0ctal/ChatGPT-Minecraft-Plugin-Translater/issues](https://github.com/Evil0ctal/ChatGPT-Minecraft-Plugin-Translater/issues)

我们非常欢迎社区的反馈和贡献！

如果这个项目对你有帮助，不妨给个⭐️支持一下吧！
