from langchain_community.chat_message_histories import ChatMessageHistory
import os
import sys
import io
import dotenv

# 打印当前编码
print(f"Default encoding: {sys.getdefaultencoding()}")

# 强制设置Python默认编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# load environment variables from .env file
dotenv.load_dotenv()

def test_use_api_key():
    from gptpdf import parse_pdf
    pdf_path = 'D:/python project/gptpdf-zhipu/examples/attention_is_all_you_need.pdf'
    output_dir = 'D:/python project/gptpdf-zhipu/examples/attention_is_all_you_need'
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_API_BASE')
    # Manually provide OPENAI_API_KEY and OPEN_API_BASE
    content, image_paths = parse_pdf(pdf_path, output_dir=output_dir, api_key=api_key, base_url=base_url, model='glm-4v', gpt_worker=6)
    
    # 打印内容
    print(content)
    for path in image_paths:
        print(path)

def test_use_env():
    from gptpdf import parse_pdf
    pdf_path = '../examples/attention_is_all_you_need.pdf'
    output_dir = '../examples/attention_is_all_you_need/'
    # Use OPENAI_API_KEY and OPENAI_API_BASE from environment variables
    content, image_paths = parse_pdf(pdf_path, output_dir=output_dir, model='glm-4v', verbose=True)
    
    # 打印内容
    print(content)
    for path in image_paths:
        print(path)

if __name__ == '__main__':
    test_use_api_key()
    # test_use_env()

