from . import db
from datetime import datetime

class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    timestamp = db.Column(db.String(45), nullable=True) 

    
    def __repr__(self):
        return f"Match('{self.timestamp}')"


class Score(db.Model):
    __tablename__ = 'score'
    team_player_hero = db.Column(db.String(45), primary_key=True, unique=True, nullable=False)
    success_score = db.Column(db.Float, nullable=False)
    exp = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"Score('{self.team_player_hero}', '{self.success_score}', '{self.exp}')"


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    tm_r_str = db.Column(db.String(45), unique=False, nullable=False)
    pos1_r_str = db.Column(db.String(45), unique=False, nullable=False)
    pos2_r_str = db.Column(db.String(45), unique=False, nullable=False)
    pos3_r_str = db.Column(db.String(45), unique=False, nullable=False)
    pos4_r_str = db.Column(db.String(45), unique=False, nullable=False)
    pos5_r_str = db.Column(db.String(45), unique=False, nullable=False)
    tm_d_str = db.Column(db.String(45), unique=False, nullable=False)
    pos1_d_str = db.Column(db.String(45), unique=False, nullable=False)
    pos2_d_str = db.Column(db.String(45), unique=False, nullable=False)
    pos3_d_str = db.Column(db.String(45), unique=False, nullable=False)
    pos4_d_str = db.Column(db.String(45), unique=False, nullable=False)
    pos5_d_str = db.Column(db.String(45), unique=False, nullable=False)
    a_result = db.Column(db.Integer, unique=False, nullable=True)
    match_timestamp = db.Column(db.String(45), default=datetime.utcnow)

    def __repr__(self):
        return f"History('{self.tm_r_str}', '{self.pos1_r_str}', '{self.pos2_r_str}', '{self.pos3_r_str}', '{self.pos4_r_str}', '{self.pos5_r_str}', '{self.tm_d_str}','{self.pos1_d_str}', '{self.pos2_d_str}', '{self.pos3_d_str}', '{self.pos4_d_str}', '{self.pos5_d_str}', '{a_result}', '{match_timestamp}')"    

class Num_history(db.Model):
    __tablename__ = 'num_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    tm_r_sc   = db.Column(db.String(45), unique=False, nullable=False)
    pos1_r_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos2_r_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos3_r_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos4_r_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos5_r_sc = db.Column(db.String(45), unique=False, nullable=False)
    tm_d_sc   = db.Column(db.String(45), unique=False, nullable=False)
    pos1_d_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos2_d_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos3_d_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos4_d_sc = db.Column(db.String(45), unique=False, nullable=False)
    pos5_d_sc = db.Column(db.String(45), unique=False, nullable=False)
    a_result  = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"History('{self.tm_r_sc}', '{self.pos1_r_sc}', '{self.pos2_r_sc}', '{self.pos3_r_sc}', '{self.pos4_r_sc}', '{self.pos5_r_sc}', '{self.tm_d_sc}','{self.pos1_d_sc}', '{self.pos2_d_sc}', '{self.pos3_d_sc}', '{self.pos4_d_sc}', '{self.pos5_d_sc}', '{self.a_result}')"    




db.create_all()