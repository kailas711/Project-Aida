import google.generativeai as genai

def Gemini_login():
    genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def clear_history():
    chat = model.start_chat(history=[])

def gemini_email_prompt(emails):
    response = chat.send_message(f"""
    Behave like a useful assistant
    A list of emails from a python scapper program is passed on to you via a python object as input , go trough them and elabortae in bullet points what each email is taking about. There are chances of same content with different index ignore it as it is from a scrapper bot.These emails are from my personal inbox.
    The index number is not the total number of emails.Start with mentioning from whon the email came the and later use the subject and the content to elaborate.

    {emails}
    """)
    return response.text

def gemini_medium_prompt(medium):
    response = chat.send_message(f"""
Behave like a useful assistant
A list of top headlines from the microblogging website medium.com from a python scapper program is passed on to you via a python object as input , go trough them and elabortae in bullet points what each blog is taking about.Please provide a brief summary of what the trending headlines are discussing.
                                                                 
The content follows the format 
author <spaces> optional topic or publisher <space> heading of blog 
                                 
These articles are from my personal recomendation in the website bwhich i got based on my profile.
                                                  
    {medium}
""")

    return response.text

def model_msg(message):
    response = chat.send_message(
    f""" Question : 
    
    {message}
                    
    reply like a friendly bot.""")

    return response.text
