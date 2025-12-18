from odoo import models, fields, api

class VehicleUsage(models.Model):
    _name = 'fleet_monitoring.vehicle.usage'
    _description = 'Vehicle Usage Request'
    
    name = fields.Char(string='Reference Title', required=True, copy=False)

    applicant_id = fields.Many2one(
        'hr.employee', 
        string="Nama Pemohon", 
        required=True
    )
    department_id = fields.Many2one(
        'hr.department', 
        string="Unit/Departemen", 
        related="applicant_id.department_id", 
        store=True,
        readonly=True
    )
    job_title = fields.Char(
        string="Jabatan", 
        related="applicant_id.job_title",
        readonly=True
    )
    request_date = fields.Date(
        string="Tanggal Pengajuan", 
        default=fields.Date.context_today
    )
    usage_date = fields.Date(
        string="Tanggal Pemakaian", 
        required=True
    )
    vehicle_id = fields.Many2one(
        'fleet.vehicle', 
        string="Nopol Kendaraan", 
        required=True
    )
    vehicle_type = fields.Char(
        string="Jenis Kendaraan/Merk", 
        related="vehicle_id.model_id.name", 
        store=True,
        readonly=True
    )
    start_time = fields.Float(string="Waktu Keberangkatan")
    end_time = fields.Float(string="Waktu Kembali")
    destination = fields.Text(string="Tujuan Perjalanan")