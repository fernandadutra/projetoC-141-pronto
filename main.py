from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": int(all_articles.iloc[0,4])
    }
    return m_data

# API para exibir o primeiro artigo
@app.route("/get-article")
def get_article():
    articles_info=assign_val()

    return jsonify({
        "data":articles_info,
        "status": "success"
    })

    #return 'Escreva o código para exibir o primeiro item na lista all_articles'


# API para mover o artigo para a lista de artigos curtidos
@app.route("/liked-article")
def liked_article():
    global all_articles

    articles_info=assign_val()
    liked_articles.append(articles_info)

    all_articles.drop([0], inplace=True)
    all_articles= all_articles.reset_index(drop=True)


    return jsonify({
        "status": "success"
    })

    #return 'Escreva o código para mudar o primeiro artigo para a lista liked_articles'


# API para mover o artigo para a lista de artigos não curtidos
@app.route("/unliked-article")
def unliked_article():
     global all_articles

     articles_info=assign_val()
     not_liked_articles.append(articles_info)

     all_articles.drop([0], inplace=True)
     all_articles= all_articles.reset_index(drop=True)

     return jsonify({
        "status": "success"
    })

    #return 'Escreva o código para mudar o primeiro artigo para a lista not_liked_articles'

# execute o aplicativo
if __name__ == "__main__":
    app.run()
