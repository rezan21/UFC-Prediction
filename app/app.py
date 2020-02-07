import streamlit as st
import altair as alt
import pandas as pd
import pickle
from PIL import Image
# encode blue=1 & red=0

# style css
st.markdown('''
        <style>
            @import url('https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300&display=swap');

            * {
                font-size: 1.2rem;
                margin: 0;
                padding: 0;
                -webkit-box-sizing: border-box;
                box-sizing: border-box;
                font-family: 'Open Sans Condensed', sans-serif !important;
                text-align:center;
            }


            #general{
                font-size: 19.2px;
                
            }
            #rtitle{
                                
            }
            #rsubheader{
                text-align: center;
                margin:0px 0px 10px 0px;
                padding: 12px 0px 30px 0px; 
                border-bottom: 1px solid #909090;
            }
            .reportview-container .main .block-container{
                padding: 2rem 1rem !important;
            }
            .reportview-container h1{
                padding:0;
                margin:0;
            }

            .reportview-container .main footer{
                display: none !important;
            }
            
        </style>
        ''',unsafe_allow_html=True)


st.markdown('''
<h1  id="rtitle" class="rgeneral" style="margin-bottom: 20px; margin-top:0px !important; padding-top:0px !important;"> UFC Prediction</h1>
''', unsafe_allow_html=True)

img = Image.open('ufc.jpg')
st.image(img, width=500)

st.markdown(''' 
<h3 id="rsubheader"> 🥊 Predict the result of upcoming UFC events by the power of AI and Machine Learning!</h3>
 ''', unsafe_allow_html=True)

st.markdown('''
    <div class="my-top-text"> 
        <p><b id="general">Algorithm:</b> The app uses multiple Machine Learning models which are trained on the dataset of all UFC events from 1993 to 2019 in order to find reocuuring patterns and predict an sporting event in the future. <br> For technical details, please <a id="general" href="https://github.com/rezan21/UFC-Prediction">visit github repository</a>.</p>
    </div>
''', unsafe_allow_html=True)



df = pd.read_csv("FIGHTER_STAT.CSV")
fighters = df["fighter"].tolist()
ens_method = pickle.load(open("ens_method.sav", 'rb'))

def predictEnsemble(sample):
    prediction = ens_method.predict(sample)
    return (prediction)

def predictMatchByID(B, R):
    blueFighter = df[df["ID"] == B].iloc[:,3:]
    blueFighter.columns = ['B_'+col for col in blueFighter.columns] #concat prefix B_ and rename columns

    redFighter = df[df["ID"] == R].iloc[:,3:]
    redFighter.columns = ['R_'+col for col in redFighter.columns]

    blueFighter.reset_index(drop=True,inplace=True)
    redFighter.reset_index(drop=True,inplace=True)

    toPredict = pd.concat([blueFighter,redFighter],axis=1).values
    return (toPredict)

def main():
    r_fighter = st.selectbox("Red Fighter", fighters)
    b_fighter = st.selectbox("Blue Fighter", fighters)
    submitBtn = st.button("Predict Match")

    if(submitBtn):
        if b_fighter == r_fighter:
            st.error("Please choose 2 distict fighters")
        else:
            try:
                players = {
                    1:str(b_fighter),
                    0:str(r_fighter)
                }

                b_id = df["ID"][df["fighter"]==b_fighter].values[0]
                r_id = df["ID"][df["fighter"]==r_fighter].values[0]
                #print(f"blue id: {b_id}, red id: {r_id}")
                sample = predictMatchByID(b_id, r_id)
                #print(sample)

                prediction = predictEnsemble(sample).tolist()[0]
                #st.title(prediction)

                st.success(players[prediction] + ' Wins')
            except Exception as e:
                #st.write(e)
                st.error("Something went wrong! Reload the page and try again.")

    st.markdown('''
        <div style="padding-top:100px;"> 
        <p><b id="general">Disclaimer:</b> The performance represented is historical and past performance is not a reliable indicator of future results and investors may not recover the full amount invested.  I do not condone this app's use for betting. I am not responsible for any damage done or losses incurred by way of this app.</p>
        </div>
        ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    
