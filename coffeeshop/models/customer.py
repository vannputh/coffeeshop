from odoo import _, api, fields, models

class Customer(models.Model):
    _name = 'customer.coffeeshop'
    _description = 'Customer'

    customer_id = fields.Char(string='Customer ID', required=True)
    name = fields.Char(string='Name', required=True)
    contact_info = fields.Char(string='Contact Info')
    purchase_history = fields.Char(string='Purchase History')
    loyalty_points = fields.Integer(string='Loyalty Points')
    rewards = fields.One2many('rewards.coffeeshop', 'customer_id', string='Rewards')
