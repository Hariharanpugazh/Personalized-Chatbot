# Personalized Chatbot

A personalized chatbot designed to answer queries related to a specific company's products and services, using a predefined knowledge base and an API for text generation. This chatbot offers accurate, company-specific responses based on official data sources.

## Features

- **Company-Specific Responses**: The chatbot provides information solely related to the selected company, ensuring accurate and relevant responses.
- **API Integration**: Uses a text generation API to dynamically respond to user queries.
- **Knowledge Base-Driven**: Fetches data from a predefined knowledge base to improve response quality.
- **Customizable**: Easily adaptable to any company with an adjustable knowledge base and API configuration.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Text Generation API**: Gemini (or Groq for Samsung chatbot)
- **Knowledge Base**: Custom knowledge base (e.g., Samsung)
- **Version Control**: Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Hariharanpugazh/Personalized-Chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Personalized-Chatbot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up your API keys in the environment variables for text generation.
2. Modify the knowledge base file to reflect the company's specific data.
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Configuration

- **Knowledge Base**: Modify the `knowledge_base.json` file with the company-specific data.
- **API Keys**: Update your API keys in the `.env` file or configure them in your environment.

## Contributing

Feel free to open issues or submit pull requests if you want to contribute to this project. Make sure to follow the contribution guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information, feel free to contact me:

- GitHub: [Hariharanpugazh](https://github.com/Hariharanpugazh)
- Email: [Hariharanpugazh](hariharanpugazh@gmail.com)

---

Let me know if you'd like to add any specific sections or images, and I can refine the `README` further!
