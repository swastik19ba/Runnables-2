from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1=PromptTemplate(
    template='wtite a  joke on a topic',
    input_variables=['topic']
)

model=ChatOpenAI()

prompt2=PromptTemplate(
    template='explain the following joke',
    input_variables=['topic']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))