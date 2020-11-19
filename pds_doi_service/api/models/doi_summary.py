# coding: utf-8

from __future__ import absolute_import
from datetime import datetime  # noqa: F401

from pds_doi_service.api.models import Model
from pds_doi_service.api import util


class DoiSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, doi: str = None, lidvid: str = None,
                 submitter: str = None, status: str = None,
                 creation_date: datetime = None, update_date: datetime = None):  # noqa: E501
        """DoiSummary - a model defined in Swagger

        :param doi: The doi of this DoiSummary.  # noqa: E501
        :type doi: str
        :param lidvid: The lidvid of this DoiSummary.  # noqa: E501
        :type lidvid: str
        :param submitter: The submitter of this DoiSummary.  # noqa: E501
        :type submitter: str
        :param status: The status of this DoiSummary.  # noqa: E501
        :type status: str
        :param creation_date: The creation_date of this DoiSummary.  # noqa: E501
        :type creation_date: datetime
        :param update_date: The update_date of this DoiSummary.  # noqa: E501
        :type update_date: datetime
        """
        self.swagger_types = {
            'doi': str,
            'lidvid': str,
            'submitter': str,
            'status': str,
            'creation_date': datetime,
            'update_date': datetime
        }

        self.attribute_map = {
            'doi': 'doi',
            'lidvid': 'lidvid',
            'submitter': 'submitter',
            'status': 'status',
            'creation_date': 'creation_date',
            'update_date': 'update_date'
        }
        self._doi = doi
        self._lidvid = lidvid
        self._submitter = submitter
        self._status = status
        self._creation_date = creation_date
        self._update_date = update_date

    @classmethod
    def from_dict(cls, dikt) -> 'DoiSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The doi_summary of this DoiSummary.  # noqa: E501
        :rtype: DoiSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def doi(self) -> str:
        """Gets the doi of this DoiSummary.


        :return: The doi of this DoiSummary.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi: str):
        """Sets the doi of this DoiSummary.


        :param doi: The doi of this DoiSummary.
        :type doi: str
        """

        self._doi = doi

    @property
    def lidvid(self) -> str:
        """Gets the lidvid of this DoiSummary.


        :return: The lidvid of this DoiSummary.
        :rtype: str
        """
        return self._lidvid

    @lidvid.setter
    def lidvid(self, lidvid: str):
        """Sets the lidvid of this DoiSummary.


        :param lidvid: The lidvid of this DoiSummary.
        :type lidvid: str
        """

        self._lidvid = lidvid

    @property
    def submitter(self) -> str:
        """Gets the submitter of this DoiSummary.


        :return: The submitter of this DoiSummary.
        :rtype: str
        """
        return self._submitter

    @submitter.setter
    def submitter(self, submitter: str):
        """Sets the submitter of this DoiSummary.


        :param submitter: The submitter of this DoiSummary.
        :type submitter: str
        """

        self._submitter = submitter

    @property
    def status(self) -> str:
        """Gets the status of this DoiSummary.


        :return: The status of this DoiSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this DoiSummary.


        :param status: The status of this DoiSummary.
        :type status: str
        """

        self._status = status

    @property
    def creation_date(self) -> datetime:
        """Gets the creation_date of this DoiSummary.


        :return: The creation_date of this DoiSummary.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date: datetime):
        """Sets the creation_date of this DoiSummary.


        :param creation_date: The creation_date of this DoiSummary.
        :type creation_date: datetime
        """

        self._creation_date = creation_date

    @property
    def update_date(self) -> datetime:
        """Gets the update_date of this DoiSummary.


        :return: The update_date of this DoiSummary.
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date: datetime):
        """Sets the update_date of this DoiSummary.


        :param update_date: The update_date of this DoiSummary.
        :type update_date: datetime
        """

        self._update_date = update_date