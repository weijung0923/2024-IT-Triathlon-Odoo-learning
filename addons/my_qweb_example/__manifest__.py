# my_qweb_example/__manifest__.py

{
    'name': 'My QWeb Example',
    'version': '1.0',
    'summary': 'A simple example of using QWeb without HTML',
    'author': 'Your Name',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'views/my_qweb_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
