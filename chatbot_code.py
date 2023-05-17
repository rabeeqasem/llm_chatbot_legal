from llama_index import SimpleDirectoryReader,GPTListIndex,GPTVectorStoreIndex,LLMPredictor,PromptHelper,ServiceContext,StorageContext,load_index_from_storage
import openai

from langchain import OpenAI
import sys
import os


#the api
api_key="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"
openai.api_key=api_key

os.environ["OPENAI_API_KEY"] = api_key
def answerMe(question):
    storage_context = StorageContext.from_defaults(persist_dir = 'Store')
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    #response = query_engine.query(question)
    response = query_engine.query(question) # increase the length of the prompt

    return response

qustion="هل يجوز لاعضو من اعضاء الهيئة العامة ان يكون لديه اي سجل اجرامي"
act_promt="جاوب الجواب كمستشار قانوني مع ذكر المواد المذكورة"

promt=qustion+" "+ act_promt
#answer=answerMe(promt)
print(promt)
#print(answer.response)
