{
    "name": "Stock Bin",
    "summary": "Add bin per warehouse in product template form",
    "version": "14.0.1.0.0",
    "category": "Stock",
    "website": "accioma.com",
    "author": "Accioma",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_bin_views.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
