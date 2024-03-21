from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Item Inventory",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_items_details', response_model=list[schema.Item])
def retrieve_all_items_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items


@app.post('/add_new_item', response_model=schema.ItemAdd)
def add_new_item(item: schema.ItemAdd, db: Session = Depends(get_db)):
    # print("STARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTttt")
    the_item = crud.get_item_by_name(db=db, _item_name=item.item_name)
    # print("STARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTttt")
    if the_item:
        # print("ifffffffffffSTARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTttt")
        item.quantity += the_item.quantity
        # print(item.item_name)
        # print(item.category)
        # print(item.seller)
        # print(the_item.id)
        # print(item.quantity)
        return crud.update_item_details(db=db, details=item, sl_id=the_item.id)
    else:
        # print("elseeeeeeeeeSTARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTttt")
        return crud.add_item_details_to_db(db=db, item=item)


@app.delete('/reduce_item_by_id')
def delete_item_by_id(sl_id: int, r_quantity:int = -1, db: Session = Depends(get_db)):
    details = crud.get_item_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")
    
    print(details.item_name)
    print(details.category)
    print(details.seller)
    print(f"r_quantity: {r_quantity}")
    print(details.quantity)

    if details.quantity-r_quantity<0:
        raise HTTPException(status_code=150, detail=f"Don't have enough quantity in stock")
    elif r_quantity==-1 or details.quantity-r_quantity==0:
        try:
            crud.delete_item_details_by_id(db=db, sl_id=sl_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    else:
        details.quantity -= r_quantity
        _itemadd_ = schema.ItemAdd(
            item_name=details.item_name,
            seller=details.seller,
            category=details.category,
            quantity=details.quantity
        )
        __temp__ = crud.update_item_details(db=db, details=_itemadd_, sl_id=details.id)
    return {"delete status": "success"}


@app.put('/update_item_details', response_model=schema.Item)
def update_item_details(sl_id: int, update_param: schema.Item, db: Session = Depends(get_db)):
    details = crud.get_item_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_item_details(db=db, details=update_param, sl_id=sl_id)