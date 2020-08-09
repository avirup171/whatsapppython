# WhatsApp message send using python and selenium

This is a simple implementation by which you can use a python script to send whatsapp messages. I have used selenium for automation. 

## How it works?

Its pretty much simple to understand. 
1. Mention the name of the contact you want to send
2. The name of the contact is searched with the title tag
3. The contact is selected with a click event triggered from the code
4. The message is then sent to the textbox and an enter key press is triggered from the code to send the message.

## Requirements
1. Python 3.7
2. Google chrome version 84
3. Chromedriver for chrome version 84
4. Selenium

## Usage

1. CLone this repo
2. open the terminal and type in
```
pip install - r requirements.txt
```
3. Edit the code in terms of whats the message or group of message you want to send
4. Edit the name of the contact
5. Execute app.py
6. Enjoy

## Code description

```
class WhatsappAutomate
```
It contains a parameterised constructor which takes in 2 params
1. url: https://web.whatsapp.com
2. sendTo: The name of the contact whom you need to send the message

```
sendMessage(messageList)
```
This takes in the messageList as a parameter which contains a list of messages to send

```
main()
```
1. Invoke the class and the constructor
2. Pass in the message list and done