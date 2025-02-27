from odoo import models, fields

class TareaMantenimiento(models.Model):
    _name = 'casa_rural.tarea_mantenimiento'
    _description = 'Tareas de Mantenimiento de la Casa Rural'

    nombre_tarea = fields.Char(string="Nombre de la Tarea", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_programada = fields.Date(string="Fecha Programada", required=True)
    fecha_realizada = fields.Date(string="Fecha Realizada")
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada')
    ], string="Estado", default='pendiente')
    empleado_id = fields.Many2one('casa_rural.empleado', string="Empleado")
    equipo_ids = fields.Many2many('casa_rural.equipo', string="Equipos")
    habitacion_id = fields.Many2one('casa_rural.habitacion', string="Habitación")