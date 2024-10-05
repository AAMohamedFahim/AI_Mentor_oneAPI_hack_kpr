from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


from dotenv import load_dotenv
import os


# load_dotenv()


# groq_api_key=os.environ['GROQ_API_KEY']
groq_api_key="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"




llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="llama-3.1-8b-instant")
def mentor_ai_res(topic,user_id):

        prompt = ChatPromptTemplate.from_template(
         """
         you are a helpfull mentor ai to assist user related to there roadmap
         
         here is the road that user has:
         {flow_txt}
         
         here is the user data : 
         {user_txt}
         
         Kamesh, born on December 12, 2004, is a 19-year-old data engineer. He has completed his 12th grade and is currently studying to become a big data analyst. Despite not having any formal courses or practical projects in Data Engineering, Kamesh is determined to learn and grow in this field.
         
         rule: 
            1. only reply to the question dont tell anything other then that.
            2. your reply should be short as much as possible.
         
         based on this data reply to this question:
         {input}.
 """)

        print(user_id)

        file_name_about = user_id+"_about"
        with open(file_name_about, 'r') as file:
            user_txt = file.read()
        file_name_flows = user_id+"_flows"
        with open(file_name_flows, 'r') as file:
            flow_txt = file.read()
        
        llm_chain = LLMChain(
                llm=llm,
                prompt=prompt)

        response =llm_chain.invoke({"input":topic,"user_txt":user_txt,"flow_txt":flow_txt})
        return response['text']

# topic="give me the roadmap for python" 
# print(response(topic))
           
                        
            
    
 
 


      