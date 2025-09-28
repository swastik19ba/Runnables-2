from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassThrough,RunnableLambda,RunnableParallel,RunnableBranch

load_dotenv()

prompt1=PromptTemplate(
    template='wtite a  detailed report on topic',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['topic']
)
report_gen_chain=RunnableSequence(prompt1,model,parser)
branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequnece(prompt2,model,parser)), #works when this condition is true
    RunnablePassThrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))

