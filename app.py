import os
import sys
from dotenv import load_dotenv
import warnings

from langchain_community.vendorstores import Chroma
from flask import Flask, render_template, jsonify, request
from langchain.memroy import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnablePassthrough
from lanchain.schema import StrOutputParser

from src.logger import logging
from src import constants
from src.helper import repo_ingestion, load_embeddings_model, get_prompt, format_docs

load_dotenv()
warnings.filterwarnings("ignore")
logger = logging.getLogger("App")
embeddings = load_embeddings_model()
persist_directory = constants.VECTOR_DB_DATA_PATH
app = Flask(__name__)
