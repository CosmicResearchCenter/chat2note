from api.core.chat2note.get_logs import ChatLoger
from api.core.chat2note.chat2note import chat_to_note
import argparse
import os
import shutil

# 获取各个配置信息
def get_config():
    api_key = os.getenv('API_KEY')
    base_url = os.getenv('BASE_URL','https://api.openai.com/v1')
    model = os.getenv('MODEL')

    return api_key, base_url, model


def main():

    # 获取终端的宽度
    terminal_width = shutil.get_terminal_size().columns

    
    # 计算需要的减去'start'的长度
    dash_count = terminal_width - len("start")

    # 输出一行适应终端宽度的 "---start---"
    print(f"{'-' * (dash_count // 2)}start{'-' * (dash_count // 2)}")
    

    parser = argparse.ArgumentParser(description="This is a tool that can automatically translate the chat log into a note using OpenAI API")
    
    # 定义命令行参数
    parser.add_argument("-u", "--url", help="The URL of the chat log with Shared link")
    parser.add_argument("-api_key", help="API key to use for operations")
    parser.add_argument("-base_url", help="Base URL for operations")
    parser.add_argument("-model", help="Base URL for operations")

    args = parser.parse_args()

    # 根据不同的命令行参数执行不同的操作
    if args.url:
        api_key, base_url, model = get_config()
        url = args.url
        chat_loger = ChatLoger(url=url)
        chat_logs_user = chat_loger.get_log_user()
        chat_logs_assistant = chat_loger.get_log_assistant()
        chat_logs = chat_loger.parse_log(chat_logs_user, chat_logs_assistant)
        chat_to_note(chat_logs,api_key=api_key,model=model,base_url=base_url)
    elif args.api_key:
        os.environ['API_KEY'] = args.api_key
        print(f"config {args.api_key}")
    elif args.base_url:
        os.environ['BASE_URL'] = args.base_url
        print(f"config {args.base_url}")
    elif args.model:
        os.environ['MODEL'] = args.model
        print(f"config {args.model}")
    else:
        print("No valid arguments provided. Use -h for help.")
    # 计算需要的减去'end'的长度
    dash_count = terminal_width - len("end")
    # 输出一行适应终端宽度的 "---end---"
    print(f"{'-' * (dash_count // 2)}end{'-' * (dash_count // 2)}")
if __name__ == "__main__":
    main()

