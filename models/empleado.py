from odoo import models, fields

class Empleado(models.Model):
    _name = 'casa_rural.empleado'
    _description = 'Empleados de la Casa Rural'

    nombre = fields.Char(string="Nombre", required=True)
    cargo = fields.Char(string="Cargo", required=True)
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    tarea_ids = fields.One2many('casa_rural.tarea_mantenimiento', 'empleado_id', string="Tareas")