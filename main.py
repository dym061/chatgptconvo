import openai as oai
import os
import pickle

from data import Files

class ChatToGPT:
    def __init__(self):
        self.messages = [] #will store previous messagaes
        self.engine = "gpt-3.5-turbo" #model
        self.apikey = Files.apikeyfile #the file that contains your openai api key
        
    def load_conversations(self):
        if os.path.exists(Files.convos):
            print("preloading conversations...")
            with open(Files.convos, 'rb') as f:
                self.messages = pickle.load(f)
                
                for message in self.messages:
                    for key, value in message.items():
                        print(value) 
                        
                    print("=================")

    def save_conversation(self,obj):
        with open(Files.convos, 'wb') as outp:
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)                    

    def get_response(self,user_text):
        self.messages += [{"role": "user", "content": user_text }]
        oai.api_key_path = self.apikey
        response = oai.ChatCompletion.create(model=self.engine,messages=self.messages)    
        
        output_text = response['choices'][0]['message']['content']
        self.messages += [{"role": "assistant", "content": output_text }]
        
        self.save_conversation(self.messages)
        
        return output_text  

if __name__ == '__main__':

    chatGPT = ChatToGPT() #initiate class
    chatGPT.load_conversations() #load any previous conversations
    
    prompt = input(">>\n")
    while prompt != "exit()":
        print(chatGPT.get_response(prompt))
        prompt = input(">>\n")