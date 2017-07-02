# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:04:38 2017

@author: Akash
"""

import facebook
token = 'EAACEdEose0cBAAUQvZBvM3WvJ1b5gfX5Rf7NoEdnp0zM50TKtIuPjr5YN6YV2GKFg2Q9JPYd5EIbgrjhKenK2csGWoYK8AtGUllZAwyyT72mgr2P4g6toUgJKVO9J7xmpg77Il20i2zNprsokTz37RHXRoHZC82sthramunP34uAEaZBJWHKBbn4uqt4POUZD'


graph = facebook.GraphAPI(token)


profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print(friend_list)