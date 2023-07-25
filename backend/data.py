import pandas as pd 
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route('/api/dane_zawodow')

def getDate ():
    df_competition =  {
    'Data': ['06-08-2023', '03-09-2023',],
    'Nazwa': ['Ironman Gdynia', '5150 Poznan'],
    'Miejsce': ['Gdynia', 'Poznan']
}
    df_competition_dataframe = pd.DataFrame(df_competition)

    df_competition_json = df_competition_dataframe.to_json(orient='records', force_ascii=False)

    return jsonify(df_competition_json)



if __name__ == '__main__':
    app.run()









