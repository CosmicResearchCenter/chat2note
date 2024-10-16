# 项目简介

[中文](./README.md) [English](./README_EN.md)

`Chat2Note` 是一个可将与 `ChatGPT` 的对话转换为笔记的工具，方便保存和回顾。`Chat2Note`提供了可视化预览笔记的Web界面，可以试试查看笔记生成效果，并及时修改并导出。

# 安装

## 前置要求
- 操作系统：`Windows` 或 `MacOS`
- 已安装 `Chrome` 浏览器
- `Python 3.8+`
- 能正常访问 `ChatGPT` 网站
##  完整版
### 后端
#### 将项目克隆到本地：
 ```bash
 git clone https://github.com/CosmicResearchCenter/chat2note.git
 ```
进入后端根目录
```bash
cd chat2note/api
```
#### 配置`.env` 
```bash
cp .env_copy .env
vim .env
```

```.env
MYSQL_IP=localhost
MYSQL_PORT=3306
MYSQL_BASE=chat2note
MYSQL_USER=chat2note
MYSQL_PASSWORD=chat2note
```
如果有MySQL实例，可根据自己的mysql信息修改并且不需要启动mysql容器，没有可以不用修改

#### 启动mysql容器
```bash
docker-compose up -d
```

#### 创建虚拟环境并激活
```bash
python -m venv venv
source venv/bin/activate #MacOS
.\venv\Scripts\activate #Windows
```

#### 安装依赖
```bash
pip install -r requirements.txt
```
#### 数据库迁移
```bash
alembic upgrade head
```

#### 启动后端
```bash
python app.py
```

### 前端
#### 进入前端根目录
```bash
cd ../web/
```

#### 构建Docker镜像
```bash
docker build -t chat2note_web .
```
#### 运行
```bash
docker run -d --name chat2note_web -p 2024:80 chat2note_web
```

这是就可以在浏览器上预览了
[http://127.0.0.1:2024/](http://127.0.0.1:2024/)

只需要将对ChatGPT对话的分享链接`https://chatgpt.com/share/xxxxx`输入到输入框，回车，然后稍等片刻即可看到笔记的生成效果了。


## 命令行版
1. 将项目克隆到本地：
   ```bash
   git clone https://github.com/CosmicResearchCenter/chat2note.git
   ```
2. 进入项目目录并创建虚拟环境
	```bash
	cd chat2note/api
	python -m venv venv
	```
3. 激活环境并安装依赖：
   ```bash
   source ./venv/bin/activate
   pip install .
   ```

# 命令行版使用指南
###  设置环境变量

请根据操作系统设置以下环境变量：

####  Windows

```bash
$env:BASE_URL="你的 OPENAI API 基础 URL"
$env:API_KEY="你的 OPENAI API 密钥"
$env:MODEL="模型名称"
```

#### MacOS

```bash
export BASE_URL="你的 OPENAI API 基础 URL"
export API_KEY="你的 OPENAI API 密钥"
export MODEL="模型名称"
```

###  运行工具

将 `ChatGPT` 对话的分享链接与以下命令一起使用：

```bash
chat2note -u https://chatgpt.com/share/xxxxx
```

###  成功提示

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
  - [x] OpenAI
  - [ ] ClaudeAI
  - [x] 智普AI
  - [x] 豆包
  - [x] 讯飞星火
- [ ] 支持通过爬虫抓取协议内容
- [ ] 读取微信聊天记录生成笔记