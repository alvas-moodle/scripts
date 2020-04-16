#!/usr/bin/python3








import base64
import cv2
import sys
import os
import time

print(
"""
    _    _                      __  __                 _ _      
   / \  | |_   ____ _ ___      |  \/  | ___   ___   __| | | ___ 
  / _ \ | \ \ / / _` / __|_____| |\/| |/ _ \ / _ \ / _` | |/ _ \\
 / ___ \| |\ V / (_| \__ \_____| |  | | (_) | (_) | (_| | |  __/
/_/   \_\_| \_/ \__,_|___/     |_|  |_|\___/ \___/ \__,_|_|\___|
                                                                
                                                               
""")


dir = sys.argv[1]

print()
print()

output_file = sys.argv[2]


files = os.listdir(dir)

questions, descriptions = [], []

for file in files:
    if 'Q' in file:
        questions.append(file)


questions.sort(key=lambda x: int(x.strip('Q').strip('.png')) )



print(questions)




answers = {}

with  open( os.path.join(dir, 'answers.txt')) as answers_processor:
    format  = answers_processor.readline().strip()
    print(format)
    for line in answers_processor.readlines():
        question, answer = line.strip().split('=')
        answers[question] = int(answer) - 1

# print(answers)





template = '''
::{0}::[html]<p><img src\="data\:image/png;base64,{1}" alt\="" role\="presentation" class\="img-responsive atto_image_button_text-bottom" width\="{2}" height\="{3}"><br></p>{{
    {4}<p>1<br></p>
    {5}<p>2<br></p>
    {6}<p>3<br></p>
    {7}<p>4<br></p>
}}

'''


with open(output_file, 'w') as out_file:
    for question in questions:

        num = question.strip('Q').strip('.png')
        
        question = os.path.join(dir, question) 
        height1, width1, _ = cv2.imread(question).shape

        initial = ['~' for  _  in range(4) ]

        if format in {'neet', 'jee'}:
              initial = ['~%-25%' for  _  in range(4) ]
        initial[ answers[num] ] = '='
        one, two, three, four = initial

        with open(question, "rb") as image_file:
           encoded_string1 = base64.b64encode(image_file.read()).decode()


        out_file.write(template.format(num, encoded_string1, width1, height1, one, two, three, four  ) )



print('Process completed ........')
time.sleep(1)
sys.exit(0)
