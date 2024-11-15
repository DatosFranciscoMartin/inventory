from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional

class EquipoForm(FlaskForm):
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    nserie = StringField('Número de Serie', validators=[DataRequired()])
    licencia = StringField('Licencia', validators=[Optional()])
    fecha_compra = DateField('Fecha de Compra', format='%Y-%m-%d', validators=[Optional()])
    esta_en_soporte = BooleanField('¿Está en Soporte?', default=True)
    sitio_id = SelectField('Sitio Asociado', coerce=int, validators=[Optional()])
    fecha_fin = DateField('Fecha de Finalización', format='%Y-%m-%d', validators=[Optional()])
    renovacion = DateField('Fecha de Renovación', format='%Y-%m-%d', validators=[Optional()])
    contacto_id = SelectField('Contacto Asociado', coerce=int, validators=[Optional()])
    submit = SubmitField('Guardar')
