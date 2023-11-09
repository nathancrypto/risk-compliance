import sqlite3
import openai

openai.api_key = "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"


def openai_task(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": question}
        ]
    )
    return response["choices"][0]["message"]["content"]


def add_idea(idea, table):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {table} VALUES('{idea}')")
    connection.commit()
    cursor.close()
    connection.close()


def fetch_ideas(table):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    data_items = cursor.execute(f"SELECT idea FROM {table}")
    items_tuple = data_items.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return items_tuple


def generate_initial_10():
    initial_ideas = fetch_ideas("Initial_ideas")
    question = f"I want you to merge any duplicate suggestions and create a top 10 unique areas from {initial_ideas}.output just the output as a python string seperated by '\n'"
    output = openai_task(question)
    ideas = output.split("\n")
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    for i in ideas:
        cursor.execute(f"INSERT INTO 'Initial_10_Ideas' VALUES('{i}',0)")
    connection.commit()
    cursor.close()
    connection.close()


def ideas_radio(table):
    ideas = fetch_ideas(table)
    radio = []
    for i in ideas:
        radio.append((i[0], i[0]))
    return radio


def update_vote(vote):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    total_vote = cursor.execute(f"SELECT vote FROM Initial_10_Ideas WHERE idea='{vote}'")
    num = total_vote.fetchone()
    new_num = num[0] + 1
    cursor.execute(f"UPDATE Initial_10_Ideas SET vote = {new_num} WHERE idea='{vote}'")
    connection.commit()
    cursor.close()
    connection.close()


def voting_calculator():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    data = cursor.execute("SELECT idea, vote FROM Initial_10_Ideas ORDER BY vote")
    votes = data.fetchall()
    top_4 = [votes[9][0], votes[8][0], votes[7][0], votes[6][0]]
    for i in top_4:
        cursor.execute(f"INSERT INTO Top_4_Ideas VALUES('{i}')")
    connection.commit()
    cursor.close()
    connection.close()

def generate_developed_5():
    ideas=fetch_ideas("Developed_Ideas")
    question = f"I want you to merge any duplicate suggestions and create a top 5 unique areas from {ideas}.output just the output as a python string seperated by '\n'"
    output =openai_task(question)
    developed_5=output.split("\n")
    for i in developed_5:
        add_idea(i,"Developed_5_Ideas")

def generate_ideas(name):
    file= open(f"{name}.txt")
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    for i in file:
        i = i.replace("\n","")
        cursor.execute(f"INSERT INTO {name} VALUES('{i}')")
    connection.commit()
    cursor.close()
    connection.close()
    file.close()