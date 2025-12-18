from odoo import models, fields

class VehicleChecklistCar(models.Model):
    _name = 'fleet_monitoring.checklist.car'
    _description = 'Driver (Car) Checklist'

    name = fields.Char(string="Checklist Title", required=True)
    
    driver_id = fields.Many2one('hr.employee', string="Nama Sopir/Pengguna")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Nomor Polisi") 
    date = fields.Date(string="Tanggal", default=fields.Date.context_today)

    # A. Pemeriksaan Eksterior & Mesin 
    body = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Body Kendaraan (tidak penyok/lecet)")
    tires = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Ban (tekanan & keausan)")
    spare_tire = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Ban Cadangan")
    lights_head = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Lampu Depan & Belakang")
    lights_brake = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Lampu Rem & Sein")
    wiper = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Wiper & Washer (air semprot)")
    horn = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Klakson")
    engine_oil = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Oli Mesin")
    radiator_water = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Air Radiator")
    accu = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Aki")
    safety_belt = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Sabuk Pengaman")
    windshield = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Kaca Depan & Spion (tidak retak)")
    brake = fields.Selection([('layak','Layak'), ('tidak_layak','Tidak Layak')], string="Rem")

    # B. Perlengkapan Wajib 
    stnk = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="Pajak STNK, STNK depan")
    kir = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="KIR (Jika ada)")
    triangle = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="Segitiga Pengaman")
    first_aid = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="Kotak P3K")
    jack = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="Dongkrak & Kunci Roda")
    fire_extinguisher = fields.Selection([('ada','Ada'), ('tidak_ada','Tidak Ada')], string="APAR (jika diwajibkan)")

    # C. Catatan Tambahan 
    notes = fields.Text(string="Catatan Tambahan / Masalah yang Ditemukan")

    # D. Pernyataan Sopir 
    is_roadworthy = fields.Selection([
        ('yes', 'Layak Jalan'),
        ('no', 'Tidak Layak Jalan (beri catatan di atas)')
    ], string="Kondisi Kendaraan", required=True)