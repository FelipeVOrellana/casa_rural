from odoo import models, fields

class TareaMantenimiento(models.Model):
    _name = 'casa_rural.tarea_mantenimiento'
    _description = 'Tareas de Mantenimiento: Registro de tareas programadas y ejecutadas'

    empleado_id = fields.Many2one('casa_rural.empleado', string='Empleado', required=True)
    habitacion_id = fields.Many2one('casa_rural.habitacion', string='Habitación')
    nombre_tarea = fields.Char(string='Nombre de la Tarea', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_programada = fields.Date(string='Fecha Programada')
    fecha_realizada = fields.Date(string='Fecha Realizada')
    estado = fields.Char(string='Estado')
    equipo_ids = fields.Many2many(
        'casa_rural.equipo',
        'casa_rural_tarea_equipo_rel',
        'tarea_id', 'equipo_id',
        string='Equipos'
    )