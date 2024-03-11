class ChatGPT_Prompts:
    """
    [中文]
    ChatGPT_Prompts类用于存储ChatGPT模型的提示词以及不同语言的翻译提示词，以便于在主函数中调用。

    [English]
    ChatGPT_Prompts class is used to store the prompts of ChatGPT model and the translated prompts in different languages for calling in the main function.
    """

    def __init__(self, output_language: str = "Simplified Chinese"):
        self.output_language = output_language
        self.prompts = {
            # For short file/短文件
            "short_file": f"""
                When translating Minecraft plugin YAML (`.yml`) configuration files, please adhere to the following rules for completing the translation:
                Target output language: {output_language}
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
                """,
            # For long file/长文件
            "long_file": f"""
            # mission details:
            You will be working with a batch of YAML configuration files for Minecraft plugins that have been converted into linear format for easy translation. Examples of linear formats and conversion rules have been given, and your goal is to translate the text content in the file that is directly facing the player, while ensuring that those technical keywords and code that are critical to the plugin's functionality and game logic remain intact.
            ## Output language: {self.output_language}
            ## SOP (Standard Operating Procedure) strategy:
            1. **Keep key names and property names unchanged**: These are usually referenced directly by plugin code and are key to getting configuration values and should not be translated.
            2. **Do not translate material naming (material)**: such as `minecraft:green_stained_glass_pane`, the game Items ID with an underline remains as it is to ensure that the game and plug-ins work properly.
            3. **Use English punctuation marks**: Ensure the structural integrity of the YAML file and use punctuation marks such as English colons.
            4. **Command and permission nodes remain as they are**: These are closely related to the internal logic of the plug-in, and translation may lead to unrecognizability.
            5. **Formatting and color codes are not translated**: Codes such as `&d&l` are used to control the text display style and color and have specific functions in the game.
            6. **Data values and enumeration values remain as they are**: These values are part of the code logic, such as `true`/`false`.
            7. **Special placeholders and variables remain unchanged**: such as `%player_name%`, etc. These words with `%` symbols are used for dynamic content replacement.
            8. **Reserved words are not translated**: keywords such as `[refresh]`, `[close]`, `[console]`,`[str]`, `[int]`, `[bool]`, `[list]`,`[float]`,`[|str]`, `[|int]`, `[|bool]`,`[|float]`), etc, and other words in symbols [] are not needed to be translated.
            9. **Item material remains unchanged**: Generally, the key name is material or other values. These are the IDs of internal items in the game, such as `green_stained_glass_pane`, and do not need to be translated.
            10. **Special expressions are not translated**: Expressions, such as `!has permission`, remain unchanged.
            11. **Special key names such as `requirements` are not translated**: Keep the original format and content of these key names.
            12. **Avoid adding unnecessary symbols**: For example, do not add unnecessary symbols for `view_requirement` or `type: javascript`, etc.
            13. **No addition or deletion of content**: Follow the original YAML file content and do not modify it without authorization.
            14. **Keep linear format unchanged**: Do not change the format and order of the input text.
            # Note
            Please follow the SOP policy above to appropriately translate direct-to-player text while keeping critical technical content intact to ensure the integrity of plugin functionality and game logic.
            """
        }
