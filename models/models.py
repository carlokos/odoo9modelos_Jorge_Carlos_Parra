# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class biblioteca(models.Model):
#     _name = 'biblioteca.biblioteca'
#     _description = 'biblioteca.biblioteca'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'model libro'

    name = fields.Char('ID', required=True)
    titulo = fields.Char(string='Titulo', required=True)

    autor_id = fields.Many2many('biblioteca.autor', 'autor_id', string='Id del autor')
    editorial_id = fields.Many2one('biblioteca.editorial', string='Id de la editorial')
    genero_id = fields.Many2many('biblioteca.genero', 'genero_id', string='Id del genero')

class autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'model autor'

    name = fields.Char('ID', required=True)
    nombre = fields.Char(string='Nombre', required=True)

class editorial(models.Model):
    _name = 'biblioteca.editorial'
    _description = 'model editorial'

    name = fields.Char('ID', required=True)
    nombre = fields.Char(string='Nombre', required=True)

class genero(models.Model):
    _name = 'biblioteca.genero'
    _description = 'model genero'

    name = fields.Char('ID', required=True)
    nombre = fields.Char(string='Genero', required=True)

class persona(models.Model):
    _name = 'biblioteca.persona'
    _description = 'model persona'

    name = fields.Char('DNI', required=True)
    nombre = fields.Char(string='Nombre completo', required=True)
    fnacimiento = fields.Date(string='Fecha de nacimiento', required=True)

    tarjeta_id = fields.One2many('biblioteca.tarjeta', 'persona_id', string='Id de la tarjeta')
    cliente_id = fields.Many2one('biblioteca.cliente', string='Id del cliente')
    empleado_id = fields.Many2one('biblioteca.empleado', string='Id del empleado')


class cliente(models.Model):
    _name = 'biblioteca.cliente'
    _description = 'model cliente'

    name = fields.Char('ID', required=True)
    nombre = fields.Char(string='Nombre', required=True)

    persona_id = fields.One2many('biblioteca.persona', 'cliente_id', string='DNI de la persona')


class empleado(models.Model):
    _name = 'biblioteca.empleado'
    _description = 'model empleado'

    name = fields.Char('ID', required=True)
    nombre = fields.Char(string='Nombre', required=True)

    persona_id = fields.One2many('biblioteca.persona', 'empleado_id', string='DNI de la persona')


class prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'model prestamo'

    name = fields.Char('ID', required=True)
    fdevolucion = fields.Date(string='Fecha de devolucion', required=True)

    libro_id = fields.Many2many('biblioteca.libro', 'libro_id', string="id del libro")

class tarjeta(models.Model):
    _name = 'biblioteca.tarjeta'
    _description = 'model tarjeta'

    name = fields.Char('ID', required=True)
    fcaducidad = fields.Date(string='Fecha de caducidad', required=True)
    
    persona_id = fields.Many2one('biblioteca.persona', string='Id de la persona')








