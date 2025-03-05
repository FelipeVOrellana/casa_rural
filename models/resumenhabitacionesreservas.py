from odoo import models, fields, api

class ResumenHabitacionesReservas(models.Model):
    _name = 'casa_rural.resumenhabitacionesreservas'
    _description = 'Resumen de Habitaciones y Reservas'

    tipo_habitacion = fields.Selection([
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite')
    ], string="Tipo de Habitación")
    habitaciones_totales = fields.Integer(string="Habitaciones Totales", compute='_compute_habitaciones')
    habitaciones_disponibles = fields.Integer(string="Habitaciones Disponibles", compute='_compute_habitaciones')
    habitaciones_ocupadas = fields.Integer(string="Habitaciones Ocupadas", compute='_compute_habitaciones')
    porcentaje_ocupacion = fields.Float(string="Ocupación (%)", compute='_compute_habitaciones')
    reservas_activas = fields.Integer(string="Reservas Activas", compute='_compute_reservas')

    @api.depends('tipo_habitacion')
    def _compute_habitaciones(self):
        for record in self:
            habitaciones = self.env['casa_rural.habitacion'].search([('tipo', '=', record.tipo_habitacion)])
            record.habitaciones_totales = len(habitaciones)
            record.habitaciones_disponibles = len(habitaciones.filtered(lambda h: h.estado == 'disponible'))
            record.habitaciones_ocupadas = len(habitaciones.filtered(lambda h: h.estado == 'ocupada'))
            if record.habitaciones_totales > 0:
                record.porcentaje_ocupacion = (record.habitaciones_ocupadas / record.habitaciones_totales) * 100
            else:
                record.porcentaje_ocupacion = 0

    @api.depends('tipo_habitacion')
    def _compute_reservas(self):
        for record in self:
            reservas = self.env['casa_rural.reserva'].search([])
            habitaciones_ocupadas = self.env['casa_rural.habitacion'].search([('tipo', '=', record.tipo_habitacion), ('estado', '=', 'ocupada')])
            record.reservas_activas = len(reservas.filtered(lambda r: any(habitacion in habitaciones_ocupadas for estancia in r.estancias_ids for habitacion in estancia.habitacion_ids)))