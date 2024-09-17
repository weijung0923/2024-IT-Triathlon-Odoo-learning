{
    'name': 'My Custom Theme',
    'description': 'Custom theme for website with custom header.',
    'version': '1.0',
    'category': 'Theme/Website',
    'depends': ['website'],  # 依賴網站模組
    'data': [
        'views/layout.xml',  # 繼承 layout 視圖
        'views/header.xml',  # 自定義的 header 視圖
        'views/content.xml',  # 加載頁面主體內容
        'views/footer.xml' # 加入footer
    ],
    'installable': True,
    'application': False,
}
