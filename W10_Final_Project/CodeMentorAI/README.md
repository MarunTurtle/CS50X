# CodeMentor AI

#### Video Demo: [(https://youtu.be/THAn1hq-eVc)]

#### Description:
The CodeMentor AI project is an innovative tool designed to automate the generation of feedback for code snippets. This project leverages the capabilities of OpenAI's GPT-4 model and the Notion API to analyze code in various programming languages, generate insightful comments, and create detailed Notion pages. The project aims to assist programmers by providing constructive feedback and improving code quality through automated analysis.

### Background and Motivation:
1. While studying CS50X and solving coding problems on BOJ (a Korean version of Leetcode), I encountered two main challenges:
   - **Challenge 1:** I wanted to keep a record of all my solutions in Notion, including problem details, requirements, and my solutions in a neat and organized style. However, manually copying and pasting all this information was too labor-intensive.
   - **Challenge 2:** I wanted to evaluate if my code was truly good. Through research, I identified four key standards for good code:
     - **Problem Understanding:** Does the code solve the core problem it states?
     - **Algorithm and Strategy:** Did the code choose the correct algorithm, method, or libraries to solve the problem? Does it have optimal Big O time and space complexity?
     - **Requirements and Readability:** Does the code meet all the requirements, including error handling and readability?
     - **Maintainability and Scalability:** Is the code structure easy to maintain and adapt to changing requirements?

2. To address these challenges, I developed CodeMentor AI, a program that automates the process of logging solutions in Notion and evaluating code based on the identified standards.

### Key Features:
1. **Automated Code Review:** Utilizes OpenAI's GPT-4 model to generate detailed comments on code in various programming languages.
2. **Web Scraping:** Extracts problem details from various competitive programming websites using BeautifulSoup.
3. **Notion Integration:** Creates comprehensive Notion pages with problem details, code snippets, and generated feedback.
4. **Multi-source Data Collection:** Fetches problem data from solved.ac and ACM-ICPC to provide a holistic view of the problem.

### Project Files:
1. **main.py:** The main script that runs the application. It handles user input, processes data, and manages the creation of Notion pages.
2. **keys.py:** Contains the API keys and tokens required for OpenAI and Notion API access.
3. **langs.py:** Includes a mapping of programming languages used in the project.
4. **urls.txt:** A text file containing URLs of problems or datasets used in the project.

### Obtaining API Keys

To set up the `keys.py` file with the necessary API keys and tokens, follow these steps:

1. **OpenAI API Key:**
   - Visit the [OpenAI website](https://www.openai.com/) and sign in to your account.
   - Navigate to the API section and generate a new API key.
   - Copy the API key and replace `'openai_api_key'` in your `keys.py` file with this key.

2. **Notion Integration Token:**
   - Go to the [Notion website](https://www.notion.so/) and log in to your account.
   - Create a new integration by visiting [Notion Integrations](https://www.notion.so/my-integrations).
   - Generate a new integration token and copy it.
   - Share your integration with the specific Notion page or workspace you want to use.
   - Replace `'notion_website_token'` in your `keys.py` file with this token.

3. **Notion Page ID:**
   - Open the Notion page you want to link with your project.
   - Copy the URL of the Notion page.
   - The URL will be in the format `https://www.notion.so/yourusername/PageName-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.
   - Extract the last part of the URL (after the last slash) which is the Page ID.
   - Replace `'notion_page_id'` in your `keys.py` file with this Page ID.

Here is an example of what your `keys.py` file should look like after adding the keys:

```python
openai = 'your_openai_api_key'
token = 'your_notion_integration_token'
page_id = 'your_notion_page_id'
```

### Installation and Setup:
To set up and run the CodeMentor AI, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [GitHub Repository URL]
   ```
2. **Navigate to the project directory:**
   ```bash
   cd CodeMentor_AI
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   python main.py
   ```

### Detailed Description:
#### Functionality Overview:
- **API Key Setup:**
  The project requires API keys for OpenAI and Notion. These keys are stored in the `keys.py` file. Ensure you have valid keys before running the application.

- **Code Comments Generation:**
  The `code_comments` function uses OpenAI's GPT-4 model to analyze the provided code snippet and generate comments in Korean, with key programming terms in English. This function ensures that the feedback is detailed and helpful for improving code quality.

- **Problem Data Fetching:**
  The `fetch_complete_problem_data` function retrieves problem details from solved.ac and ACM-ICPC websites. It combines the data from both sources to provide comprehensive problem information.

- **Code Retrieval:**
  The `get_code` function extracts code and related metadata from a given URL. It uses BeautifulSoup to parse the HTML content and extract relevant information such as problem number, programming language, and code snippet.

- **Notion Page Creation:**
  The `post_page` function creates and populates a Notion page with the extracted problem details and code. It organizes the content into structured sections and adds generated comments to the page.

#### Design Choices:
- **Language:** Python was chosen for its rich ecosystem of libraries and ease of use for web scraping, API integration, and natural language processing.
- **Modular Structure:** The code is organized into functions to enhance readability and maintainability. Each function has a specific responsibility, making the code easier to understand and modify.
- **API Integration:** The project integrates with external APIs (OpenAI and Notion) to enhance its functionality. This choice allows for the automation of complex tasks such as natural language processing and content management.

### Future Improvements:
- **Enhanced Feedback:** Improve the accuracy and depth of feedback by refining the prompts and parameters used in the OpenAI API.
- **User Interface:** Develop a graphical user interface (GUI) to make the tool more accessible and user-friendly. e.g. Chrome extension
- **Multi-language Support:** Expand the tool to support multiple programming languages and provide feedback in different languages.

### Conclusion:
The CodeMentor AI project demonstrates the potential of combining artificial intelligence with automation to improve code quality and productivity. By automating the feedback process, it helps programmers receive timely and constructive feedback, ultimately enhancing their coding skills and project outcomes.
