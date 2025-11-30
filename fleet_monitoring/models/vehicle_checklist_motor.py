from odoo import models, fields

class VehicleChecklistMotor(models.Model):
    _name = 'fleet_monitoring.checklist.motor'
    _description = 'Motorcycle Checklist'

    name = fields.Char(string="Checklist Title", required=True)
    
    driver_id = fields.Many2one('hr.employee', string="Nama Pengguna")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Nomor Polisi") 
    date = fields.Date(string="Tanggal", default=fields.Date.context_today)

    # A. Pemeriksaan Teknis 
    oil = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Oli Mesin")
    fuel = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Bahan Bakar Cukup")
    brakes = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Rem Depan & Belakang (berfungsi)")
    light_front = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Lampu Depan (dekat/jauh)")
    light_back = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Lampu Belakang & Lampu Rem")
    light_head = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Lampu Sein (kiri/kanan)")
    horn = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Klakson")
    wheels = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Ban Depan & Belakang (tekanan & kondisi)")
    chain = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Rantai/Driver Belt")
    mirror = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Spion Lengkap & Utuh")
    box_key = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Kunci Kotak Berfungsi Baik")
    stand = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Standar Samping & Tengah (berfungsi)")
    starter = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Kick Starter/Electric Starter")

     # B. Kelengkapan dan Dokumen    
    stnk_tax = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="Pajak STNK")
    stnk = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="STNK Depan")

    # C. Catatan Tambahan 
    notes = fields.Text(string="Catatan Tambahan / Masalah yang Ditemukan")

    # D. Pernyataan Sopir 
    is_roadworthy = fields.Selection([
        ('yes', 'Layak Jalan'),
        ('no', 'Tidak Layak Jalan (beri catatan di atas)')
    ], string="Kondisi Kendaraan", required=True)