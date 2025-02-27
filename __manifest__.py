{
    'name': 'Casa Rural',
    'version': '1.0',
    'summary': 'Gestión de una casa rural en Odoo 18',
    'description': 'Módulo para gestionar huéspedes, estancias, facturación, habitaciones y más.',
    'category': 'Hospitality',
    'author': 'Tu Nombre',
    'website': 'https://tuweb.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/huesped_views.xml',
        'views/estancia_views.xml',
        'views/factura_views.xml',
        'views/habitacion_views.xml',
        'views/canalcomunicacion_views.xml',
        'views/empleados_views.xml',
        'views/equipos_views.xml',
        'views/extra_views.xml',
        'views/incidencia_views.xml',
        'views/mensaje_views.xml',
        'views/pago_views.xml',
        'views/proveedor_views.xml',
        'views/reserva_views.xml',
        'views/servicio_views.xml',
        'views/tarifa_views.xml',
        'views/tiposervicio_views.xml',
        'views/tareamantenimiento_views.xml'
        ,
    ],
    'installable': True,
    'application': True,
}