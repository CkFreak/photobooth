import interaction

response = interaction.start_conversation()

while response != "q":
    if response == "y" or response == "yes":
        print("Starting count-down!")
        print("Get Ready!")
        interaction.countdown(5)
        print("SMILE!")
        response = interaction.start_conversation()
    else:
        print("Sad to see you leave!")
        response = interaction.start_conversation()
