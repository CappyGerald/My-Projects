from textwrap import dedent

# welcoming the player

greeting = dedent("""
                      Hello player. Welcome to Guessing Game, an interractive game that allows you to pick a topic and then answer questions that follow. Have fun!
                    """)
                    
print(greeting)     

# topic options for players to select
                            
topics = [
             "History", "Python", "Geography"
]


python_option = {
              "questions": [     "Who developed the Python programming language?",
    "Which type of programming does Python support?",
    "Is Python case-sensitive when dealing with identifiers?",
    "What is the correct extension for Python files?",
    "Is Python code compiled or interpreted?",
    "What are all the keywords in Python written in?",
    "What will be the output of 4 + 3 % 5?",
    "Which keyword is used for defining a block of code in Python?",
    "Which function is used for creating anonymous functions at runtime?",
    "What does 'pip' stand for in Python?"

  ], 
              "answers": [
                 
      "Guido van Rossum",
    "All of the mentioned",
    "Yes",
    ".py",
    "Python code is both compiled and interpreted",
    "Capitalized",
    "7",
    "Indentation",
    "lambda",
    "Pip Installs Packages"
]}
history_option = {
              "question's": [   
              
    "As recently dramatized in a critically acclaimed miniseries, what year did the Chernobyl disaster occur?",
    "Who was Lord Mayor of London four times between 1397 and 1419 and the inspiration for a classic English folk tale?",
    "Who was the second President of the United States?",
    "Which British archaeologist discovered Tutankhamun's tomb?",
    "Who was the leader of Britain's ill-fated Antarctic expedition that was one of the first to reach the South Pole in 1912?",
    "In which European country was there a civil war between 1946 and 1949?",
    "Which 13th-century Scottish knight did Mel Gibson portray in 'Braveheart'?",
    "Which war was fought in South Africa between 1899 and 1902?",
    "In which country did the Second World War Battles of El Alamein take place?",
    "Who discovered the wreckage of the Titanic?"
                  
                      ], 
              "answers": [
              
              
              "1986",
    "Richard (Dick) Whittington",
    "John Adams",
    "Howard Carter",
    "Robert Falcon Scott",
    "Greece",
    "William Wallace",
    "Anglo-Boer War",
    "Egypt",
    "Robert Ballard"
]}

geography_option = {
             "questions": [
             "What is the only country that borders the    United Kingdom?",
    "Ninety percent of the Earth's population lives in which hemisphere?",
    "In which country would you find the city of Dresden?",
    "What would you call someone from Sudan?",
    "What are the names of South Africa's three capital cities?",
    "How many large islands make up Hawaii?",
    "In which U.S. state can the world's tallest trees be found?",
    "What is the name of the highest uninterrupted waterfall in the world?",
    "Which river flows through the Grand Canyon?",
    "What is the largest ocean in the world?"
             
             ], 
              "answers": [
             " Ireland",
    "The Northern Hemisphere",
    "Germany",
    "Sudanese",
    "Cape Town, Pretoria, and Bloemfontein",
    "Eight",
    "California",
    "Angel Falls",
    "Colorado River",
    "Pacific Ocean"
]}



# validating the topic selected by player
def select_topic():
    user_topic = input(f"Please select a topic from the following: {topics}").capitalize()
    
    if user_topic in topics:
        print(f"You've selected {user_topic}")
        return user_topic
    else:
        print(f"Invalid! Please select a topic from the following: {topics}")
        return select_topic()
        
        
# we want to present the questions to the user one by one giving them an opportunity to answer each one by one

def ask_questions(topic):
    score = 0
    for i, question in enumerate(topic["questions"], start=1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == topic["answers"][i - 1].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The answer is: {topic['answers'][i - 1]}\n")

    print(f"Your final score: {score}/{len(topic['questions'])}")


# Let's use these functions to run the game.
selected_topic = select_topic()

if selected_topic == "Python":
    ask_questions(python_option)
elif selected_topic == "History":
    ask_questions(history_option)
elif selected_topic == "Geography":
    ask_questions(geography_option)
