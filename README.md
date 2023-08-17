# Spaced Repetition Study Tool with GPT

## Description

This project is a Spaced Repetition Study Tool that utilizes the state-of-the-art GPT (Generative Pre-trained Transformer) language model. The main purpose of the tool is to aid in efficient learning by serving questions to the user based on the spaced repetition algorithm.

The tool is designed to pose questions to the user, verify their answers using the GPT model, and then, depending on the user's self-assessed understanding of the question (easy, medium, hard), set the next review time for that question.

Additional functionality includes a conversation box, where users can interact freely with the GPT model.

## Features

- **MongoDB Atlas Integration:** MongoDB Atlas, a fully-managed cloud database available in AWS, Azure, and Google Cloud, is used to store the study questions, answers, next review times, and difficulties.
- **Spaced Repetition Algorithm:** The system uses a spaced repetition algorithm to calculate the next review time for a question. This algorithm is based on the user's self-assessed difficulty of the question.
- **GPT Integration:** The system uses OpenAI's GPT model to verify user's answers, provide feedback, and facilitate free chat sessions.
- **Streamlit UI:** The tool uses Streamlit to provide a simple and intuitive user interface for interaction with the study system.

## Usage

To use the system, you need to have a set of questions you want to study. The system will then serve these questions to you in an order determined by the spaced repetition algorithm. After answering a question, you will be asked to assess the difficulty of the question, which will determine the next review time for that question.

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your_username/StudyGPT.git

2. Install the requirements:
   ```bash
   pip install -r requirements.txt

3. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key_here

4. Run Streamlit app:
  ```bash
  streamlit run app.py



