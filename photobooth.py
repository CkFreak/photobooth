import interaction

response = interaction.start_conversation()

while response != "q":
    if response == "y" or response == "yes":
        interaction.countdown(5)
        interaction.take_picture()
        response = interaction.get_email_addresses()
        interaction.send_mail_to(response)
    else:
        print("Sad to see you leave! Enjoy the party ;)")
        response = interaction.start_conversation()
