# import fastapi
# from fastapi import APIRouter, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
# from typing import Type
# from pydantic import BaseModel
# from sqlalchemy.orm import DeclarativeMeta
# import database.core


# class CRUD_pattern:
#     def __init__(
#         self,
#         router: APIRouter,
#         db_model: Type[DeclarativeMeta],
#         schema_create: Type[BaseModel],
#         schema_read: Type[BaseModel],
#         schema_update: Type[BaseModel],
#         object_name: str,
#         on_create=None,
#         on_read=None,
#         on_update=None,
#         on_delete=None,
#         get_user=None,
#     ):
#         self.router = router
#         self.db_model = db_model
#         self.schema_create = schema_create
#         self.schema_read = schema_read
#         self.schema_update = schema_update
#         self.object_name = object_name
#         self.on_create = on_create
#         self.on_read = on_read
#         self.on_update = on_update
#         self.on_delete = on_delete
#         self.get_user = get_user
#         self._register_routes()

#     async def _get_object(self, db: AsyncSession, item_id: int):
#         result = await db.execute(
#             select(self.db_model).where(self.db_model.id == item_id)
#         )
#         obj = result.scalar_one_or_none()
#         if not obj:
#             raise HTTPException(
#                 status_code=404,
#                 detail=f"{self.object_name.capitalize()} not found",
#             )
#         return obj

#     def _register_routes(self):
#         router = self.router
#         obj_name = self.object_name
#         schema_create = self.schema_create
#         schema_read = self.schema_read
#         schema_update = self.schema_update
#         db_model = self.db_model

#         # ---------- CREATE ----------
#         @router.post(
#             f"/{obj_name}/create/", response_model=schema_read, tags=[obj_name]
#         )
#         async def create_item(
#             item: schema_create,
#             db: AsyncSession = database.core.async_session_factory(),
#             headers: fastapi.Request = None,
#         ):
#             user = await self.get_user(headers.get("session_token"), db)

#             if self.on_create:
#                 is_valid = await self.on_create(user)
#                 if not is_valid:
#                     raise HTTPException(
#                         status_code=403, detail="Access denied"
#                     )

#             db_item = db_model(**item.dict())
#             db.add(db_item)
#             await db.commit()
#             await db.refresh(db_item)
#             return db_item

#         # ---------- READ ----------
#         @router.get(
#             f"/{obj_name}/read/{{item_id}}",
#             response_model=schema_read,
#             tags=[obj_name],
#         )
#         async def read_item(
#             item_id: int,
#             db: AsyncSession = database.core.async_session_factory(),
#             headers: fastapi.Request = None,
#         ):
#             user = await self.get_user(headers.get("session_token"), db)
#             db_item = await self._get_object(db, item_id)

#             if self.on_read:
#                 is_valid = await self.on_read(db_item, user)
#                 if not is_valid:
#                     raise HTTPException(
#                         status_code=403, detail="Access denied"
#                     )

#             return db_item

#         # ---------- UPDATE ----------
#         @router.put(
#             f"/{obj_name}/update/", response_model=schema_read, tags=[obj_name]
#         )
#         async def update_item(
#             item: schema_update,
#             db: AsyncSession = database.core.async_session_factory(),
#             headers: fastapi.Request = None,
#         ):
#             user = await self.get_user(headers.get("session_token"), db)
#             db_item = await self._get_object(db, item.id)

#             if self.on_update:
#                 is_valid = await self.on_update(db_item, user)
#                 if not is_valid:
#                     raise HTTPException(
#                         status_code=403, detail="Access denied"
#                     )

#             for key, value in item.dict().items():
#                 setattr(db_item, key, value)

#             await db.commit()
#             await db.refresh(db_item)
#             return db_item

#         # ---------- DELETE ----------
#         @router.delete(f"/{obj_name}/delete/{{item_id}}", tags=[obj_name])
#         async def delete_item(
#             item_id: int,
#             db: AsyncSession = database.core.async_session_factory(),
#             headers: fastapi.Request = None,
#         ):
#             user = await self.get_user(headers.get("session_token"), db)
#             db_item = await self._get_object(db, item_id)

#             if self.on_delete:
#                 is_valid = await self.on_delete(db_item, user)
#                 if not is_valid:
#                     raise HTTPException(
#                         status_code=403, detail="Access denied"
#                     )

#             await db.delete(db_item)
#             await db.commit()
#             return {"detail": f"{obj_name.capitalize()} deleted"}
