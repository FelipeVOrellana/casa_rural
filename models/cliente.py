class ClientesCom(models.Model):
    _name = 'casa_rural.clientes_com'
    _description = 'Clientes Com: Datos de clientes para la comunicación'

    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Char(string='Dirección')
    mensaje_ids = fields.One2many('casa_rural.mensaje', 'cliente_id', string='Mensajes')