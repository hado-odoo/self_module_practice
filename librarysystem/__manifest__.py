{
    'name': "librarysystem",
    'version': '0.1.0',
    'author': "hado",
    'category': 'Library Systeam',
    'description': """

    """,
    # data files always loaded at installation
    'data': [ 
            'security/ir.model.access.csv',
            'views/books_view.xml',
            'views/book_tags_view.xml',
            'views/book_author_view.xml',
            'views/book_issue_view.xml',
            'views/library_menus.xml'
    ],
    'depends':[],

    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}