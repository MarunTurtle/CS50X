import os
from openai import OpenAI

# Initialize OpenAI client with the provided API key
client = OpenAI(api_key="")

def summarize_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Summarize the following README file into one sentence."},
            {"role": "user", "content": content}
        ],
        max_tokens=50,
        temperature=0.5
    )
    summary = response.choices[0].message.content.strip()
    return summary

def generate_toc_and_summaries(base_path, output_file, readme_dir):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(base_path):
            # Exclude hidden directories and specified directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'static', 'templates'}]
            level = root.replace(base_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            folder_name = os.path.basename(root)
            f.write('{}{}/\n'.format(indent, folder_name))
            
            readme_file = os.path.join(readme_dir, f"{folder_name}_README.md")
            if os.path.exists(readme_file):
                summary = summarize_readme(readme_file)
                f.write('{}    {}\n'.format(indent, summary))

def main():
    base_path = r'C:\Users\SSAFY\Desktop\CS50X'
    output_file = r'C:\Users\SSAFY\Desktop\CS50X_README.md'
    readme_dir = r'C:\Users\SSAFY\Desktop'

    # Generate Table of Contents and summaries
    generate_toc_and_summaries(base_path, output_file, readme_dir)

if __name__ == "__main__":
    main()
