

class Prompt:

    prompt_list = []

    def __init__(self):
        self.prompt_responses = [-1 for i in range(0, len(Prompt.prompt_list))]
        self.current_prompt = 0

    @classmethod
    def InitPromptList(cls):
        first_prompt = "How many BTC are you trying to flip?"
        second_prompt = "How much USD were these BTC worth when you bought them?"
        third_prompt = "How much USD did you spend in fees when buying these BTC?"
        fourth_prompt = "How much USD are you trying to make?"

        cls.prompt_list.append(first_prompt)
        cls.prompt_list.append(second_prompt)
        cls.prompt_list.append(third_prompt)
        cls.prompt_list.append(fourth_prompt)
    
    def GetNextPrompt(self):
        if self.prompt_responses[self.current_prompt] != -1:
            self.current_prompt = (self.current_prompt + 1) % len(Prompt.prompt_list)

        return Prompt.prompt_list[self.current_prompt]

    def CollectResponse(self, response):
        
        try:
            response = float(response)
            self.prompt_responses[self.current_prompt] = response
            return 0
        except ValueError:
            return -1

    def AllResponsesCompleted(self):
        for response in self.prompt_responses:
            if response == -1:
                return False
        return True
