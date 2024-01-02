from anthropic import AsyncAnthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
import os 
import streamlit as st
import asyncio

load_dotenv()

anthropic = AsyncAnthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv("API_CLAUD"),
)





async def generate_text(x):
    container = st.empty()
    ai_prompt = "You are a professional AI expert. If I ask you question related to math, AI, DS, DL, ML, you can answer them from a professional perspective and give me career interview suggestions. You can choose to search online to get more accurate information.  If you feel that the question I asked may not be so important, or there are other more important questions that I may not understand, you can try to guide me to further understand the relevant technical knowledge."
    text = ""
    stream = await anthropic.completions.create(
        model="claude-2.1",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {x} {AI_PROMPT} {ai_prompt}",
        stream=True,
        temperature=0.9,
    )
    # print(completion.completion)
    async for completion in stream:
        new_char = completion.completion
        text += new_char
        container.text(text)
        asyncio.sleep(0.1)  
        # print(completion.completion, end="", flush=True)

prompt = st.text_input('士桓AI哥在此')


if prompt:
    asyncio.run(generate_text(prompt))