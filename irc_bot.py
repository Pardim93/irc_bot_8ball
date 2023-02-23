import socket
import random

question = ""
phrases = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]


server = "irc.freenode.net"  # We"re connecting to the freenode IRC server.
# A (probably) empty channel for testing the bot.
channel = "#SOMEEMPTYCHANNEL"
nickname = "magicbottest"  # The nickname of the bot.

# Create a socket instance.
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((server, 6667))
irc.send(("USER " + nickname + " " + nickname + " " +
         nickname + " :Magicbot\r\n").encode(encoding="UTF-8"))
irc.send(("NICK " + nickname + "\r\n").encode(encoding="UTF-8"))
irc.send(("JOIN " + channel + "\r\n").encode(encoding="UTF-8"))
# Infinite loop.
while True:
    # Recieve data from the socket, and decode it.
    recieved = irc.recv(2048).decode("UTF-8")
    # print(bytes(recieved, "UTF-8")) #If the server sends a PING.
    print(recieved)
    if recieved.startswith("PING"):
        # Respond with a PONG to prevent timing out.
        irc.send(("PONG " + recieved.split()[1] + "\r\n").encode())
        print("Ponged")
    if ":!8ball" in recieved:
        question = recieved.split(":!8ball")[1].strip()
    if question != "":
        irc.send(("PRIVMSG " + channel + " :" +
                 random.choice(phrases) + " \r\n").encode())
