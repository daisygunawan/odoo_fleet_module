from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_fleet_service = fields.Boolean(string="Is Fleet Service", default=False)

    vehicle_id = fields.Many2one('fleet.vehicle', string="Kendaraan")
  
    vehicle_type = fields.Many2one(related='vehicle_id.model_id', string="Jenis Kendaraan", readonly=True)
    vehicle_year = fields.Char(related='vehicle_id.year', string="Tahun", readonly=True)
    
    driver_id = fields.Many2one('hr.employee', string="Sopir")
    
    rute = fields.Char(string="Rute")
    
    spk_no = fields.Char(string="No. SPK")
    spk_date = fields.Date(string="Tgl SPK")
    pra_no = fields.Char(string="No. PRA")
   
    odometer = fields.Float(string="KM Saat Ini")
    next_odometer = fields.Float(string="KM Selanjutnya")
    
    cost = fields.Float(string="Biaya / Cost")