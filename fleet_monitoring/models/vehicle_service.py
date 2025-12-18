from odoo import models, fields

class VehicleService(models.Model):
    _name = 'fleet_monitoring.vehicle.service'
    _description = 'Vehicle Service Monitoring'
    _rec_name = 'vehicle_id'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Nopol", required=True)
    
    vehicle_model_id = fields.Many2one(related='vehicle_id.model_id', string="Jenis Kendaraan", 
                                       store=True, readonly=True)

    pengguna = fields.Char(related='vehicle_id.user', string="Pengguna", 
                           store=True, readonly=True) 
    
    vehicle_year = fields.Char(related='vehicle_id.year', string="Tahun", 
                               store=True, readonly=True)
  
    rute = fields.Char(string="Rute") 

    pra_no = fields.Char(string="No. PRA")
    spk_date = fields.Date(string="Tgl SPK")
    spk_no = fields.Char(string="No. SPK")
    description = fields.Text(string="Keterangan Service")
    service_date = fields.Date(string="Tgl Service", default=fields.Date.context_today)

    vendor_id = fields.Many2one('res.partner', string="Vendor") 

    odometer = fields.Float(string="KM Service")
    cost = fields.Float(string="B. Service")
    next_odometer = fields.Float(string="KM Service Selanjutnya")