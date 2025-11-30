from odoo import models, fields

class VehicleDocument(models.Model):
    _name = 'fleet_monitoring.vehicle.document'
    _description = 'Vehicle Document Monitoring'
    _rec_name = 'vehicle_id'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Nopol", required=True)
    
    vehicle_model_id = fields.Many2one(related='vehicle_id.model_id', string="Jenis Kendaraan", store=True)
    vehicle_user_id = fields.Char(related='vehicle_id.user', string="Pengguna", store=True)
    vehicle_year = fields.Char(related='vehicle_id.year', string="Tahun", store=True)

    # Asuransi
    insurance_name = fields.Char(string="Nama Asuransi")
    insurance_period = fields.Char(string="Periode")
    insurance_premium = fields.Float(string="Premi")
    insurance_premium_final = fields.Float(string="Premi Akhir")

    # Pajak
    tax_due_date = fields.Date(string="Tgl. JT Pajak Tahunan")
    tax_paid_date = fields.Date(string="Tgl. Bayar Pajak Tahunan")
    tax_amount = fields.Float(string="Nominal")
    
    # Ganti Plat
    plate_due_date = fields.Date(string="Tgl JT Ganti Plat")
    plate_paid_date = fields.Date(string="Tgl. Bayar Ganti Plat")

    keur_date = fields.Date(string="Keur Kendaraan")
    notes = fields.Text(string="Keterangan")