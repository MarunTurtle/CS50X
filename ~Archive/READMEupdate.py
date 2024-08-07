import os
import re
from openai import OpenAI

def get_api_key(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading API key from {file_path}: {e}")
        return None

# Get the API key from the key.txt file and set it as an environment variable
script_dir = os.path.dirname(os.path.abspath(__file__))
key_file_path = os.path.join(script_dir, 'key.txt')
api_key = get_api_key(key_file_path)

if api_key is None:
    print("API key is missing or invalid. Exiting.")
    exit(1)

os.environ["OPENAI_API_KEY"] = api_key

# Initialize OpenAI client with the provided API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def enhance_readability_with_gpt(content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Enhance the readability of the following markdown content without changing its meaning. Improve formatting, headers, and link titles for better readability."},
                {"role": "user", "content": content}
            ],
            max_tokens=2000,
            temperature=0.5
        )
        enhanced_content = response.choices[0].message.content.strip()

        # Update effortless links
        enhanced_content = re.sub(r'\[link\]\((https://cs50\.harvard\.edu/x/2024/psets/.+?)\)',
                                  lambda m: f"[CS50 {m.group(1).split('/')[-2].capitalize()} Problem Set]({m.group(1)})",
                                  enhanced_content)

        return enhanced_content
    except Exception as e:
        print(f"Error enhancing readability with GPT: {e}")
        return content

def process_md_files(base_path):
    for root, dirs, files in os.walk(base_path):
        if 'README.md' in files:
            file_path = os.path.join(root, 'README.md')
            backup_file_path = os.path.join(root, 'beforeREADME.md')
            try:
                # Check if beforeREADME.md already exists and read from it
                if os.path.exists(backup_file_path):
                    with open(backup_file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                else:
                    # Read from the current README.md and rename it
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    os.rename(file_path, backup_file_path)

                # Enhance the readability and links with GPT
                updated_content = enhance_readability_with_gpt(content)
                
                # Save the updated content as new README.md
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

def main():
    base_path = r'C:\Users\SSAFY\Desktop\CS50X'

    # Process the markdown files in their respective folders
    try:
        process_md_files(base_path)
    except Exception as e:
        print(f"Error in main processing: {e}")

if __name__ == "__main__":
    main()
