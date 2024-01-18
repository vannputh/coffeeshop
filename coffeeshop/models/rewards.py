from odoo import _, api, fields, models

class Rewards(models.Model):
    _name = 'rewards.coffeeshop'
    _description = 'Rewards'

    reward_id = fields.Char(string='Reward ID', required=True)
    customer_id = fields.Char(string='Customer ID', required=True)
    application_status = fields.Char(string='Application Status', required=True)