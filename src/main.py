import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a personal fitness trainer specializing in health and wellness."}]

def CustomFitnessAssistant(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    fitness_assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": fitness_assistant_reply})
    return fitness_assistant_reply

demo = gradio.Interface(fn=CustomFitnessAssistant, inputs="text", outputs="text", title="Fitness Trainer AI")

demo.launch(share=True)

