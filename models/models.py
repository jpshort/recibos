#-*- coding: utf-8 -*-

from odoo import models,fields,api
import number_to_word

class account_register_payments(models.TransientModel):
    _inherit = "account.register.payments"

    @api.onchange('amount')
    def _onchange_amount(self):
        self.check_amount_in_words = number_to_word.to_word(self.amount, self.currency_id.name)


class Payment(models.Model):
    _name    = "account.payment" 
    _inherit = "account.payment"

    concepto       = fields.Text()
    anexo          = fields.Char(string="Documentacion Anexa")
    rubro          = fields.Char(string="Rubro del Presupuesto")
    evento         = fields.Char(string="Evento o Actividad a cargar")
    solicitante    = fields.Char()
    autorizado_por = fields.Char()
     
    @api.onchange('amount')
    def get_amount_in_word(self):
        self.amount_in_word = number_to_word.to_word(self.amount, self.currency_id.name)
   
    @api.multi
    @api.depends("amount")
    def get_amont_in_word(self):
        for rec in self:
            rec.amont_in_word =  number_to_word.to_word(rec.amount, rec.currency_id.name)
   
    amount_in_word = fields.Char("En letras", compute=get_amount_in_word,store=True)
   
