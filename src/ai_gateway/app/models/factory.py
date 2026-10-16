from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

def build_model(persona):
    temperature =  persona['model']['temperature']
    deployment_name = persona['model']['deployment_name']
    logging.info(f"loaded deployment model {deployment_name}")
    return AzureChatOpenAI(
        azure_deployment= deployment_name
    )

    

