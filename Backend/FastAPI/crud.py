from sqlalchemy.orm import Session
import model
import schema



def get_item_by_id(db: Session, sl_id: int):
    return db.query(model.Items).filter(model.Items.id == sl_id).first()

def get_item_by_name(db: Session, _item_name: str):
    return db.query(model.Items).filter(model.Items.item_name == _item_name).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Items).offset(skip).limit(limit).all()


def add_item_details_to_db(db: Session, item: schema.ItemAdd):
    item_details = model.Items(
        item_name=item.item_name,
        seller=item.seller,
        category=item.category,
        quantity=item.quantity
    )
    # print("DB not SETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    db.add(item_details)
    db.commit()
    db.refresh(item_details)
    # print("DB ALL SETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    return model.Items(**item.dict())


def update_item_details(db: Session, sl_id: int, details: schema.Item):
    db.query(model.Items).filter(model.Items.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Items).filter(model.Items.id == sl_id).first()


def delete_item_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Items).filter(model.Items.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)