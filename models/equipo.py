from odoo import models, fields

class Equipo(models.Model):
    _name = 'casa_rural.equipo'
    _description = 'Equipos de la Casa Rural'

    nombre_equipo = fields.Char(string="Nombre del Equipo", required=True)
    tipo_equipo = fields.Char(string="Tipo de Equipo", required=True)
    fecha_adquisicion = fields.Date(string="Fecha de Adquisición", required=True)
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('en_uso', 'En Uso'),
        ('mantenimiento', 'En Mantenimiento')
    ], string="Estado", default='disponible')
    tarea_ids = fields.Many2many('casa_rural.tarea_mantenimiento', string="Tareas")