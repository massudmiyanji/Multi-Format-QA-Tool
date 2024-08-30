
![Untitled Diagram (1)](https://github.com/user-attachments/assets/bb57b31c-c08c-4c3a-b942-18e0500bfb79)













# Multi-Format QA Tool

This application is designed to interact with users by answering questions based on information retrieved from various document formats. The tool uses advanced natural language processing (NLP) techniques, embeddings, and retrieval mechanisms to provide accurate and relevant responses. It is built using the LangChain library, which supports conversational AI and document processing.

## Features

- **Multi-Format Document Support**: Upload various file types to extract and retrieve information.
- **Conversational Interface**: Engage in a conversation with the AI to ask questions about the uploaded documents.
- **Customizable Retrieval**: Supports different retrieval methods, including contextual compression for efficient querying.
- **Memory Management**: Keeps track of conversation history for context-aware responses.
- **Moderation Options**: Optional integration with OpenAI moderation tools to ensure safe interactions.

## How to Use

1. **Install Dependencies**: Make sure you have Python installed. Then, install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application**: Start the application using the following command:
    ```bash
    PYTHONPATH=. streamlit run app.py
    ```

3. **Upload Files**: Use the sidebar to upload documents. Supported file formats are defined in the `FileProcessor.supported_extensions`.

4. **Ask Questions**: Interact with the chatbot interface. Type your questions into the chat, and the AI will respond with information retrieved from the uploaded documents.

5. **Clear History**: Use the sidebar option to clear the conversation history if needed.

## Configuration

- The application uses environment variables to configure the OpenAI API. Ensure that you have a `.env` file with your API keys.
- The retrieval process can be customized to use compression techniques and moderation chains.

## Dependencies

- **LangChain**: Core library for building conversational AI applications.
- **OpenAI**: Provides the language models and embeddings.
- **Streamlit**: Web interface for interacting with the chatbot.

## Example Usage

- After launching the app, upload a `.pdf` or `.docx` file.
- Ask the application specific questions about the content of the document.
- Receive answers based on the document's content, using embeddings to ensure relevance.

## Future Improvements

- Support for more file formats.
- Enhanced moderation features for safer interactions.
- Additional configuration options for retrieval settings.

## License

This project is licensed under the MIT License.

## Contact

For questions or collaboration opportunities, feel free to reach out.

