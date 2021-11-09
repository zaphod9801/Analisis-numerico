from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length


metodos = [("Busqueda Incremental",1),("Biseccion",2),("Regla Falsa",3),("Punto fijo",4),("Newton",5),("Secante",6),("Raices Multiples",7),("Gaussiana Simple",8)]

class SelectorMetodos(FlaskForm):
    metodo: int = SelectField('Metodo: ', validators=[DataRequired()],choices=metodos)
    submit = SubmitField('Seleccionar')

class BusquedaIncrementalF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    x0: float = FloatField('Punto inicial: ', validators=[DataRequired(), Length(max=64)])
    h: float = FloatField('Paso: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
    
class BiseccionF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    a: float = FloatField('Inicio del intervalo: ', validators=[DataRequired(), Length(max=64)])
    b: float = FloatField('Fin del intervalo: ', validators=[DataRequired(), Length(max=64)])
    t: float = FloatField('Tolerancia: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
class ReglaFalsaF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    a: float = FloatField('Inicio del intervalo: ', validators=[DataRequired(), Length(max=64)])
    b: float = FloatField('Fin del intervalo: ', validators=[DataRequired(), Length(max=64)])
    t: float = FloatField('Tolerancia: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
class PuntoFijoF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    funcionG: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    x0: float = FloatField('Punto inicial: ', validators=[DataRequired(), Length(max=64)])
    t: float = FloatField('Tolerancia: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
class NewtonF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    funcionD: str = StringField('Primera derivada de la función: ', validators=[DataRequired(), Length(max=64)])
    x0: float = FloatField('Punto inicial: ', validators=[DataRequired(), Length(max=64)])
    t: float = FloatField('Tolerancia: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
class SecanteF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    X0: float = FloatField('Punto inicial: ', validators=[DataRequired(), Length(max=64)])
    X1: float = FloatField('Segundo punto: ', validators=[DataRequired(), Length(max=64)])
    t: float = FloatField('Tolerancia: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
class RaicesMLTF(FlaskForm):
    funcion: str = StringField('Función: ', validators=[DataRequired(), Length(max=64)])
    funcionD: str = StringField('Primera derivada de la función: ', validators=[DataRequired(), Length(max=64)])
    funcion2D: str = StringField('Segunda derivada de la función: ', validators=[DataRequired(), Length(max=64)])
    x0: float = FloatField('Punto inicial: ', validators=[DataRequired(), Length(max=64)])
    t: float = FloatField('Tolerancia: ', validators=[DataRequired(), Length(max=64)])
    n: int = IntegerField('Iteraciones maximas: ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
class GaussianaSimpleF(FlaskForm):
    matriz: str = StringField('Matriz de coeficientes (en formato de python): ', validators=[DataRequired(), Length(max=64)])
    vector: str = StringField('Vector de terminos independientes (en formato de python): ', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Calcular')
    
