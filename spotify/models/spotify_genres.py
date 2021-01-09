from odoo import fields, models, api


class SpotifyGenres(models.Model):
    _name = 'spotify.gender'
    _description = 'Model that stores music genomers according to the spotify database'

    name = fields.Char()

    _sql_constraints = [('unique_name', 'unique (name)', 'Name gender already exists!')]
