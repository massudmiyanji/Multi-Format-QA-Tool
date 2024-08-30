import logging
import pathlib
from typing import Any
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredEPubLoader,
    UnstructuredWordDocumentLoader,
)
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document


def initialize_cache(output_key: str):
    """Initialize the cache for contextual conversation."""
    return ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True,
        output_key='answer'
    )





class EpubReader(UnstructuredEPubLoader):
    def __init__(self, file_path: str | list[str], **unstructured_kwargs: Any):
        super().__init__(file_path, **unstructured_kwargs, mode="elements", strategy="fast")








class FileProcessor(object):
    """Loads in a file with a supported extension."""
    supported_extensions = {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".epub": EpubReader,
        ".docx": UnstructuredWordDocumentLoader,
        ".doc": UnstructuredWordDocumentLoader
    }





class FileLoaderException(Exception):
    pass


def process_file(temp_filepath: str) -> list[Document]:
    """Load a file and return it as a list of documents."""
    ext = pathlib.Path(temp_filepath).suffix
    loader = FileProcessor.supported_extensions.get(ext)
    if not loader:
        raise FileLoaderException(
            f"Invalid extension type {ext}, cannot load this type of file"
        )

    loaded = loader(temp_filepath)
    docs = loaded.load()
    logging.info(docs)
    return docs