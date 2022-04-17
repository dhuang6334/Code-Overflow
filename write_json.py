import json

if __name__ == "__main__":
    with open("questions2.json", "w") as file:
        json_object = {"math":[], "english":[], "science":[], "history":[]}
        while True:
            user_subject = input("What subject: ")
            if (user_subject == "done"):
                break
            run2 = True
            while True:
                user_question = input("Question: ")
                if(user_question == "done"):
                    break
                user_answer = input("Answer: ")
                json_object[user_subject].append([user_question, user_answer])
                while True:
                    user_wrong = input("Wrong: ")
                    if (user_wrong == "done"):
                        break
                    json_object[user_subject][-1].append(user_wrong)
        json.dump(json_object, file)

