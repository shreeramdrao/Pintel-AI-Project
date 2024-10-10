import requests
from bs4 import BeautifulSoup
import re
import spacy

# Step 1: Crawl the page and extract HTML
url = "https://www.sec.gov/Archives/edgar/data/200406/000020040624000013/jnj-20231231.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Clean the text by removing HTML tags and unnecessary content
def clean_text(text):
    # Remove extra spaces and newlines
    clean = re.sub(r'\s+', ' ', text)
    return clean.strip()

# Step 3: Extract sections and subsections
def extract_sections(soup):
    sections = []
    section_headers = soup.find_all(['h2', 'h3'])  # Assuming h2/h3 tags mark sections/subsections
    for header in section_headers:
        section = {}
        section_name = header.get_text(strip=True).lower()
        next_sibling = header.find_next_sibling()

        # Check if there is a subsection or direct content
        if next_sibling and next_sibling.name == 'h3':
            sub_section_name = next_sibling.get_text(strip=True).lower()
            content = clean_text(next_sibling.find_next_sibling().get_text())
        else:
            sub_section_name = ''
            content = clean_text(header.find_next_sibling().get_text())

        section["section_name"] = section_name
        section["sub_section_name"] = sub_section_name
        section["content"] = content
        sections.append(section)

    return sections

# Step 4: Get the structured data
data = extract_sections(soup)

# Print the output (list of dictionaries)
for entry in data:
    print(entry)

# Step 5: Select a section (for example 'risk') and analyze using traditional NLP
risk_section = [entry for entry in data if 'risk' in entry['section_name']]

# Use spaCy for phrase extraction and risk analysis
nlp = spacy.load("en_core_web_sm")

def extract_risks(content):
    doc = nlp(content)
    risks = []
    
    # Find named entities and noun phrases that could represent risks
    for ent in doc.ents:
        if ent.label_ in ["ORG", "NORP", "FAC", "EVENT", "GPE"]:  # Common labels that might relate to risks
            risks.append(ent.text)
    
    return risks

# Analyze the risks
for entry in risk_section:
    risks = extract_risks(entry['content'])
    print(f"Risks for section {entry['section_name']}: {risks}")

# Step 6: Extract important phrases (noun chunks)
def extract_phrases(text):
    doc = nlp(text)
    return [chunk.text for chunk in doc.noun_chunks]

for entry in risk_section:
    phrases = extract_phrases(entry['content'])
    print(f"Important phrases for section {entry['section_name']}: {phrases}")