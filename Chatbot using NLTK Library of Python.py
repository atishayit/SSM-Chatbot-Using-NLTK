import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello|hola",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a chatbot created by Atishay Jain, You can call me Jarvis!",]
    ],
    [
        r"how are you?",
        ["I'm doing great! \nWhat about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind","No Problem!","Not an Issue",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a program. \nI have no age, I am immortal!",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Atishay created me using NLTK library present in Python","Its a Top Secret, you know ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Noida, Uttar Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is just awesome","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an exceptional company, I have heard about it.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["Come on dude!. I am a program, I'm always healthy :)",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket, especially Virat Kohli.",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Virat Kohli","Rohit Sharma","Steve Smith"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Andrew Lincoln"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Well, check Coursera or Udemy, they have a lot of courses from exceptional firms to offer!"]
    ],
    [
        r"quit",
        ["Bye! Take Care. See you soon :) ","It was nice talking to you. See you soon :)","Have a nice day, Bye!"]
    ],
    [
        r"bye|exit",
        ["Please type quit to exit the chatbot!"]
    ],
]
                
def chat():
    print("Hi! I am a chatbot created by Atishay Jain and I am at your service!")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()