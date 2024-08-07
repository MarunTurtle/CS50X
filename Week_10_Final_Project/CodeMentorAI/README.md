# CodeMentor AI

## Video Demo
[Watch the demo on YouTube](https://youtu.be/THAn1hq-eVc)

## Description
CodeMentor AI is an innovative tool designed to automate the generation of feedback for code snippets. Leveraging OpenAI's GPT-4 model and the Notion API, it analyzes code in various programming languages, generates insightful comments, and creates detailed Notion pages. The goal is to assist programmers by providing constructive feedback and improving code quality through automated analysis.

## Background and Motivation

### Challenges
1. **Organizing Solutions in Notion**:
   - Keeping a record of all solutions in Notion, including problem details and requirements, was labor-intensive.
   
2. **Evaluating Code Quality**:
   - Research identified four key standards for good code:
     - **Problem Understanding**: Does the code solve the core problem?
     - **Algorithm and Strategy**: Is the correct algorithm chosen? Is the time and space complexity optimal?
     - **Requirements and Readability**: Does the code meet all requirements, including error handling and readability?
     - **Maintainability and Scalability**: Is the code easy to maintain and adapt?

### Solution
CodeMentor AI automates the process of logging solutions in Notion and evaluating code based on the identified standards.

## Key Features

1. **Automated Code Review**: Utilizes OpenAI's GPT-4 model to generate detailed comments on code.
2. **Web Scraping**: Extracts problem details from competitive programming websites using BeautifulSoup.
3. **Notion Integration**: Creates comprehensive Notion pages with problem details, code snippets, and generated feedback.
4. **Multi-source Data Collection**: Fetches problem data from solved.ac and ACM-ICPC for a holistic view.

## Project Files

1. **main.py**: The main script that runs the application.
2. **keys.py**: Contains the API keys and tokens required for OpenAI and Notion API access.
3. **langs.py**: Includes a mapping of programming languages used in the project.
4. **urls.txt**: A text file containing URLs of problems or datasets used in the project.

## Obtaining API Keys

### OpenAI API Key
1. Visit the [OpenAI website](https://www.openai.com/) and sign in.
2. Navigate to the API section and generate a new API key.
3. Copy the API key and replace `'openai_api_key'` in your `keys.py` file with this key.

### Notion Integration Token
1. Go to the [Notion website](https://www.notion.so/) and log in.
2. Create a new integration by visiting [Notion Integrations](https://www.notion.so/my-integrations).
3. Generate a new integration token and copy it.
4. Share your integration with the specific Notion page or workspace you want to use.
5. Replace `'notion_website_token'` in your `keys.py` file with this token.

### Notion Page ID
1. Open the Notion page you want to link with your project.
2. Copy the URL of the Notion page.
3. Extract the last part of the URL (after the last slash) which is the Page ID.
4. Replace `'notion_page_id'` in your `keys.py` file with this Page ID.

Example `keys.py` file:
```python
openai = 'your_openai_api_key'
token = 'your_notion_integration_token'
page_id = 'your_notion_page_id'
```

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone [GitHub Repository URL]
   ```
2. **Navigate to the project directory**:
   ```bash
   cd CodeMentor_AI
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python main.py
   ```

## Detailed Description

### Functionality Overview

- **API Key Setup**: The project requires API keys for OpenAI and Notion, stored in the `keys.py` file. Ensure you have valid keys before running the application.
- **Code Comments Generation**: The `code_comments` function uses OpenAI's GPT-4 model to analyze the provided code snippet and generate comments in Korean, with key programming terms in English.
- **Problem Data Fetching**: The `fetch_complete_problem_data` function retrieves problem details from solved.ac and ACM-ICPC websites.
- **Code Retrieval**: The `get_code` function extracts code and related metadata from a given URL using BeautifulSoup.
- **Notion Page Creation**: The `post_page` function creates and populates a Notion page with the extracted problem details and code.

### Design Choices

- **Language**: Python was chosen for its rich ecosystem of libraries and ease of use for web scraping, API integration, and natural language processing.
- **Modular Structure**: The code is organized into functions to enhance readability and maintainability.
- **API Integration**: The project integrates with external APIs (OpenAI and Notion) to automate complex tasks like natural language processing and content management.

## Future Improvements

- **Enhanced Feedback**: Improve the accuracy and depth of feedback by refining the prompts and parameters used in the OpenAI API.
- **User Interface**: Develop a graphical user interface (GUI) to make the tool more accessible and user-friendly.
- **Multi-language Support**: Expand the tool to support multiple programming languages and provide feedback in different languages.

## Conclusion
CodeMentor AI demonstrates the potential of combining artificial intelligence with automation to improve code quality and productivity. By automating the feedback process, it helps programmers receive timely and constructive feedback, ultimately enhancing their coding skills and project outcomes.