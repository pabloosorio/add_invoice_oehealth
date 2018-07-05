from odoo import api, fields, models, _

class OeHealthInherithPayment(models.Model):
    _inherit = 'account.payment'
    _description = 'Anexo a pagos'


    expediente = fields.Char(string='Expediente', compute="_get_expediente")

    @api.one
    @api.depends('partner_id','expediente')
    def _get_expediente(self):
        cr = self.env.cr
        pid = self.partner_id.id
        sql = "select identification_code from oeh_medical_patient where partner_id='"+str(pid)+"'"
        cr.execute(sql)
        id_returned = cr.fetchone()
        for t in id_returned:
            self.expediente = str(t)

class OeHealthInherithPayment(models.Model):
    _inherit = 'account.invoice'
    _description = 'Anexo a facturas'


    expediente = fields.Char(string='Expediente', compute="_get_expediente")

    @api.one
    @api.depends('partner_id','expediente')
    def _get_expediente(self):
        cr = self.env.cr
        pid = self.partner_id.id
        sql = "select identification_code from oeh_medical_patient where partner_id='"+str(pid)+"'"
        cr.execute(sql)
        id_returned = cr.fetchone()
        for t in id_returned:
            self.expediente = str(t)