from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class Input(FlaskForm):
    tm_r = StringField('Team_r', validators=[DataRequired()])
    pos1_r = StringField('Pos1_r', validators=[DataRequired()])
    pos2_r = StringField('Pos2_r', validators=[DataRequired()])
    pos3_r = StringField('Pos3_r', validators=[DataRequired()])
    pos4_r = StringField('Pos4_r', validators=[DataRequired()])
    pos5_r = StringField('Pos5_r', validators=[DataRequired()])
    tm_d = StringField('Team_d', validators=[DataRequired()])
    pos1_d = StringField('Pos1_d', validators=[DataRequired()])
    pos2_d = StringField('Pos2_d', validators=[DataRequired()])
    pos3_d = StringField('Pos3_d', validators=[DataRequired()])
    pos4_d = StringField('Pos4_d', validators=[DataRequired()])
    pos5_d = StringField('Pos5_d', validators=[DataRequired()])

    submit = SubmitField('Predict')


class Update(FlaskForm):
    tm_r = StringField('Team_r', validators=[DataRequired()])
    pos1_r = StringField('Pos1_r', validators=[DataRequired()])
    pos2_r = StringField('Pos2_r', validators=[DataRequired()])
    pos3_r = StringField('Pos3_r', validators=[DataRequired()])
    pos4_r = StringField('Pos4_r', validators=[DataRequired()])
    pos5_r = StringField('Pos5_r', validators=[DataRequired()])
    tm_d = StringField('Team_d', validators=[DataRequired()])
    pos1_d = StringField('Pos1_d', validators=[DataRequired()])
    pos2_d = StringField('Pos2_d', validators=[DataRequired()])
    pos3_d = StringField('Pos3_d', validators=[DataRequired()])
    pos4_d = StringField('Pos4_d', validators=[DataRequired()])
    pos5_d = StringField('Pos5_d', validators=[DataRequired()])
    a_result = StringField('Result (win/lose)', validators=[DataRequired()])
    # time_stamp = DateTimeField('time_stamp')
    time_stamp = StringField('Time_stamp')

    submit = SubmitField('Update')
    

