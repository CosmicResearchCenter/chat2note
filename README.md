# 项目简介

`ChatGPT-to-Note` 是一个工具，可将与 `ChatGPT` 的对话转换为笔记，方便保存和回顾。

# 安装

## 前置要求
- 操作系统：`Windows` 或 `MacOS`
- 已安装 `Chrome` 浏览器
- `Python 3.8+`
- 能正常访问 `ChatGPT` 网站

## 安装步骤
1. 将项目克隆到本地：
   ```bash
   git clone https://github.com/CosmicResearchCenter/chat2note.git
   ```

2. 进入项目目录并安装依赖：
   ```bash
   pip install .
   ```

# 使用指南

## 设置环境变量

请根据操作系统设置以下环境变量：

### Windows

```bash
$env:BASE_URL="你的 OPENAI API 基础 URL"
$env:API_KEY="你的 OPENAI API 密钥"
$env:MODEL="模型名称"
```

### MacOS

```bash
export BASE_URL="你的 OPENAI API 基础 URL"
export API_KEY="你的 OPENAI API 密钥"
export MODEL="模型名称"
```

## 运行工具

将 `ChatGPT` 对话的分享链接与以下命令一起使用：

```bash
chat2note -u https://chatgpt.com/share/xxxxx
```

## 成功提示

当工具成功运行时，会看到如下提示：

```
-------------------------------------------------start-------------------------------------------------
Retrieving user conversation history.
Successfully retrieved user conversation history.
Retrieving AI conversation history.
Successfully retrieved AI conversation history.
Parsing conversation history
Conversation history parsing completed
Generating note ...
Note generation complete
Generating file name ...
The file name is generated, and the file name is xxxxx
Note has been saved to xxxx.md file
--------------------------------------------------end--------------------------------------------------
```

# 后续计划

- [ ] 支持更多模型
- [ ] 支持通过爬虫抓取协议内容
