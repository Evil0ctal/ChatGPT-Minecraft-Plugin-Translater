class ChatGPT_Prompts:
    """
    [中文]
    ChatGPT_Prompts类用于存储ChatGPT模型的提示词以及不同语言的翻译提示词，以便于在主函数中调用。

    [English]
    ChatGPT_Prompts class is used to store the prompts of ChatGPT model and the translated prompts in different languages for calling in the main function.
    """

    def __init__(self):
        self.prompts = {
            # Chinese/中文
            "zh": """
                中文翻译Minecraft插件的YAML（`.yml`）配置文件，请遵循以下的规则对文件完成翻译：
                1. 键名和属性名：YAML文件中的键（key）和属性名通常被插件代码直接引用，用于获取配置文件中的值。这些键名和属性名应保持原样，不进行翻译。
                2. 命名空间和技术标识符：如`minecraft:diamond_sword`这样的命名空间和技术标识符是Minecraft和插件功能的一部分，它们需要保持原样，以确保游戏和插件的正常运作。
                3. 中文和英文标点符号：使用英文标点符号:而不是：确保yml文件的结构不被破坏。
                4. 命令和权限节点：插件中定义的命令（如`/give`）和权限节点（如`pluginname.command.give`）是与插件内部逻辑密切相关的，这些也需要保持原样，因为翻译会导致命令或权限无法被识别。
                5. 格式化代码和颜色代码：YAML文件中可能会使用特殊的格式化代码（如`&c`表示红色文字）和颜色代码，这些是控制文本显示样式的，不应进行翻译。
                6. 数据值和枚举值：某些配置选项可能接受一组特定的值（如`true`/`false`，或者特定的枚举值），这些值通常是代码逻辑的一部分，应当保留原文。
                7. 特殊占位符和变量：如你之前提到的PlaceholderAPI变量（例如`%player_name%`），这些特殊的占位符和变量是动态替换内容的标记，必须保持不变。
                8. 执行保留字：插件中包含如`[refresh]`，`[console]`，`[close]`，`[message]`等保留关键字，请不要翻译。
                9. 物品材质：材质将作为图片显示在游戏中，如`material: green_stained_glass_pane`中的green_stained_glass_pane是游戏物品的ID，请不要翻译。
                10. 特殊表达式：以特殊符号开头的为特殊条件表达式，如`type: "!has permission"`中的!has permission为表达式，请不要翻译。
                11. yml文件缩进：注意yml文件的缩进，在有必要的情况下对文件开头或末尾插入`\n`自动换行符。
                12. yml文件键名重复：yml文件中键名不允许重复，如有重复请修改键名。
                13. 特殊的键名：如`requirements`开头的请不要翻译，保持原有格式输出。
                14. 请注意不要添加多余符号：如当yml文件中有`view_requirement`或`type: javascript`时，不要添加```符号或其他符号。
                请遵守上面的规则对文件进行翻译，并且不要修改输入文本的格式。
                """,
            # English/英文
            "en": """
                When translating Minecraft plugin YAML (`.yml`) configuration files into English, please adhere to the following rules for completing the translation:
                1. Key and property names: Keys and property names in the YAML file are usually directly referenced by plugin code to retrieve values from the configuration file. These key and property names should remain unchanged and not be translated.
                2. Namespaces and technical identifiers: Namespaces and technical identifiers, such as`minecraft:diamond_sword`, are part of Minecraft and plugin functionality. They need to remain unchanged to ensure the game and plugins operate correctly.
                3. Chinese and English punctuation: Use English punctuation, such as`:`, instead of`：` to ensure the structure of the yml file is not disrupted.
                4. Commands and permission nodes: Commands (e.g.,`/give`) and permission nodes (e.g.,`pluginname.command.give`) defined in the plugin are closely related to the plugin's internal logic. These should also remain unchanged, as translation could cause commands or permissions to be unrecognized.
                5. Formatting codes and color codes: The YAML file may use special formatting codes (e.g.,`&c` for red text) and color codes. These control the text display style and should not be translated.
                6. Data values and enumeration values: Some configuration options may accept a set of specific values (such as`true`/`false`, or specific enumeration values). These values are usually part of the code logic and should be kept in their original form.
                7. Special placeholders and variables: Special placeholders and variables, such as those mentioned for PlaceholderAPI (e.g.,`%player_name%`), are markers for dynamically replacing content and must remain unchanged.
                8. Reserved keywords: The plugin includes reserved keywords like`[refresh]`,`[console]`,`[close]`,`[message]`, etc. Please do not translate these.
                9. Item materials: Materials will be displayed as images in the game, such as the`green_stained_glass_pane` in`material: green_stained_glass_pane` is the game item's ID. Please do not translate these.
                10. Special expressions: Expressions starting with special symbols, like`type: "!has permission"` where`!has permission` is an expression, should not be translated.
                11. YAML file indentation: Pay attention to the indentation in the YAML file, and insert`\n` newline characters at the beginning or end of the file as necessary.
                12. YAML file key duplication: Key names in the YAML file are not allowed to be duplicated. If there are duplicates, please modify the key names.
                13. Special key names: Key names starting with`requirements` should not be translated and kept in their original format.
                14. Avoid adding extra symbols: When the YAML file contains`view_requirement` or`type: javascript`, do not add ``` symbols or other symbols.
                Please follow the rules above for translating the file, and do not modify the format of the input text.
                """
        }
