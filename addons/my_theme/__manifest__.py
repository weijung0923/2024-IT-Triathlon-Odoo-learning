{
    'name': 'My Custom Theme',
    'description': 'Custom theme for website with custom header.',
    'version': '1.0',
    'category': 'Theme/Website',
    'depends': ['website'],  # 依賴網站模組
    'data': [
        'views/layout.xml',  # 繼承 layout 視圖
        'views/header.xml',  # 自定義的 header 視圖
    ],
    'installable': True,
    'application': False,
}
