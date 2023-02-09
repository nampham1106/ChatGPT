import openai
import gradio as gr
import time

openai.api_key = "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"

start_squence = "\nAI"
restart_human = "\nHuman"

prompt = "What is research?"


def openai_create(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
    except openai.error.RateLimitError:
        print("Openai RateLimitError is handled!")

    return response.choices[0].text



def chatGPT(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>your own chatGPT</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatGPT, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True)