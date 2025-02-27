from odoo import models, fields

class CanalComunicacion(models.Model):
    _name = 'casa_rural.canal_comunicacion'
    _description = 'Canales de Comunicación de la Casa Rural'

    nombre_canal = fields.Char(string="Nombre del Canal", required=True)
    descripcion = fields.Text(string="Descripción")
    mensaje_ids = fields.One2many('casa_rural.mensaje', 'canal_comunicacion_id', string="Mensajes")