#-*- coding: utf-8 -*-

from odoo import models,fields,api
import number_to_word

class Payment(models.Model):
    _name    = "account.payment" 
    _inherit = "account.payment"

    numerocheque  = fields.Char(string="Cheque No.")
    banco         = fields.Selection([('popular','Banco Popular Dominicano'),
                                      ('reservas','BanReservas'),
                                      ('bhd','Banco BHD Leon'),
                                      ('scotiabank','Scotia Bank'),
                                      ('caribe','Banco Caribe'),
                                      ('scotiabank','Scotia Bank'),
                                      ('santacruz','Banco Santa Cruz'),
                                      ('ademi','Banco ADEMI'),
                                      ('lopezdeharo','Banco Lopez de Haro'),
                                      ('bellbank','Banco Bell Bank'),
                                      ('banesco','Banco Banesto'),
                                      ('promerica','Banco Proamerica'),
                                      ('progreso','Banco del Progreso')])
 

   
