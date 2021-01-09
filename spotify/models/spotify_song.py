from odoo import fields, models, api


class SpotifySong(models.Model):
    _name = 'spotify.song'
    _description = 'Description'

    id_track = fields.Char()
    name = fields.Char()
    url = fields.Char()
    artist = fields.Char()

    _sql_constraints = [('unique_id_track', 'unique (id_track)', 'Name gender already exists!')]
