

## Project Overview:
This project crawls and extracts data from an SEC report using Python. The extracted sections are cleaned and stored in a structured format (list of dictionaries). It uses the spaCy library for Natural Language Processing (NLP) to analyze a specific section (e.g., "risk") to extract potential risks and important phrases without relying on any external APIs.

## Project Structure:
- **pintel_ai_task_nlp.py**: The main Python script containing the code for data extraction and risk analysis using spaCy.
- **requirements.txt**: Contains all the dependencies required for the project.
- **README.md**: Instructions for running the project.

## Installation Instructions:
1. Clone the repository or download the zip folder:
    ```bash
    git clone <repo_link> OR download the zip file
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download spaCy's language model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Running the Script:
1. Run the script:
    ```bash
    python pintel_ai_task_nlp.py
    ```

2. Expected Output:
    - The extracted sections and their cleaned content will be printed.
    - The potential risks for the selected section will be printed (using spaCy NER).
    - Important phrases will be extracted from the selected section.

## Notes:
- This solution doesn't require an OpenAI API key or any external service.
- The extracted sections and their content can be further processed as per your specific needs.
