import os
import csv
import pandas as pd
from . import db
from .db_handle import Match, Score, History, Num_history
from sqlalchemy import func



def update_baseinfo(tm_r, pos1_r, pos2_r, pos3_r, pos4_r,
                    pos5_r, tm_d, pos1_d, pos2_d, pos3_d,
                    pos4_d, pos5_d, a_result, time_stamp):
    match = Match(timestamp=time_stamp)
    db.session.add(match)
    db.session.commit()
    
    tmp_team_r = [tm_r]
    tmp_team_d = [tm_d]
    tmp_player_hero_list_r = [pos1_r, pos2_r, pos3_r, pos4_r, pos5_r]
    tmp_player_hero_list_d = [pos1_d, pos2_d, pos3_d, pos4_d, pos5_d]
    

    if (a_result=='1'): 
        ########## give score to radiant team ##########
        for tmp in tmp_team_r:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=1.0, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score += 1.0
                scan.exp += 1.0
                db.session.commit()
        for tmp in tmp_player_hero_list_r:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=1, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score += 1.0
                scan.exp += 1.0
                db.session.commit()
        ########## take score from dire team ##########
        for tmp in tmp_team_d:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=-1, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score -= 1.0
                scan.exp += 1.0
                db.session.commit()
        for tmp in tmp_player_hero_list_d:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=-1, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score -= 1.0
                scan.exp += 1.0
                db.session.commit()
        ########## ########## ##########
        
    else:
        ########## give score to dire team ##########
        for tmp in tmp_team_d:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=1, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score += 1.0
                scan.exp += 1.0
                db.session.commit()
        for tmp in tmp_player_hero_list_d:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=1, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score += 1.0
                scan.exp += 1.0
                db.session.commit()
        ########## take score from radiant team ##########
        for tmp in tmp_team_r:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=-1.0, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score -= 1.0
                scan.exp += 1.0
                db.session.commit()
        for tmp in tmp_player_hero_list_r:
            scan = Score.query.filter_by(team_player_hero=tmp).first()
            if (scan is None):
                score_add = Score(team_player_hero=tmp, success_score=-1, exp=1.0)
                db.session.add(score_add)
                db.session.commit()
            else:
                scan.success_score -= 1.0
                scan.exp += 1.0
                db.session.commit()
        ########## ########## ##########

    ########## update history (str_form) ##########
    update_history(tm_r, pos1_r, pos2_r, pos3_r, pos4_r, pos5_r, tm_d, pos1_d, pos2_d, pos3_d, pos4_d, pos5_d, a_result, time_stamp)
    ########## update history (str_form) ##########
    


def update_history(tm_r_str, pos1_r_str, pos2_r_str, pos3_r_str, pos4_r_str,
                    pos5_r_str, tm_d_str, pos1_d_str, pos2_d_str, pos3_d_str,
                    pos4_d_str, pos5_d_str, a_result, time_stamp):
    
    a_history = History(tm_r_str=tm_r_str, pos1_r_str=pos1_r_str, pos2_r_str=pos2_r_str,
                        pos3_r_str=pos3_r_str, pos4_r_str=pos4_r_str, pos5_r_str=pos5_r_str,
                        tm_d_str=tm_d_str, pos1_d_str=pos1_d_str, pos2_d_str=pos2_d_str,
                        pos3_d_str=pos3_d_str, pos4_d_str=pos4_d_str, pos5_d_str=pos5_d_str,
                        a_result=a_result, match_timestamp=time_stamp)
    db.session.add(a_history)
    db.session.commit()


def create_numerical_hist():
    Num_history.query.delete()
    hist_list = History.query.all()
    for a_hist in hist_list:
        hist_id             = a_hist.id
        hist_tm_r_str       = a_hist.tm_r_str
        hist_pos1_r_str     = a_hist.pos1_r_str
        hist_pos2_r_str     = a_hist.pos2_r_str
        hist_pos3_r_str     = a_hist.pos3_r_str
        hist_pos4_r_str     = a_hist.pos4_r_str
        hist_pos5_r_str     = a_hist.pos5_r_str
        hist_tm_d_str       = a_hist.tm_d_str
        hist_pos1_d_str     = a_hist.pos1_d_str
        hist_pos2_d_str     = a_hist.pos2_d_str
        hist_pos3_d_str     = a_hist.pos3_d_str
        hist_pos4_d_str     = a_hist.pos4_d_str
        hist_pos5_d_str     = a_hist.pos5_d_str
        hist_a_result       = a_hist.a_result
        hist_math_timestamp = a_hist.match_timestamp
        hist_result         = a_hist.a_result
        each_sc = dota2_dictionary(tm_r=hist_tm_r_str, pos1_r=hist_pos1_r_str, pos2_r=hist_pos2_r_str,
                                   pos3_r=hist_pos3_r_str, pos4_r=hist_pos4_r_str, pos5_r=hist_pos5_r_str,
                                   tm_d=hist_tm_d_str, pos1_d=hist_pos1_d_str, pos2_d=hist_pos2_d_str,
                                   pos3_d=hist_pos3_d_str, pos4_d=hist_pos4_d_str, pos5_d=hist_pos5_d_str)

        a_num_hist = Num_history(id=hist_id, tm_r_sc=each_sc[0][0], pos1_r_sc=each_sc[0][1], pos2_r_sc=each_sc[0][2], pos3_r_sc=each_sc[0][3],
                                 pos4_r_sc=each_sc[0][4], pos5_r_sc=each_sc[0][5], tm_d_sc=each_sc[0][6], pos1_d_sc=each_sc[0][7],
                                 pos2_d_sc=each_sc[0][8], pos3_d_sc=each_sc[0][9], pos4_d_sc=each_sc[0][10], pos5_d_sc=each_sc[0][11],
                                 a_result=hist_result)
        db.session.add(a_num_hist)
        db.session.commit()
        print("1 history has been added")
        

def dota2_dictionary(tm_r, pos1_r, pos2_r, pos3_r, 
                     pos4_r, pos5_r, tm_d, pos1_d,
                     pos2_d, pos3_d, pos4_d, pos5_d):
        
    # default_score = db.session.query(func.count(Match.id)).scalar()
    default_score = 2
    
    db_obj_tm_r   = Score.query.filter_by(team_player_hero=tm_r).first()
    if (not db_obj_tm_r):
        tm_r_sc = default_score
    else:
        raw_tm_r_sc   = db_obj_tm_r.success_score
        exp_tm_r      = db_obj_tm_r.exp
        tm_r_sc       = default_score + (raw_tm_r_sc/exp_tm_r)

    db_obj_pos1_r = Score.query.filter_by(team_player_hero=pos1_r).first()
    if (not db_obj_pos1_r):
        pos1_r_sc = default_score
    else:
        raw_pos1_r_sc = db_obj_pos1_r.success_score
        exp_pos1_r    = db_obj_pos1_r.exp
        pos1_r_sc     = tm_r_sc + (raw_pos1_r_sc/exp_pos1_r)

    db_obj_pos2_r = Score.query.filter_by(team_player_hero=pos2_r).first()
    if (not db_obj_pos2_r):
        pos2_r_sc = default_score
    else:
        raw_pos2_r_sc = db_obj_pos2_r.success_score
        exp_pos2_r    = db_obj_pos2_r.exp
        pos2_r_sc     = tm_r_sc + (raw_pos2_r_sc/exp_pos2_r)

    db_obj_pos3_r = Score.query.filter_by(team_player_hero=pos3_r).first()
    if (not db_obj_pos3_r):
        pos3_r_sc = default_score
    else:
        raw_pos3_r_sc = db_obj_pos3_r.success_score
        exp_pos3_r    = db_obj_pos3_r.exp
        pos3_r_sc     = tm_r_sc + (raw_pos3_r_sc/exp_pos3_r)

    db_obj_pos4_r = Score.query.filter_by(team_player_hero=pos4_r).first()
    if (not db_obj_pos4_r):
        pos4_r_sc = default_score
    else:
        raw_pos4_r_sc = db_obj_pos4_r.success_score
        exp_pos4_r    = db_obj_pos4_r.exp
        pos4_r_sc     = tm_r_sc + (raw_pos4_r_sc/exp_pos4_r)

    db_obj_pos5_r = Score.query.filter_by(team_player_hero=pos5_r).first()
    if (not db_obj_pos5_r):
        pos5_r_sc = default_score
    else:
        raw_pos5_r_sc = db_obj_pos5_r.success_score
        exp_pos5_r    = db_obj_pos5_r.exp
        pos5_r_sc     = tm_r_sc + (raw_pos5_r_sc/exp_pos5_r)

    db_obj_tm_d   = Score.query.filter_by(team_player_hero=tm_d).first()
    if (not db_obj_tm_d):
        tm_d_sc = default_score
    else:
        raw_tm_d_sc   = db_obj_tm_d.success_score
        exp_tm_d      = db_obj_tm_d.exp
        tm_d_sc       = default_score + (raw_tm_d_sc/exp_tm_d)

    db_obj_pos1_d = Score.query.filter_by(team_player_hero=pos1_d).first()
    if (not db_obj_pos1_d):
        pos1_d_sc = default_score
    else:
        raw_pos1_d_sc = db_obj_pos1_d.success_score
        exp_pos1_d    = db_obj_pos1_d.exp    
        pos1_d_sc     = tm_d_sc + (raw_pos1_d_sc/exp_pos1_d)

    db_obj_pos2_d = Score.query.filter_by(team_player_hero=pos2_d).first()
    if (not db_obj_pos2_d):
        pos2_d_sc = default_score
    else:
        raw_pos2_d_sc = db_obj_pos2_d.success_score
        exp_pos2_d    = db_obj_pos2_d.exp
        pos2_d_sc     = tm_d_sc + (raw_pos2_d_sc/exp_pos2_d)

    db_obj_pos3_d = Score.query.filter_by(team_player_hero=pos3_d).first()
    if (not db_obj_pos3_d):
        pos3_d_sc = default_score
    else:
        raw_pos3_d_sc = db_obj_pos3_d.success_score
        exp_pos3_d    = db_obj_pos3_d.exp
        pos3_d_sc     = tm_d_sc + (raw_pos3_d_sc/exp_pos3_d)

    db_obj_pos4_d = Score.query.filter_by(team_player_hero=pos4_d).first()
    if (not db_obj_pos4_d):
        pos4_d_sc = default_score
    else:
        raw_pos4_d_sc = db_obj_pos4_d.success_score
        exp_pos4_d    = db_obj_pos4_d.exp
        pos4_d_sc     = tm_d_sc + (raw_pos4_d_sc/exp_pos4_d)

    db_obj_pos5_d = Score.query.filter_by(team_player_hero=pos5_d).first()
    if (not db_obj_pos5_d):
        pos5_d_sc = default_score
    else:
        raw_pos5_d_sc = db_obj_pos5_d.success_score
        exp_pos5_d    = db_obj_pos5_d.exp
        pos5_d_sc     = tm_d_sc + (raw_pos5_d_sc/exp_pos5_d)

    X_input = [[tm_r_sc, pos1_r_sc, pos2_r_sc, pos3_r_sc,
                pos4_r_sc, pos5_r_sc, tm_d_sc, pos1_d_sc,
                pos2_d_sc, pos3_d_sc, pos4_d_sc, pos5_d_sc]]

    return X_input


def export_csv_num_history():
    with open('app/datasets/Dota2_num_history.csv', 'w') as fw:
        out = csv.writer(fw)
        out.writerow(['id','tm_r_sc','pos1_r_sc','pos2_r_sc','pos3_r_sc','pos4_r_sc','pos5_r_sc','tm_d_sc','pos1_d_sc','pos2_d_sc','pos3_d_sc','pos4_d_sc','pos5_d_sc','a_result'])

        for item in Num_history.query.all():
            out.writerow([item.id,item.tm_r_sc,item.pos1_r_sc,item.pos2_r_sc,item.pos3_r_sc,item.pos4_r_sc,item.pos5_r_sc,item.tm_d_sc,item.pos1_d_sc,item.pos2_d_sc,item.pos3_d_sc,item.pos4_d_sc,item.pos5_d_sc,item.a_result])


def load_Num_history(file_name='Dota2_Num_history.csv'):
    csv_path = os.path.join('app/datasets', file_name)
    features = ['id', 'tm_r_sc', 'pos1_r_sc', 'pos2_r_sc', 'pos3_r_sc', 'pos4_r_sc', 'pos5_r_sc', 'tm_d_sc', 'pos1_d_sc', 'pos2_d_sc', 'pos3_d_sc', 'pos4_d_sc', 'pos5_d_sc', 'a_result']
    return pd.read_csv(csv_path, header = 0, sep = ',', names=features) 