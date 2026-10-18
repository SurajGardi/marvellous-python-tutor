import streamlit as st
from ollama import chat


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Marvellous Python Tutor",
    page_icon="🐍",
    layout="centered"
)


# ============================================================
# Custom CSS - Mobile Friendly
# ============================================================

st.markdown(
    """
    <style>

    /* Main container */
    .main {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* Header */
    .title {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #888;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }

    /* Mobile optimization */
    @media (max-width: 600px) {

        .title {
            font-size: 1.6rem;
        }

        .subtitle {
            font-size: 0.8rem;
        }

        .main {
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="title">🐍 Marvellous Python Tutor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Powered by Ollama • Llama 3.2</div>',
    unsafe_allow_html=True
)


# ============================================================
# Initialize Chat History
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a Python programming teacher"
        }
    ]


# ============================================================
# Display Chat History
# ============================================================

for message in st.session_state.messages:

    # Don't display system message
    if message["role"] == "system":
        continue

    if message["role"] == "user":

        with st.chat_message("user"):
            st.markdown(message["content"])

    elif message["role"] == "assistant":

        with st.chat_message("assistant"):
            st.markdown(message["content"])


# ============================================================
# User Input
# ============================================================

question = st.chat_input(
    "Ask me anything about Python..."
)


# ============================================================
# LLM Processing
# ============================================================

if question:

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Add user message to conversation
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:

        # Get Ollama response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = chat(
                    model="llama3.2:1b",
                    messages=st.session_state.messages
                )

                answer = response.message.content

                st.markdown(answer)

        # Add AI response to conversation
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as error:

        st.error(
            f"Unable to connect to Ollama.\n\n"
            f"Error: {error}"
        )