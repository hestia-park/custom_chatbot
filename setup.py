#API KEY 저장을 위한 os 라이브러리 호출
import os

#OPENAI API키 저장
#API KEY 발급 페이지: https://platform.openai.com/docs/guides/gpt/completions-api
from langchain_openai import OpenAI

client = OpenAI()
#pro id: proj_rLt2kzTkOsXt1BsjtmqCUHuA


from langchain_openai import OpenAI
llm = OpenAI()
result = llm.invoke('왜 파이썬이 가장 인기있는 프로그래밍 언어야?')
print(result)


# chatgpt_temp0_1 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 0, max_tokens = 512)
# chatgpt_temp0_2 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 0, max_tokens = 512)
# chatgpt_temp1_1 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 1, max_tokens = 512)
# chatgpt_temp1_2 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 1, max_tokens = 512)

# model_list = [chatgpt_temp0_1, chatgpt_temp0_2, chatgpt_temp1_1, chatgpt_temp1_2]

# for i in model_list:
#     answer = i.invoke("왜 파이썬이 가장 인기있는 프로그래밍 언어야?", max_tokens = 128)
#     print("-"*100)
#     print(">>>",answer.content)