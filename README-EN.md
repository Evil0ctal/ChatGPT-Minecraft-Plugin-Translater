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
   - Delete the remaining test files in the following two directories
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

## Test comparison 👁‍🗨

> Original yml file (English), from DeluxeMenus plugin.

```
menu_title: '&8Vip Skill Tree | &6Baker'
open_command:
- jobs skilltree Baker vip
- job skilltree Baker vip
size: 45
open_requirement:
  minimum_requirements: 1
  stop_at_success: true
  requirements:
    perm1:
     type: has permission
     permission: 'jobs.all.vipmaxlevel'
    perm2:
     type: has permission
     permission: 'jobs.baker.vipmaxlevel'
update_interval: 1
items:
################## VIP Skill Tree Levels
  '2':
    material: red_stained_glass
    slot: 4
    priority: 3
    display_name: '&4&nLevel 1'
    hide_attributes: true
    lore:
    - '&cAttention! Rewards can only be claimed'
    - '&cafter you level up to the shown level.'
    - ''
    - '&6Rewards:'
    - '&#eb984e➟ &a&l$&a150'
    - '&#eb984e➟ &d1.5&d&lXP &dboost for 2h'
    - '&#eb984e➟ &e0.5&e&lP &eboost for 2h'
    left_click_commands:
    - '[refresh]'
    right_click_commands:
    - '[refresh]'
  '3':
    material: lime_stained_glass
    slot: 4
    priority: 2
    view_requirement:
      requirements:
        claimed:
         type: has permission
         permission: 'jobs.vipbaker.level1'
    display_name: '&a&nLevel 1'
    hide_attributes: true
    lore:
    - '&7Reward has been claimed.'
    - ''
    - '&6Rewards:'
    - '&#eb984e➟ &a&l$&a150'
    - '&#eb984e➟ &d1.5&d&lXP &dboost for 2h'
    - '&#eb984e➟ &e0.5&e&lP &eboost for 2h'
    left_click_commands:
    - '[refresh]'
    right_click_commands:
    - '[refresh]'
  '4':
    material: orange_stained_glass
    slot: 4
    priority: 1
    update: true
    view_requirement:
      requirements:
        level:
         type: javascript
         expression: "%jobsr_user_jlevel_Baker% >= 1"
        perm:
         type: "!has permission"
         permission: 'jobs.vipbaker.level1'
    display_name: '&#e67e22&nLevel 1'
    hide_attributes: true
    lore:
    - '&aClick to claim your reward!'
    - ''
    - '&6Rewards:'
    - '&#eb984e➟ &a&l$&a150'
    - '&#eb984e➟ &d1.5&d&lXP &dboost for 2h'
    - '&#eb984e➟ &e0.5&e&lP &eboost for 2h'
    left_click_commands:
    - '[console] lp user %player_name% permission set jobs.vipbaker.level1'
    - '[console] eco give %player_name% 150'
    - '[console] lp user %player_name% permission settemp jobs.boost.Baker.exp.1.5 true 2h'
    - '[console] lp user %player_name% permission settemp jobs.boost.Baker.points.0.5 true 2h'
    - '[close]'
```

> Output file (Chinese)

```
menu_title: '&8Vip技能树 | &6面包师'
open_command:
- jobs skilltree Baker vip
- job skilltree Baker vip
size: 45
open_requirement:
  minimum_requirements: 1
  stop_at_success: true
  requirements:
    perm1:
     type: has permission
     permission: 'jobs.all.vipmaxlevel'
    perm2:
     type: has permission
     permission: 'jobs.baker.vipmaxlevel'
update_interval: 1
items:
################## VIP技能树等级
  '2':
    material: red_stained_glass
    slot: 4
    priority: 3
    display_name: '&4&n等级 1'
    hide_attributes: true
    lore:
    - '&c注意！奖励只能在达到所示等级后领取。'
    - ''
    - '&6奖励：'
    - '&#eb984e➟ &a&l$&a150'
    - '&#eb984e➟ &d1.5&d&l经验提升2小时'
    - '&#eb984e➟ &e0.5&e&l点数提升2小时'
    left_click_commands:
    - '[refresh]'
    right_click_commands:
    - '[refresh]'
  '3':
    material: lime_stained_glass
    slot: 4
    priority: 2
    view_requirement:
      requirements:
        claimed:
         type: has permission
         permission: 'jobs.vipbaker.level1'
    display_name: '&a&n等级 1'
    hide_attributes: true
    lore:
    - '&7奖励已领取。'
    - ''
    - '&6奖励：'
    - '&#eb984e➟ &a&l$&a150'
    - '&#eb984e➟ &d1.5&d&l经验提升2小时'
    - '&#eb984e➟ &e0.5&e&l点数提升2小时'
    left_click_commands:
    - '[refresh]'
    right_click_commands:
    - '[refresh]'
  '4':
    material: orange_stained_glass
    slot: 4
    priority: 1
    update: true
    view_requirement:
      requirements:
        level:
         type: javascript
         expression: "%jobsr_user_jlevel_Baker% >= 1"
        perm:
         type: "!has permission"
         permission: 'jobs.vipbaker.level1'
    display_name: '&#e67e22&n等级 1'
    hide_attributes: true
    lore:
    - '&a点击以领取奖励！'
    - ''
    - '&6奖励：'
    - '&#eb984e➟ &a&l$&a150'
    - '&#eb984e➟ &d1.5&d&l经验提升2小时'
    - '&#eb984e➟ &e0.5&e&l点数提升2小时'
    left_click_commands:
    - '[console] lp user %player_name% permission set jobs.vipbaker.level1'
    - '[console] eco give %player_name% 150'
    - '[console] lp user %player_name% permission settemp jobs.boost.Baker.exp.1.5 true 2h'
    - '[console] lp user %player_name% permission settemp jobs.boost.Baker.points.0.5 true 2h'
    - '[close]'
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
