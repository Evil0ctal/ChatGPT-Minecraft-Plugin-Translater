# Minecraft 插件配置文件ChatGPT翻译工具 🌐

自述文档语言: [English](./README-EN.md) | [简体中文](./README.md)

## 这是什么? 🤔

这个工具能够帮助您将Minecraft Java服务器插件的配置yml文件翻译成不同的语言。它基于OpenAI的ChatGPT 3.5模型，并内置了中文和英文两套提示词，开箱即用，准确率高达99%。此外，它还支持大型文件的拆分与合并，以及批量处理文件，提高您的工作效率，大型yaml文件的处理使用PKVPM算法来对文件进行拆分和合并，具体实现请参考：[多态键值路径映射（PKVPM-Polymorphic Key-Value Path Mapping）](https://github.com/PKVPM/PKVPM)

## 功能特点 🚀

- **高准确率翻译**：基于OpenAI ChatGPT 3.5模型，准确率达99%。
- **多语言支持**：内置中文和英文提示词，支持更多语言的翻译。
- **大型文件处理**：支持大型文件的拆分与合并（使用PKVPM算法）。
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
   - 删除下面两个目录内的残留测试文件
   - 将单个或多个yml配置文件放入指定的输入文件夹`Input_Files`
   - 执行脚本，查看输出文件夹`Output_Files`

4. **检查翻译结果**：
   
   - 翻译完成后，检查输出文件夹中的文件。
   - 确认翻译结果符合预期。

5. **切换语言（可选）**

- 默认的输出语言为： `英文 -> 中文`

在`main.py`中编辑可以进行切换原始语言和目标语言：

```python
# 你可以在这自定义输出语言/You can customize the output language here
output_language = "Simplified Chinese"

# Use English as the output language
# output_language = "English"
```

## 测试对比 👁‍🗨

> 原始yml文件（英文），来自DeluxeMenus插件。

```yaml
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

> 输出文件（中文）

```yaml
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

