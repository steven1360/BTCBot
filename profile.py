from prompt import Prompt

Prompt.InitPromptList()

class Profile:

    def __init__(self, id):
        self.id = id
        self.prompt = Prompt()
        self.complete = False  # A profile is complete if all prompts were answered correctly
        self.initial_btc = 0
        self.initial_usd_worth = 0
        self.desired_profit = 0

    
        
