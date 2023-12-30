#!/usr/bin/env python3

import os
from openai import OpenAI
import gradio

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

messages = [{"role": "system", "content": "You are a personal fitness trainer specializing in health and wellness."}]

def CustomFitnessAssistant(user_input):
    messages.append({"role": "user", "content": user_input})
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    
    fitness_assistant_reply = chat_completion["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": fitness_assistant_reply})
    
    return fitness_assistant_reply

demo = gradio.Interface(fn=CustomFitnessAssistant, inputs="text", outputs="text", title="Fitness Trainer AI")

demo.launch(share=True)

