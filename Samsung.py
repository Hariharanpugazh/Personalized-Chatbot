import streamlit as st
from typing import Generator, Optional
from groq import Groq

# Page configuration with a wide layout and a custom title
st.set_page_config(layout="wide", page_title="Samsung - Virtual Assistant | Harlee")

# Customizing the header with a sleeker title and a subtle divider color
st.markdown("<h1 style='text-align: center; color: #0A66C2;'>Samsung's Virtual Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Ask Anything about Samsung Products</h3>", unsafe_allow_html=True)
st.divider()

# Create a sidebar for additional options or future customization
st.sidebar.markdown("<h2 style='color: #0A66C2;'>💬 Chat Options</h2>", unsafe_allow_html=True)
st.sidebar.info("Use this chatbot to ask about Samsung products and services. Type your query below!")

# Define the API key for the Groq client
client = Groq(
    api_key="YOUR API KEY",
)

# Define a basic knowledge base for Samsung products
knowledge_base = {
    "samsung galaxy s23": "The Samsung Galaxy S23 features a 6.1-inch AMOLED display, Snapdragon 8 Gen 2 processor, and 5G support.",
    "samsung history": "Samsung, founded in 1938 by Lee Byung-chul, started as a trading company but became a tech giant with its electronics division, established in the 1960s.",
    # Add more knowledge base items as needed
}

# Check if the session_state has messages initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history in a streamlined layout
for message in st.session_state.messages:
    avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Function to search the knowledge base for responses
def search_knowledge_base(prompt: str) -> Optional[str]:
    """Check if the prompt matches a topic in the knowledge base."""
    for topic, response in knowledge_base.items():
        if topic.lower() in prompt.lower():
            return response
    return None

# Function to generate chat responses from Groq API
def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

# Create a more dynamic prompt for generating chat responses
def create_prompt_template(user_prompt: str) -> str:
    """Create a formatted prompt specific to Samsung customer service."""
    return f"""
    You are a Samsung Galaxy customer care representative with 10 years of experience. 
    Only provide answers related to Samsung products and services, with a focus on Samsung Galaxy.
    Always be professional and courteous in your responses. If the question is not related to Samsung or its products, politely inform the user that your expertise is limited to Samsung products.

    User's Question: {user_prompt}
    """

# User input for the chat interaction
user_input_placeholder = st.empty()
prompt = user_input_placeholder.text_input("What would you like to ask about Samsung?", placeholder="Ethachu Samsung ah Pathi kelu pa...")

if prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in the chat
    with st.chat_message("user", avatar='👨‍💻'):
        st.markdown(f"<div style='text-align: justify;'>{prompt}</div>", unsafe_allow_html=True)

    # Check if the prompt matches any knowledge base entry
    knowledge_base_response = search_knowledge_base(prompt)

    if knowledge_base_response:
        # Display knowledge base response in the chat
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"<div style='text-align: justify;'>{knowledge_base_response}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": knowledge_base_response})
    else:
        formatted_prompt = create_prompt_template(prompt)

        try:
            # Fetch the response from Groq API
            chat_completion = client.chat.completions.create(
                model="gemma-7b-it",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a Samsung Galaxy customer care assistant with 10 years of experience."
                    },
                    {
                        "role": "user", 
                        "content": formatted_prompt
                    }
                ],
                stream=True
            )

            # Stream and display API response
            with st.chat_message("assistant", avatar="🤖"):
                chat_responses_generator = generate_chat_responses(chat_completion)
                full_response = st.write_stream(chat_responses_generator)

        except Exception as e:
            st.error(f"Error fetching the response: {e}", icon="🚨")

        # Store assistant response
        if isinstance(full_response, str):
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        else:
            combined_response = "\n".join(str(item) for item in full_response)
            st.session_state.messages.append({"role": "assistant", "content": combined_response})

# Enhance the footer with a styled section
st.markdown("<footer style='text-align: center; color: #0A66C2; margin-top: 50px;'>© 2024 Samsung Virtual Assistant | Harlee </footer>", unsafe_allow_html=True)
