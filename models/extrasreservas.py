class CasaRuralExtrasReservas(models.Model):
    _name = 'casa_rural.extras_reservas'
    _description = 'Extras Reservas: Extras añadidos a cada reserva con cantidad y precio total'

    reserva_id = fields.Many2one('casa_rural.reserva', string='Reserva', required=True)
    extra_id = fields.Many2one('casa_rural.extra', string='Extra', required=True)
    cantidad = fields.Integer(string='Cantidad')
    precio_total = fields.Float(string='Precio Total')