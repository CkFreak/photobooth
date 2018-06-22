import interaction

response = interaction.start_conversation()

while response != "q":
    if response == "y" or response == "yes":
        interaction.countdown(5)
        response = interaction.take_picture()
    else:
        print("Sad to see you leave! Enjoy the party ;)")
        response = interaction.start_conversation()
