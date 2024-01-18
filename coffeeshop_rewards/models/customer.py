from odoo import _, api, fields, models
class Customer(models.Model):
    _name = 'customer.coffeeshop'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    contact_information = fields.Char(string='Contact Information')
    purchase_history = fields.Text(string='Purchase History')
    loyalty_points = fields.Integer(string='Loyalty Points', default=0)
    reward_status = fields.Selection([
        ('eligible', 'Eligible'),
        ('redeemable', 'Redeemable'),
        ('granted', 'Granted'),
        ('rejected', 'Rejected'),
    ], string='Reward Status', default='eligible')