routes:-
- "/retrieve_all_items_details": To fetch a list of all items.\
        Parameters: skip, limit.
- "/add_new_item": To add a new item.\
        Parameters: item(item_name, seller, category, quantity).
- "/reduce_item_by_id": To reduce the quantity of any item in inventory.\
        Parameters: r_quantity(Amount by which quantity is reduced),sl_id(pK of item).
- "/update_item_details": To update the item.\
        Parameters:update_param(item_name, seller, category, quantity),sl_id(pK of item).
