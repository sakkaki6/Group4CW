def top_three(shop_dict):

    top_three = sorted(shop_dict.items(),
                       key=lambda item: item[1], reverse=True)[:3]
    print(dict(top_three))


top_three({'T-shirt': 45.50, 'Pants': 35, 'Sneakers': 41.30, 'Hat':
           55, 'Backpack': 24})
