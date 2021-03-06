# coding: utf-8

from __future__ import absolute_import
from datetime import datetime  # noqa: F401

from pds_doi_service.api.models import Model
from pds_doi_service.api import util


class DoiSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, doi: str = None, lidvid: str = None, title: str = None,
                 node: str = None, submitter: str = None, status: str = None,
                 update_date: datetime = None):  # noqa: E501
        """DoiSummary - a model defined in Swagger

        :param doi: The doi of this DoiSummary.  # noqa: E501
        :type doi: str
        :param lidvid: The lidvid of this DoiSummary.  # noqa: E501
        :type lidvid: str
        :param title: The title of this DoiRecord.  # noqa: E501
        :type title: str
        :param node: The node of this DoiSummary.  # noqa: E501
        :type node: str
        :param submitter: The submitter of this DoiSummary.  # noqa: E501
        :type submitter: str
        :param status: The status of this DoiSummary.  # noqa: E501
        :type status: str
        :param update_date: The update_date of this DoiSummary.  # noqa: E501
        :type update_date: datetime
        """
        self.swagger_types = {
            'doi': str,
            'lidvid': str,
            'title': str,
            'node': str,
            'submitter': str,
            'status': str,
            'update_date': datetime
        }

        self.attribute_map = {
            'doi': 'doi',
            'lidvid': 'lidvid',
            'title': 'title',
            'node': 'node',
            'submitter': 'submitter',
            'status': 'status',
            'update_date': 'update_date'
        }
        self._doi = doi
        self._lidvid = lidvid
        self._title = title
        self._node = node
        self._submitter = submitter
        self._status = status
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
    def title(self) -> str:
        """Gets the title of this DoiSummary.


        :return: The title of this DoiSummary.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this DoiSummary.


        :param title: The title of this DoiSummary.
        :type title: str
        """

        self._title = title

    @property
    def node(self) -> str:
        """Gets the node of this DoiSummary.


        :return: The node of this DoiSummary.
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node: str):
        """Sets the node of this DoiSummary.


        :param node: The node of this DoiSummary.
        :type node: str
        """

        self._node = node

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
