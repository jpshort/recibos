#-*- coding: utf-8 -*-

from odoo import models,fields,api

class Payment(models.Model):
    _name    = "account.payment" 
    _inherit = "account.payment"

    concepto       = fields.Text()
    anexo          = fields.Char(string="Documentacion Anexa")
    rubro          = fields.Char(string="Rubro del Presupuesto")
    evento         = fields.Char(string="Evento o Actividad a cargar")
    solicitante    = fields.Char()
    autorizado_por = fields.Char()
