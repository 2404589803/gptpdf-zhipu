import os
import sys

# 打印当前编码
print(f"Default encoding: {sys.getdefaultencoding()}")

# 强制设置Python默认编码为UTF-8
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# load environment variables from .env file
import dotenv
dotenv.load_dotenv()

def test_use_api_key():
    from gptpdf import parse_pdf
    pdf_path = 'D:/python project/gptpdf-zhipu/examples/attention_is_all_you_need.pdf'
    output_dir = 'D:/python project/gptpdf-zhipu/examples/attention_is_all_you_need'
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_API_BASE')
    # Manually provide OPENAI_API_KEY and OPEN_API_BASE
    content, image_paths = parse_pdf(pdf_path, output_dir=output_dir, api_key=api_key, base_url=base_url, model='gpt-4o', gpt_worker=6)
    print(content.encode('utf-8').decode('utf-8'))
    print([path.encode('utf-8').decode('utf-8') for path in image_paths])
    # also output_dir/output.md is generated

def test_use_env():
    from gptpdf import parse_pdf
    pdf_path = '../examples/attention_is_all_you_need.pdf'
    output_dir = '../examples/attention_is_all_you_need/'
    # Use OPENAI_API_KEY and OPENAI_API_BASE from environment variables
    content, image_paths = parse_pdf(pdf_path, output_dir=output_dir, model='glm-4v', verbose=True)
    print(content.encode('utf-8').decode('utf-8'))
    print([path.encode('utf-8').decode('utf-8') for path in image_paths])
    # also output_dir/output.md is generated

if __name__ == '__main__':
    test_use_api_key()
    # test_use_env()
