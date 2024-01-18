from odoo import _, api, fields, models
class Rewards(models.Model):
    _name = 'rewards.coffeeshop'
    _description = 'Rewards'

    customer_id = fields.Many2one('coffee_shop.customer', string='Customer', required=True)
    application_status = fields.Selection([
        ('applied', 'Applied'),
        ('granted', 'Granted'),
        ('rejected', 'Rejected'),
    ], string='Application Status', default='applied')