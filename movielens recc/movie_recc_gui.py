import pandas as pd
import warnings
warnings.filterwarnings('ignore')
## import os
## print(os.getcwd())

import tkinter as ttk
app = ttk.Tk()
app.title('Movie Reccomendor System')
app.geometry("800x700")

#Reading the Data Files
cols = ['user_id', 'movie_id', 'rating', 'ts']
df = pd.read_csv('u.data', sep = '\t', names = cols).drop('ts', axis = 1)
item_cols = ['movie_id', 'title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep = '|', names = item_cols, encoding = "ISO-8859-1")[['movie_id', 'title']]
    
#Merging the two Data Frames
movie = pd.merge(df, df1, on = 'movie_id')

result = ttk.Variable(app)


frame = ttk.Frame(app)
frame.place(x=10, y=10)

box = ttk.Listbox(frame, height=10, width=50)
for title in movie['title'].unique():
    box.insert(ttk.END, title)

box.pack(side='left', fill='y')
## box.grid(row=0, column=0)
## box.place(x=10, y=10)

# scroll bar adding
scroll = ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(command = box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right', fill='y')


def get_movie():
    pass
    movie_selected = box.get(box.curselection())
    print('movie_selected:', movie_selected)

    #Creating a Pivot Table
    movie_pivot = movie.pivot_table(index = 'user_id', columns = 'title', values = 'rating')
    
    #Finding the similarity for the Selected Movie
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df = pd.DataFrame(corrs, columns = ['correlation'])
    corrs_df['avg_ratings'] = movie.groupby('title')['rating'].mean()
    corrs_df['count'] = movie['title'].value_counts()
    
    #Finding the top 2-3 Recommendations
    top_recom = list(corrs_df[corrs_df['count'] > 50].sort_values(by = 'correlation', ascending = False).head(3).index)
    
    ## important
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)

    print('Recommendations: ',top_recom)

    if top_recom:
        result.set(top_recom[0])
    else:
        result.set('Sorry no recommendations Found !! ')


ttk.Button(app, text="Find Reccomendations", font= ('Arial',22), command = get_movie).place(x=10, y=250)


ttk.Label(app, textvariable=result, font=('Arial',22)).place(x=10, y=350)






app.mainloop()