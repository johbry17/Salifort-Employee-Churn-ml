'''Script to inject metadata (title, description, author, favicon) into multiple HTML files.'''

from bs4 import BeautifulSoup

# List of dicts: one per HTML file
files_metadata = [
    {
        'filepath': './index.html',
        'title': 'Classified: At Risk — Salifort Motors Employee Attrition Prediction',
        'description': 'Executive summary of the Salifort employee churn project. Key findings, business insights, and model performance for stakeholder review.',
        'author': 'Bryan C. Johns',
        'favicon': './static/images/favicon.ico'
    },
    {
        'filepath': './notebooks/eda.html',
        'title': 'Exploratory Data Analysis — Salifort Employee Churn',
        'description': 'Exploratory data analysis for Salifort employee churn project.',
        'author': 'Bryan C. Johns',
        'favicon': '../static/images/favicon.ico'
    },
    {
        'filepath': './notebooks/models.html',
        'title': 'Model Construction & Validation — Salifort Employee Churn',
        'description': 'Model construction and validation for Salifort employee churn project.',
        'author': 'Bryan C. Johns',
        'favicon': '../static/images/favicon.ico'
    },
    {
        'filepath': './notebooks/initial_work.html',
        'title': 'Reference: Model Development — Salifort Employee Churn',
        'description': 'Reference notebook for model development in Salifort employee churn project.',
        'author': 'Bryan C. Johns',
        'favicon': '../static/images/favicon.ico'
    },
]

# Loop through each file and inject metadata
for meta in files_metadata:
    fn = meta['filepath']
    html = open(fn, 'r', encoding='utf8').read()
    soup = BeautifulSoup(html, 'html.parser')
    if soup.head is None:
        soup.html.insert(0, soup.new_tag('head'))

    # Insert/replace title
    if soup.head.title:
        soup.head.title.string = meta['title']
    else:
        t = soup.new_tag('title')
        t.string = meta['title']
        soup.head.insert(0, t)

    # Add description and author meta tags (ensure only single instance)
    for name in ('description', 'author'):
        tag = soup.head.find('meta', attrs={'name': name})
        if tag:
            tag['content'] = meta[name]
        else:
            tag = soup.new_tag('meta', attrs={'name': name, 'content': meta[name]})
            soup.head.append(tag)

    # Add favicon
    link = soup.head.find('link', rel='icon')
    if link:
        link['href'] = meta['favicon']
    else:
        link_tag = soup.new_tag('link', attrs={'rel': 'icon', 'href': meta['favicon'], 'type': "image/x-icon"})
        soup.head.append(link_tag)

    open(fn, 'w', encoding='utf8').write(str(soup))
    print('Wrote', fn)