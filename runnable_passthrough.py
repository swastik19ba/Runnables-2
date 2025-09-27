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

joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassThrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'cricket'})) 