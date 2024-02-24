import openai
import gradio as gr
openai.apikey = "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"
client = openai.Client(api_key=openai.apikey)

class Conversation:
  def __init__(self, prompt):
    self.prompt = prompt
    self.messages = []
    self.messages.append({"role": "system", "content": self.prompt})

  def response_call(self, prompt):
    self.messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=1024,
        messages=self.messages,
        n=1,
        stop=None,
        temperature=0.6,
    )
    message = response.choices[0].message.content
    self.messages.append({"role": "assistant", "content": message})
    return message

#print("hello, I am bayMax. Please talk with me!")

#questions=[]
#answers=[]

#def generator_prompt(prompt, questions, answers):
#  num = len(answers)
#  for i in range(num):
#    prompt += "\n Q:" + questions[i]
#    prompt += "\n A:" + answers[i]
#  prompt += "\n Q:" + questions[num] + "\n A:"
#  return prompt
prompt = """
"""

conv = Conversation(prompt)


def answer(question, history=[]):
  history.append(question)
  response = conv.response_call(question)
  history.append(response)
  responses = [(u,b) for u,b in zip(history[::2], history[1::2])]
  return responses, history

def clear_input(text_input):
    # Clear the input line
    text_input.clear()

with gr.Blocks(css="#chatbot{height:300px} .overflow-y-auto{height:500px}") as demo:
  #while True:
  chatbot = gr.Chatbot(elem_id="chatbot")
  state = gr.State([])
  #user_input = input("> ")
  #questions.append(user_input)
  #if user_input.lower() in ["bye", "goodbye", "exit"]:
  #  print("good bye")
  #  break
  with gr.Column():
    with gr.Row():
      inputtext = gr.Textbox(show_label=False, placeholder= "Enter txt", container=False)
      clear_button = gr.Button("Clear")

  # Connect the clear_input() function to the Button component
  clear_button.click(clear_input, inputs=[inputtext], outputs=[])

  # Clear the input line when the user taps enter
  inputtext.submit(clear_input, inputs=[inputtext], outputs=[])
  inputtext.submit(answer, [inputtext, state], [chatbot, state])
demo.launch()
    #prompt = generator_prompt("", questions, answers)
    #answer = response_call(prompt)
    #print(answer)
    #answers.append(answer)
