from . import db
from .db_handle import Match, Score, History, Num_history
from .functions import update_baseinfo
from sqlalchemy import func

def update_history_backend():
    fr_history = open("app/datasets/Dota2_history.csv")
    next(fr_history)
    for line in fr_history:
        line = line.split(',')
        update_baseinfo(line[1],line[2],line[3],line[4],line[5],line[6],line[7],
                        line[8],line[9],line[10],line[11],line[12],line[13],line[14])
    fr_history.close()
            
        
