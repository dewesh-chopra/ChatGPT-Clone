from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://deweshchopra:sUlBW0jV3bEzf6ef@cluster0.xovt6s4.mongodb.net/chatgpt"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html", mychats=mychats)

@app.route("/api", methods=["GET", "POST"])
def qna():
    data = {"answer": "It looks like you entered a random string of characters. If there's something specific you would like to discuss or any questions you have, feel free to let me know, and I'll be happy to help!"}

    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"answer": chat['answer']}
            return jsonify(data)
        else:
            # Code for da-vinci-003, GPT 3

            # response = openai.Completion.create(
            #     model="text-davinci-003",
            #     prompt="",
            #     temperature=0.7,
            #     max_tokens=256,
            #     top_p=1,
            #     frequency_penalty=0,
            #     presence_penalty=0
            # )
            # print(response)
            # data = {"question": question, "answer": response['choices'][0]['text']}
            # mongo.db.chats.insert_one({"question": question, "answer": response['choices'][0]['text']})

            # Code for gpt-3.5-turbo, GPT 3.5

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            data = {"question": question, "answer": response['choices'][0]['message']['content']}
            mongo.db.chats.insert_one({"question": question, "answer": response['choices'][0]['message']['content']})
            
            # mongo.db.chats.insert_one({"question": question, "answer": "It looks like you entered a random string of characters. If there's something specific you would like to discuss or any questions you have, feel free to let me know, and I'll be happy to help!"})

            # data = {"answer": "It looks like you entered a random string of characters. If there's something specific you would like to discuss or any questions you have, feel free to let me know, and I'll be happy to help!"}
            
            return jsonify(data)

    return jsonify(data)

app.run(debug=True)