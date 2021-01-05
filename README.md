# BTCBot
A discord bot for flipping bitcoin to make a quick profit.

# How Does It Work?
The bot starts off by asking the discord user four questions:
```
1. How many BTC are you trying to flip?
2. What was the USD price per 1 BTC when you bought them?
3. How much USD did you spend on fees when buying these BTC?
4. How much USD are you trying to make?
```
After answering these questions, the bot creates a profile for the user and constantly performs the calculations to determine whether it is a good time to sell their bitcoins. Behind the scenes, the bot captures the USD price of 1 BTC every 10 seconds. It incorporates this price value when doing the calculations to determine profitability. If the profit that can be made exceeds the user's response to question 4, then the bot will notify the user to sell X bitcoins to make Y USD. Finally, that user's profile gets deleted. A new profile can be made by answering the questions above again.

# Commands
Commands are aceepted only in DM chat with the bot
* `!start` - Starts a new profile. The bot will ask the set of questions above.
* `!cancel` - Maybe you already have a profile but got your numbers wrong. In that case, use this command to cancel.

# Example

After opening a DM to the bot, I enter the `!start` command (not shown in image). The bot responds by going directly to the questions, asking them one by one. At `1:29 AM`, I received confirmation that the bot has recorded my responses and will tell me when it's a good time to sell. `14` minutes later, while I am busy working on something else, discord pings me at `1:43 AM` saying that I should sell my bitcoins now. So, I open up some mobile app on my phone and sell my bitcoins immediately to make a quick profit. Then I'll start another profile to make another quick profit. This is how I am using the bot.

![BTCBot Example](/images/btcbot.JPG)
