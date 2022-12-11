from ..settings import BASE_DIR, TEMPLATES


# Update TEMPLATES by ref
template_path_list = []
template_path_list = TEMPLATES[0]['DIRS']
template_path_list.append(BASE_DIR / 'templates')
# template_path_list.append(BASE_DIR / 'users' / 'templates' )
# template_path_list.append(BASE_DIR / 'organization' / 'templates'  )
template_path_list.append(BASE_DIR / 'corpus' / 'templates'  )