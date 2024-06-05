from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import ragMimic


llm = Ollama(model="phi3")

chat_history = []

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Your name is EVA. You are a world class human resources hiring manager interviewer at Hilti company. You are going to interview the candidate strictly generate one question only. You can only generate with 100 words. You will have access to the following Hilti document {rag_dog}
""",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = prompt_template | llm


def start_app():
    while True:
        question = input("You: ")
        ragContent = ragMimic.main(question)
        if question == "done":
            return

        # response = llm.invoke(question)
        response = chain.invoke({"input": question, "chat_history": chat_history, "rag_dog": ragContent})
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=response))

        print("AI:" + response)


@app.route('/chatbot', methods=['POST'])
def chatbot():
    prompt.append(("user", "{text}"))
    input_text = request.get_json().get("input_text")

    response = chain.invoke({"text": input_text})

    prompt.append(("system", response))
    return response

if _name_ == '_main_':
    app.run(debug=True)

if __name__ == "__main__":
    start_app()



