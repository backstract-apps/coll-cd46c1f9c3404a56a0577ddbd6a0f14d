from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

import requests

from pathlib import Path


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def get_users(db: Session):

    class_name = aliased(models.Class1)
    query = db.query(models.Users, class_name)

    query = query.join(class_name)

    users_all = query.all()
    users_all = (
        [
            {
                "users_all_1": s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__,
                "users_all_2": s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__,
            }
            for s1, s2 in users_all
        ]
        if users_all
        else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_info: str = raw_data.contact_info
    created_at: str = raw_data.created_at

    record_to_be_added = {
        "id": id,
        "name": name,
        "created_at": created_at,
        "contact_info": contact_info,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()

    res = {
        "users_deleted": users_deleted,
    }
    return res


async def put_users_id(
    db: Session, id: int, name: str, contact_info: str, created_at: str
):

    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()


if users_edited_record is None:
    users_edited_record = None
else:
    for key, value in update_data.items():
        setattr(users_edited_record, key, value)

    db.commit()
    db.refresh(users_edited_record)

    users_edited_record = (
        users_edited_record.to_dict()
        if hasattr(users_edited_record, "to_dict")
        else vars(users_edited_record)
    )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res
