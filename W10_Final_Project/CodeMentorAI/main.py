import requests
import openai
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import keys
from langs import langs
from notion.client import NotionClient
from notion.block import (
    SubsubheaderBlock, TextBlock, PageBlock,
    CalloutBlock, QuoteBlock, CodeBlock, ColumnListBlock, ColumnBlock
)

# Set API keys for OpenAI and Notion
openai.api_key = keys.openai
notion_token_v2 = keys.token
notion_page_id = keys.page_id

# Initialize user agent for web scraping
ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}

def code_comments(param):
    """Generate comments for a given code snippet using OpenAI's GPT-4 model."""
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {
                    'role': 'system',
                    'content': (
                        'You are a skilled programmer and experienced code reviewer. '
                        'You are proficient in analyzing Python code, explaining complex concepts clearly, '
                        'and providing constructive feedback. Discuss problem-solving, algorithm efficiency using Big-O notation, '
                        'coding best practices, and insights into code maintenance and scalability. '
                    )
                },
                {
                    'role': 'user',
                    'content': (
                        "Please analyze the provided Python code snippet."
                        "Use code markup for any code references. Review the code based on the following criteria:\n\n"
                        "1. Problem Understanding: How does the code understand the problem?\n"
                        "2. Algorithm and Strategy: Describe the chosen algorithm and problem-solving strategy, including its time complexity using Big-O notation.\n"
                        "3. Requirements and Readability: Review if the code meets all requirements and assess its readability.\n"
                        "4. Maintainability and Scalability: Evaluate the code structure for easy maintenance and how it can adapt to changing requirements.\n"
                        "The code snippet is as follows:\n" + param
                    )
                }
            ],
            temperature=0.3,
            top_p=0.2,
            max_tokens=2000
        )
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return

    return response['choices'][0]['message']['content']

def fetch_complete_problem_data(prob_n):
    """Fetch complete problem data from both solved.ac and ACM-ICPC websites."""
    print("Extracting problem information")

    # Fetch problem data from solved.ac API
    url_solved_ac = "https://solved.ac/api/v3/problem/show"
    querystring = {"problemId": str(prob_n)}
    api_headers = {"Accept": "application/json"}
    
    try:
        response_solved_ac = requests.get(url_solved_ac, headers=api_headers, params=querystring)
        response_solved_ac.raise_for_status()
        data = response_solved_ac.json()
        problemId = data['problemId']
        titleKo = data['titleKo']
        level = data['level']
        tags = [tag['displayNames'][0]['name'] for tag in data['tags']]
        solved_ac_details = [problemId, titleKo, level, tags]
    except requests.RequestException:
        print("Solved.ac API ERROR!")
        solved_ac_details = []

    # Fetch additional problem details from ACM-ICPC problem page
    url_acm_icpc = f'https://www.acmicpc.net/problem/{prob_n}'
    try:
        response_acm_icpc = requests.get(url_acm_icpc, headers=headers)
        response_acm_icpc.raise_for_status()

        soup = BeautifulSoup(response_acm_icpc.content, 'html.parser')
        problem_text = soup.select_one('#description .problem-text p').text.strip()
        input_text = soup.select_one('#input .problem-text p').text.replace('\xa0', ' ').strip()
        output_text = soup.select_one('#output .problem-text p').text.replace('\xa0', ' ').strip()

        list_sampleinput_text = []
        list_sampleoutput_text = []
        sample_index = 1
        while True:
            sample_input_text = soup.select_one(f'#sample-input-{sample_index}')
            sample_output_text = soup.select_one(f'#sample-output-{sample_index}')
            if not (sample_input_text and sample_output_text):
                break
            list_sampleinput_text.append(sample_input_text.text.replace('\xa0', ' ').strip())
            list_sampleoutput_text.append(sample_output_text.text.replace('\xa0', ' ').strip())
            sample_index += 1

        acm_icpc_details = [
            "Problem", problem_text, "Input Requirements", input_text,
            "Output Requirements", output_text, "Input Example", list_sampleinput_text,
            "Output Example", list_sampleoutput_text
        ]
    except requests.RequestException:
        print("Failed to fetch problem details from ACM-ICPC.")
        acm_icpc_details = []

    print("Problem information extraction complete")

    # Combine and return the fetched data
    return solved_ac_details + acm_icpc_details
    
def get_code(code_link):
    """Retrieve code and related metadata from a given URL."""
    with requests.Session() as session:
        print("Analyzing code")
        r = session.get(code_link, headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')

        h1_tag = soup.find('h1', class_="pull-left")
        a_tag = h1_tag.find('a', href=lambda x: x and '/problem/' in x)

        if a_tag:
            href_value = a_tag['href']
            problem_number = href_value.split('/')[-1]

        textarea_tag = soup.find('textarea', {'class': 'form-control no-mathjax codemirror-textarea'})
        if textarea_tag:
            source_code = textarea_tag.text

        divs = soup.find_all('div', {'class': 'col-md-12'})

        for div in divs:
            headline_tag = div.find('div', {'class': 'headline'})
            if headline_tag:
                h2_tag = headline_tag.find('h2')
                if h2_tag:
                    lang = h2_tag.text
                    code_lang = langs[lang]

        tds = soup.find_all('td', {'class': 'text-center'})
        info = []
        for td in tds:
            info.append(td.text)
        extra_info=info[1:]
        extra_info[0]=extra_info[0]+'KB'
        extra_info[1]=extra_info[1]+'ms'
        extra_info[2]=extra_info[2]+'B'

        print("Code analysis complete")
        return [problem_number, code_lang, source_code,extra_info]

def post_page(problem_info, submitted_code, code, extra_info, code_link):
    """Create and populate a Notion page with problem and code details."""
    try:
        client = NotionClient(token_v2=notion_token_v2)
    except Exception as e:
        print("Notion Client Error:", e)
        return
    
    print("Posting to Notion")

    page = client.get_block(notion_page_id)

    # Page title
    post_title = f'{problem_info[0]} - {problem_info[1]}'
    new_page = page.children.add_new(PageBlock, title=post_title)

    # Problem link
    link_text_block = new_page.children.add_new(TextBlock)
    link_text_block.title = f'[Problem Link](https://www.acmicpc.net/problem/{problem_info[0]})'

    # Solution link
    link_text_block = new_page.children.add_new(TextBlock)
    link_text_block.title = f'[Solution Link]({(code_link[0])})'

    # Page icon
    tier = str(problem_info[2])
    icon_url = f'https://d2gd6pc034wcta.cloudfront.net/tier/{tier}.svg'
    new_page.icon = icon_url

    # Page callout with tags
    callout_info = '/'.join(problem_info[3])
    callout = new_page.children.add_new(CalloutBlock, title=callout_info)
    callout.icon = "💡"
    callout.color = "gray_background"

    # Adding problem, input, output
    new_page.children.add_new(SubsubheaderBlock, title=problem_info[4])  # Problem headline
    problem_text_callout = new_page.children.add_new(CalloutBlock, title=problem_info[5])
    problem_text_callout.icon = "🧐"
    problem_text_callout.color = "blue_background"
    
    # Create a new column list for organizing Input and Output sections
    column_list1 = new_page.children.add_new(ColumnListBlock)

    # Create the first column for Input section
    input_column = column_list1.children.add_new(ColumnBlock)
    
    # Add a subsubheader for Input
    input_column.children.add_new(SubsubheaderBlock, title=problem_info[6])
    # Add a callout block for Input text
    input_text_callout = input_column.children.add_new(CalloutBlock, title=problem_info[7])
    input_text_callout.icon = "⌨"  # Set the icon to a keyboard
    input_text_callout.color = "yellow_background"  # Set the background color to yellow

    # Create the second column for Output section
    output_column = column_list1.children.add_new(ColumnBlock)
    # Add a subsubheader for Output
   
    output_column.children.add_new(SubsubheaderBlock, title=problem_info[8])
    # Add a callout block for Output text
    output_text_callout = output_column.children.add_new(CalloutBlock, title=problem_info[9])
    output_text_callout.icon = "🖥️"  # Set the icon to a computer monitor
    output_text_callout.color = "yellow_background"  # Set the background color to yellow

    # Sample Inputs and Outputs with headlines and texts
    column_list2 = new_page.children.add_new(ColumnListBlock)  # Add a new column list
    
    # Create the first column for input
    input_column = column_list2.children.add_new(ColumnBlock)
    input_column.children.add_new(TextBlock, title=f'**{problem_info[10]}**')  # Sample Input Headline, bold
    # Add all sample input texts under the headline
    for sample_input_text in problem_info[11]:
        input_column.children.add_new(TextBlock, title=f'{sample_input_text}', color='gray_background')  # Sample Input Texts, grey background

    # Create the second column for output
    output_column = column_list2.children.add_new(ColumnBlock)
    output_column.children.add_new(TextBlock, title=f'**{problem_info[12]}**')  # Sample Output Headline, bold
    # Add all sample output texts under the headline
    for sample_output_text in problem_info[13]:
        output_column.children.add_new(TextBlock, title=f'{sample_output_text}', color='gray_background')  # Sample Output Texts

    # Submit Info Callout
    quote_info = f"**{'Memory   '+extra_info[0]:<50}{'Time   '+extra_info[1]:^0}{'Code Length   '+extra_info[2]:>50}**"
    quote = new_page.children.add_new(QuoteBlock)
    quote.title = quote_info

    # Formatting code for display
    code_lines = code.splitlines()
    formatted_code = '\n    '.join(code_lines)
    formatted_code = '    ' + formatted_code  # Add indentation to the first line as well

    # Code block
    new_page.children.add_new(CodeBlock, title=formatted_code, language=submitted_code)

    print("Writing GPT comments")

    # code comments
    new_text_block = new_page.children.add_new(TextBlock)
    new_text_block.title = code_comments("\n".join(code_lines))

    print(f'Commit complete for problem {problem_info[0]}')

def main():
    """Main function to process input code links and manage Notion page creation."""
    while True:
        code_links = input(">>>Input Source Code Links: ")
        code_links = [code_link.strip() for code_link in code_links.split('\n')]
        if code_links[0].lower() == "done":
            break
        for code_link in code_links:
            submit_info = get_code(code_link)
            problem_info = fetch_complete_problem_data(submit_info[0])
            post_page(problem_info, submit_info[1], submit_info[2], submit_info[3], code_links)

if __name__ == "__main__":
    main()