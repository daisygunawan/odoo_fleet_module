# -*- coding: utf-8 -*-
{
    'name': "Fleet Monitoring",
    'summary': """
        A new module to manage vehicle checklists, usage requests,
        service monitoring, and document monitoring.""",
    'description': """
        - Vehicle Driver Checklists (Car & Motor)
        - Vehicle Usage/Booking Forms
        - Vehicle Service Monitoring
        - Vehicle Document (Tax, Insurance) Monitoring
    """,
    'author': "Daisy Gunawan",
    'category': 'Operations/Fleet',
    'version': '17.0.1.0.0',
    
    'depends': [
        'base',
        'fleet',  # Dependency for linking to fleet.vehicle
        'hr'      # Dependency for linking to hr.employee
    ],

   'data': [
        'security/ir.model.access.csv',
        'views/vehicle_checklist_car_views.xml',    
        'views/vehicle_checklist_motor_views.xml',  
        'views/vehicle_usage_views.xml',
        'views/vehicle_service_views.xml',
        'views/vehicle_document_views.xml',
        'views/menus.xml',  
    ],
    'installable': True,
    'application': True,
    'web_icon': 'fleet_monitoring,static/description/icon.png',
    'license': 'LGPL-3',
}