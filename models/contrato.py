class Contrato(models.Model):
    _name = 'casa_rural.contrato'
    _description = 'Contratos: Acuerdos contractuales con proveedores'

    proveedor_id = fields.Many2one('casa_rural.proveedor', string='Proveedor', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_fin = fields.Date(string='Fecha de Fin')
    terminos = fields.Text(string='Términos')