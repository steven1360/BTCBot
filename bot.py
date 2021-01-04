from discord.ext import commands
from profile import Profile
from btc import BTC
import asyncio

TOKEN = 'NzkzMzEwOTExMjY3NDcxNDAw.X-qaXA.ZEWRXzoBc59KuSqJ22dSMt-gLoc'

class BTCBot(commands.Bot):

    profiles = {}
    
    def __init__(self, command_prefix):
        commands.Bot.__init__(self, command_prefix=command_prefix)
        self.InitCommands()
    
    async def on_ready(self):
        print("Ready!")

    async def ScanProfiles(self):
        BTC.UpdatePrice()
        while True:

            up_for_deletion = []

            for user, profile in BTCBot.profiles.items():

                if profile.complete and profile.IsReadyToSell():
                    await profile.user.send(user.mention)
                    message = "```Right now is a good time to sell your BTC.\n"
                    message += "The current price of BTC is {} USD per 1 BTC.\n".format(BTC.usd_price)
                    message += "You bought your BTC when it was {} USD per 1 BTC.\n".format(profile.initial_btc_worth)
                    message += "Your profit would be {} USD if you sell now!```".format(profile.current_profit)
                    await profile.user.send(message)
                    up_for_deletion.append(user)

            for user in up_for_deletion:
                del BTCBot.profiles[user]
            
            await asyncio.sleep(10)
            BTC.UpdatePrice()

    
    async def on_message(self, message):

        user = self.get_user(message.author.id) 
        
        if user in BTCBot.profiles.keys():
            prompt = BTCBot.profiles[user].prompt
            profile_is_complete = BTCBot.profiles[user].complete
            status = prompt.CollectResponse(message.content)

            if not profile_is_complete:
              
                if status == 0:

                    if prompt.AllResponsesCompleted():
                        BTCBot.profiles[user].complete = True
                        BTCBot.profiles[user].ImportPromptResponses()
                        await user.send("Registered all responses. I will ping you whenever it's a good time to sell your BTC.")
                    else:
                        next_prompt = prompt.GetNextPrompt()
                        await user.send(next_prompt)
                else:
                    await user.send("Sorry, I do not understand your response. Please try again.")

        
        await bot.process_commands(message)
    
    def InitCommands(self):

        @self.command()
        async def start(ctx):
            
            user = self.get_user(ctx.message.author.id) 

            if user not in BTCBot.profiles.keys():
                BTCBot.profiles[user] = Profile(user)
                prompt = BTCBot.profiles[user].prompt
                next_prompt = prompt.GetNextPrompt()
                await user.send(next_prompt)
            else:
                await user.send("I have already recorded your responses. To cancel, use the !cancel command.")

        @self.command()
        async def cancel(ctx):
            user = self.get_user(ctx.message.author.id) 

            if user in BTCBot.profiles.keys():
                await user.send("Your responses were canceled. You can start a new profile with the !start command.")
                del BTCBot.profiles[user]
            else:
                await user.send("I have already recorded your responses. To cancel, use the !cancel command.")


bot = BTCBot(command_prefix="!")
bot.loop.create_task(bot.ScanProfiles())
bot.run(TOKEN)

