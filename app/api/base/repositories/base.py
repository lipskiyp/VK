"""
Base SQLAlchemy data repository.
"""

from sqlalchemy import Select, ScalarResult
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, TypeVar, List, Any, Optional


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepo:
    """
    Base data repository.
    """

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session


    async def get_by(
        self, _filter_by: dict[str, Any]
    ) -> Optional[ModelType]:
        """
        Get a model object by a field.
        """
        query = self._query()
        query = self._filter(query, _filter_by)
        return await self._one_or_none(query)


    async def list_by(
        self, _filter_by: dict[str, Any], _order_by: dict = Optional[None]
    ) -> List[ModelType]:
        """
        List model objects.
        """
        query = self._query(_order_by)
        query = self._filter(query, _filter_by)
        return await self._all(query)


    def _query(
        self, _order_by: dict = Optional[None]
    ) -> Select:
        """
        Returns base query with optional order by filter and join.
        """
        query = select(self.model)
        query = self._order(query, _order_by)
        return query


    def _filter(
        self, query: Select, _filter_by: dict[str, Any]
    ) -> Select:
        """
        Applies filters and returns query.
        """
        for field, value in _filter_by.items():
            query = query.filter(getattr(self.model, field) == value)
        return query


    def _order(
        self, query: Select, _order_by: dict[str, str] = Optional[None]
    ) -> Select:
        """
        Applies optional order by filter and returns query.
        """
        if not query:
            return query

        for field, order in _order_by.items():
            if order == "asc":
                query = query.order_by(getattr(self.model, field).asc())
            elif order == "dsc":
                query = query.order_by(getattr(self.model, field).desc())
            else:
                query = query.order_by(getattr(self.model, field))
        return query


    async def _all(
        self, query: Select
    ) -> List[ModelType]:
        """
        Returns list of all model objects.
        """
        res = await self._scalars(query)
        return res.all()


    async def _one_or_none(
        self, query: Select
    ) -> Optional[ModelType]:
        """
        Returns model object or None.
        """
        res = await self._scalars(query)
        return res.one_or_none()


    async def _scalars(
        self, query: Select
    ) -> ScalarResult:
        """
        Executes and returns query.
        """
        return await self.session.scalars(query)
