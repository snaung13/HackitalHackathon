from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
import random
import pandas as pd 
import random
import numpy as np
df=pd.read_excel('Database.xlsx',sheetname='Sheet1')
data = df.replace(np.nan, '', regex=True)


@app.route("/")
def index():
    return render_template('test.html')

@app.route("/result", methods=['GET','POST'])
def result():
    carb_food=[]
    LNS_food=[]
    vegetables_food=[]
    dessert_food=[]
    protein_food=[]
    choice_food=[]
    recommended=[]
    recommended_display=''
    calo=0
    protein=0
    vitaminA=0
    fiber=0
    meal = request.form['meal']
    for i in range(len(data['Type'])):
        if data['Type'][i]=='carb':
            carb_food.append(data['Food'][i])
    for i in range(len(data['Type'])):
        if data['Type'][i]=='protein':
            protein_food.append(data['Food'][i])
    for i in range(len(data['Type'])):
        if data['Type'][i]=='vegetables':
            vegetables_food.append(data['Food'][i])
    for i in range(len(data['Type'])):
        if data['Type'][i]=='dessert':
            dessert_food.append(data['Food'][i])
    for i in range(len(data['Type'])):
        if data['Type'][i]=='LNS':
            LNS_food.append(data['Food'][i])                
    if meal=='breakfast':
        for i in range(19):
            if 'B' in data['Meals'][i]:
                choice_food.append(data['Food'][i])
        food=random.choice(choice_food)
        recommended.append(food)
        if data['Type'][data.loc[data['Food']==food].index[0]]=='carb':#Check if it's carb,protein
            recommended.append(random.choice(vegetables_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(LNS_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='vegetables':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(LNS_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='dessert':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(LNS_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(vegetables_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='protein':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(LNS_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(vegetables_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='LNS':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(vegetables_food))                          
    elif meal=='lunch':
        for i in range(19):
            if 'L' in data['Meals'][i]:
                choice_food.append(data['Food'][i])
        food=random.choice(choice_food)
        recommended.append(food)
        if data['Type'][data.loc[data['Food']==food].index[0]]=='carb':#Check if it's carb,protein
            recommended.append(random.choice(vegetables_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(LNS_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='vegetables':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(LNS_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='dessert':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(LNS_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(vegetables_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='protein':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(LNS_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(vegetables_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='LNS':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(vegetables_food))  
    elif meal=='dinner':
        for i in range(19):
            if 'D' in data['Meals'][i]:
                choice_food.append(data['Food'][i])
        food=random.choice(choice_food)
        recommended.append(food)
        if data['Type'][data.loc[data['Food']==food].index[0]]=='carb':#Check if it's carb,protein
            recommended.append(random.choice(vegetables_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(LNS_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='vegetables':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(LNS_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='dessert':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(LNS_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(vegetables_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='protein':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(LNS_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(vegetables_food))
        elif data['Type'][data.loc[data['Food']==food].index[0]]=='LNS':
            recommended.append(random.choice(carb_food))
            recommended.append(random.choice(protein_food))
            recommended.append(random.choice(dessert_food))
            recommended.append(random.choice(vegetables_food))
    recommended_display=', '.join(recommended)+' for '+meal 
    for output in recommended:
        calo=calo+data['calories'][data.loc[data['Food']==output].index[0]]
    for output in recommended:
        protein=protein+data['Protein(grams)'][data.loc[data['Food']==output].index[0]]
    for output in recommended:
        vitaminA=vitaminA+data['vitamin A%'][data.loc[data['Food']==output].index[0]]
    for output in recommended:
        fiber=fiber+data['Dietary Fiber(grams)'][data.loc[data['Food']==output].index[0]]   
    return render_template('second.html',fiber=fiber,vitaminA=vitaminA, food=recommended_display, calories=calo,protein=protein)
if __name__ == "__main__":
	app.run()



    
            


