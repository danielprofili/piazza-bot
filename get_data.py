#!/usr/bin/python3

import piazza_api
from bs4 import BeautifulSoup
import sys



def add_text(convo,r_text):
    soup = BeautifulSoup(r_text,features='html.parser') #write responses
    r_text = soup.find(text=True)
    if r_text is not None:
        convo = convo + [r_text]
    return convo

p = piazza_api.Piazza()
print('Piazza Login')
email = input('Email: ')
password = input('Password: ')
p.user_login(email=email, password=password)
out_file = open('responses.txt','w')

class_url = sys.argv[1]
cs1371 = p.network(class_url)
posts = cs1371.iter_all_posts()

all_convos = []
for post in posts:
    #out_file.write(str(post['nr']))
    if 'student' in post['tags'] and len(post['children']) > 0:
        question = post['history'][-1]['content']
        soup = BeautifulSoup(question,features='html.parser')
        st_text = soup.find(text=True)
        if st_text is not None:
            convo = [st_text]
            #out_file.write(st_text + '\n') #write question
            for response in post['children']:
                if 'answer' in response['type']:
                    r_text = response['history'][-1]['content']
                    convo = add_text(convo,r_text)
                else:
                    r_text = response['subject']
                    convo = add_text(convo,r_text)
                    if response['children'] is not []:
                        for followup in response['children']:
                            r_text = followup['subject']
                            convo = add_text(convo,r_text)
                #soup = BeautifulSoup(r_text,features='html.parser') #write responses
                #r_text = soup.find(text=True)
                #if r_text is not None:
                #    convo = convo + [r_text]
                    #out_file.write(r_text + '\n')
    #out_file.write('\n')
        all_convos.append(convo)
out_file.writelines(['%s\n' % item for item in all_convos])
out_file.close()
print('done')
