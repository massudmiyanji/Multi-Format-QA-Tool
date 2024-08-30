"""Document loading functionality.

Run like this:
> PYTHONPATH=. streamlit run chat_with_retrieval/app.py
"""
import logging

import streamlit as st
from streamlit.external.langchain import StreamlitCallbackHandler

from chain import costum_retrieval_chain,memory_instance
from main import initialize_cache, FileProcessor

#logging.basicConfig(encoding="utf-8", level=logging.INFO)
#LOGGER = logging.getLogger()

st.set_page_config(page_title="LangChain: Chat with Documents", page_icon="🦜")
st.title("🦜 LangChain: Chat with Documents")


uploaded_files = st.sidebar.file_uploader(
    label="Upload files",
    type=list(FileProcessor.supported_extensions.keys()),
    accept_multiple_files=True
)
if not uploaded_files:
    st.info("Please upload documents to continue.")
    st.stop()

# use compression by default:
#use_compression = st.checkbox("compression", value=False)
#use_flare = st.checkbox("flare", value=True)
#use_moderation = st.checkbox("moderation", value=False)

CONV_CHAIN = costum_retrieval_chain(
    uploaded_files,
    use_compression=False,
    use_flare=True,
    use_moderation=False
)

if st.sidebar.button("Clear message history"):
    memory_instance.chat_memory.clear()

avatars = {"human": "user", "ai": "assistant"}

if len(memory_instance.chat_memory.messages) == 0:
    st.chat_message("assistant").markdown("Ask me anything!")

for msg in memory_instance.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)
assistant = st.chat_message("assistant")
if user_query := st.chat_input(placeholder="Give me 3 keywords for what you have right now"):
    st.chat_message("user").write(user_query)
    container = st.empty()
    stream_handler = StreamlitCallbackHandler(container)

    # Define params based on use_flare condition
    #if use_flare:
       # params = {
            #"user_input": user_query,  # For FlareChain
       # }
   # else:
        #params = {
              # For ConversationalRetrievalChain
           # "chat_history": memory_instance.chat_memory.messages,
           # "question": user_query
       # }

    # Debugging: Print params to verify
    #st.write("Params:", params)

    # Run the conversation chain with the provided parameters
    try:
        response = CONV_CHAIN.run({"question": user_query}, callbacks=[stream_handler])
        
        # Display the response from the chatbot
        if response:
            container.markdown(response)
    except ValueError as e:
        st.error(f"Error: {e}")
