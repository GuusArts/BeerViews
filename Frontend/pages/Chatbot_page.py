import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import AIMessage, HumanMessage


# Transform to prompt adds all the known info from the info variable to a string which will be used in the prompt for the NLP-model
def transform_to_prompt(info):
    return f"The name of the beer is: {info['name']}, The style of the beer is {info['style']}. The beer is from the brewery {info['brewery']}. The abv of this beer is {info['abv']}. The average score is {info['average score']}, the aroma's average score is {info['average score aroma']}, the appearance's average score is {info['average score appearance']}, the palate's average score is {info['average score palate']}, the taste's average score is {info['average score taste']}."


# Streamlit application having a NLP-model

# Imports the model
model = Ollama(model="llama3")

# Sets the title of the page
st.header(f'{st.session_state.beer['name']} expert')

# Initialize conversation memory
if "conversation_chain" not in st.session_state:
    st.session_state.conversation_chain = ConversationChain(
        llm=model,
        memory=ConversationBufferMemory()
    )

# There should be no messages when none have been asked
if "messages" not in st.session_state:
    st.session_state.messages = []

if "beer_initialized" not in st.session_state:
    st.session_state.beer_initialized = False

# When something has been selected
if st.session_state.beer and st.session_state.beer_initialized is not st.session_state.beer:
    beer_info = st.session_state.beer

    if beer_info:
        st.session_state.messages = []
        st.session_state.conversation_chain.memory.clear()  # Clear previous memory

        initial_message = f'Please ask me questions about the beer {beer_info["name"]}.'
        st.session_state.conversation_chain.memory.chat_memory.add_message(AIMessage(content=initial_message))
        st.session_state.messages.append({"role": "assistant",
                                          "content": initial_message})
        st.session_state.beer_initialized = st.session_state.beer
    else:
        st.title('Beer not known')

# Make sure the messages are clearly shown after they have been asked
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# When a question is asked
if question := st.chat_input('Type here!'):
    # Sets up question
    with st.chat_message('user'):
        st.markdown(question)
    st.session_state.conversation_chain.memory.chat_memory.add_message(HumanMessage(question))
    st.session_state.messages.append({"role": "user",
                                      "content": question})

    try:
        # Initialises variable for the prompt
        beer_name = st.session_state.beer['name']
        info_string = transform_to_prompt(st.session_state.beer)

        # Create the prompt
        prompt_template: str = """/
        You are a beer expert which only know about the beer: {beer_name}. You are going to answer every question of the user as an expert about this beer. You are going to use this discription: {info}. With this information answer this question: {question}.
        """
        prompt = PromptTemplate.from_template(template=prompt_template)

        # Format the prompt to add variable values
        prompt_formatted_str: str = prompt.format(question=question,    
                                                  beer_name=beer_name,
                                                  info=info_string)

        # Get response from the conversation chain
        response = st.session_state.conversation_chain.run(input=prompt_formatted_str)

        # Ensure response is a string
        if isinstance(response, list):
            response = "".join(response)

        # Sets up response
        with st.chat_message('assistant'):
            st.markdown(response)
        st.session_state.conversation_chain.memory.chat_memory.add_message(AIMessage(response))
        st.session_state.messages.append({"role": "assistant",
                                          "content": response})
    except:
        # Error
        st.title('Please pick a beer first.')  