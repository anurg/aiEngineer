from openai import OpenAI
from dotenv import load_dotenv
from system_prompt import SYSTEM_PROMPT
import sys

load_dotenv()
try:
    client = OpenAI()
except Exception as e:
    print(f"Error in OpenAI client {e}")
    sys.exit(1)


def main():
    messages = [
                {
                    "role":"system",
                    "content":SYSTEM_PROMPT
                }
            ]
    print("-"*50)
    print("TaskBuddy: Hey! What's on your mind today?")
    print("          Dump Your tasks here, and I'll organise them for you!")
    print("-"*50)

    while True:
        try:
            user_input = input(f"\n You:").strip()
            print(user_input)
            if user_input.lower() in ["quit","exit","bye","done","finished"]:
                print(f"\nTaskBuddy: Good Bye!")
                break
            if not user_input.strip():
                continue
            messages.append({
                    "role":"user",
                    "content":user_input
                    })
            response = client.chat.completions.create(
                model="gpt-5.4-mini",
                messages=messages
            )
            reply = response.choices[0].message.content
            print(f"\n {reply}")
        except KeyboardInterrupt as e:
            print(f"TaskBuddy: GoodBye!")
            break
        except Exception as e:
            print(f"An Error occurred-{e}!")
            break
        
if __name__=="__main__":
    main()

    


