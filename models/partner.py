#-*- coding: utf-8-*-

from odoo import models,fields,api

class Partner(models.Model):
    _inherit = 'res.partner'

    solicitante = fields.Boolean("Solicitante",default=False)
    autorizador = fields.Boolean("Autorizador",default=False)
