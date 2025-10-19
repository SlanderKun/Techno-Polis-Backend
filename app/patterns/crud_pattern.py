from typing import List, Type

import database.core
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta


# Асинхронная зависимость для БД
async def get_db():
    async with database.core.async_session_factory() as session:
        yield session


class CRUD_pattern:
    def __init__(
        self,
        router: APIRouter,
        db_model: Type[DeclarativeMeta],
        schema_create: Type[BaseModel],
        schema_read: Type[BaseModel],
        schema_update: Type[BaseModel],
        object_name: str,
    ):
        self.router = router
        self.db_model = db_model
        self.schema_create = schema_create
        self.schema_read = schema_read
        self.object_name = object_name
        self.schema_update = schema_update

        self._register_routes()

    def _register_routes(self):
        router = self.router
        db_model = self.db_model
        schema_create = self.schema_create
        schema_read = self.schema_read
        obj_name = self.object_name
        schema_update = self.schema_update

        # ---------- CREATE ----------
        @router.post(
            f"/{obj_name}/create/", response_model=schema_read, tags=[obj_name]
        )
        async def create_item(
            item: schema_create, db: AsyncSession = Depends(get_db)
        ):
            db_item = db_model(**item.dict())
            db.add(db_item)
            await db.commit()
            await db.refresh(db_item)
            return db_item

        # ---------- READ ALL ----------
        @router.get(
            f"/{obj_name}/list/",
            response_model=List[schema_read],
            tags=[obj_name],
        )
        async def read_items(db: AsyncSession = Depends(get_db)):
            result = await db.execute(select(db_model))
            return result.scalars().all()

        # ---------- READ ONE ----------
        @router.get(
            f"/{obj_name}/read/{{item_id}}",
            response_model=schema_read,
            tags=[obj_name],
        )
        async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
            result = await db.execute(
                select(db_model).where(db_model.id == item_id)
            )
            obj = result.scalar_one_or_none()
            if not obj:
                raise HTTPException(
                    status_code=404,
                    detail=f"{obj_name.capitalize()} not found",
                )
            return obj

        # ---------- UPDATE ----------
        @router.put(
            f"/{obj_name}/update/", response_model=schema_read, tags=[obj_name]
        )
        async def update_item(
            item: schema_update, db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(
                select(db_model).where(db_model.id == item.id)
            )
            db_item = result.scalar_one_or_none()
            if not db_item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{obj_name.capitalize()} not found",
                )

            for key, value in item.dict().items():
                setattr(db_item, key, value)

            await db.commit()
            await db.refresh(db_item)
            return db_item

        # ---------- DELETE ----------
        @router.delete(f"/{obj_name}/delete/{{item_id}}", tags=[obj_name])
        async def delete_item(
            item_id: int, db: AsyncSession = Depends(get_db)
        ):
            result = await db.execute(
                select(db_model).where(db_model.id == item_id)
            )
            db_item = result.scalar_one_or_none()
            if not db_item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{obj_name.capitalize()} not found",
                )

            await db.delete(db_item)
            await db.commit()
            return {"detail": f"{obj_name.capitalize()} deleted"}
