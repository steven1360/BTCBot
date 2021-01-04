from prompt import Prompt
from btc import BTC

Prompt.InitPromptList()

class Profile:

    def __init__(self, user):
        self.user = user
        self.prompt = Prompt()
        self.complete = False  # A profile is complete if all prompts were answered correctly
        self.initial_btc = 0
        self.initial_btc_worth = 0
        self.fees = 0
        self.desired_profit = 0
        self.current_profit = 0

    def ImportPromptResponses(self):
        self.initial_btc = self.prompt.prompt_responses[0]
        self.initial_btc_worth = self.prompt.prompt_responses[1]
        self.fees = self.prompt.prompt_responses[2]
        self.desired_profit = self.prompt.prompt_responses[3]

    def IsReadyToSell(self):
        current_btc_price = BTC.usd_price
        initial_usd = (self.initial_btc * self.initial_btc_worth) - self.fees
        # print("---------------------------------------------------")
        # print("initial usd: " + str(initial_usd))
        current_usd = (self.initial_btc * float(current_btc_price))
        # print("current usd: " + str(current_usd))

        # print("profit: " + str(current_usd - initial_usd))
        # print("---------------------------------------------------")

        if (current_usd - initial_usd) >= self.desired_profit:
            self.current_profit = (current_usd - initial_usd)
            return True
        else:
            self.current_profit = 0
            return False
        

if __name__ == "__main__":
    profile = Profile(69)
    profile.initial_btc = 0.0007
    profile.initial_btc_worth = 30000
    profile.fees = 1.42
    profile.desired_profit = 5

    if profile.IsReadyToSell():
        print("Ready")
    else:
        print("Not Ready")