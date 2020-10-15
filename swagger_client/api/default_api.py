# coding: utf-8

"""
    StreetSpectra API

    API description for StreetSpectra project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: jgcasta@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_new_user(self, **kwargs):  # noqa: E501
        """Create user data  # noqa: E501

        Send user data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_new_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData user_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_new_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_new_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_new_user_with_http_info(self, **kwargs):  # noqa: E501
        """Create user data  # noqa: E501

        Send user data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_new_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData user_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_new_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_data' in params:
            body_params = params['user_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/addNewUserData', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_user_data(self, **kwargs):  # noqa: E501
        """Edit user data  # noqa: E501

        Edit user data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_user_data(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData user_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_user_data_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.edit_user_data_with_http_info(**kwargs)  # noqa: E501
            return data

    def edit_user_data_with_http_info(self, **kwargs):  # noqa: E501
        """Edit user data  # noqa: E501

        Edit user data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_user_data_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData user_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_user_data" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_data' in params:
            body_params = params['user_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/editUserData', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_history_data_post(self, **kwargs):  # noqa: E501
        """Retrieve history data for a user  # noqa: E501

        Retrieve history data for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_history_data_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Login login:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_history_data_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_history_data_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_history_data_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve history data for a user  # noqa: E501

        Retrieve history data for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_history_data_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Login login:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_history_data_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'login' in params:
            body_params = params['login']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/getHistoryData', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_map_distribution_post(self, **kwargs):  # noqa: E501
        """Retrieve map data distribution  # noqa: E501

        Retrieve map data distribution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_distribution_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestMapDistribution get_map_distribution:
        :return: ResponseListSpectra
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_map_distribution_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_map_distribution_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_map_distribution_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve map data distribution  # noqa: E501

        Retrieve map data distribution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_distribution_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestMapDistribution get_map_distribution:
        :return: ResponseListSpectra
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_map_distribution']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_map_distribution_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_map_distribution' in params:
            body_params = params['get_map_distribution']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/getMapDistribution', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseListSpectra',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_spectrum_data_post(self, **kwargs):  # noqa: E501
        """Retrieve data from a single spectrum  # noqa: E501

        Retrieve data from a single spectrum. Image stored as username + ts_gps UNIX time in seconds **jgcasta1579627948.jpg**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_spectrum_data_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetSpectrumData get_spectrum_data:
        :return: SpectrumData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_spectrum_data_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_spectrum_data_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_spectrum_data_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve data from a single spectrum  # noqa: E501

        Retrieve data from a single spectrum. Image stored as username + ts_gps UNIX time in seconds **jgcasta1579627948.jpg**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_spectrum_data_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetSpectrumData get_spectrum_data:
        :return: SpectrumData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_spectrum_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_spectrum_data_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_spectrum_data' in params:
            body_params = params['get_spectrum_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/getSpectrumData', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SpectrumData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_data(self, **kwargs):  # noqa: E501
        """Retrieve user data  # noqa: E501

        Retrieve user data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_data(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData user_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_data_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_data_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_data_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve user data  # noqa: E501

        Retrieve user data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_data_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData user_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_data" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_data' in params:
            body_params = params['user_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/getUserData', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users_ranking_post(self, **kwargs):  # noqa: E501
        """Retrieve ranking of users  # noqa: E501

        Retrieve ranking of users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_ranking_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData login:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_ranking_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_users_ranking_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_users_ranking_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve ranking of users  # noqa: E501

        Retrieve ranking of users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_ranking_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserData login:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_ranking_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'login' in params:
            body_params = params['login']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/getUsersRanking', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login(self, **kwargs):  # noqa: E501
        """User login  # noqa: E501

        User login  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Login login:
        :return: UserData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.login_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.login_with_http_info(**kwargs)  # noqa: E501
            return data

    def login_with_http_info(self, **kwargs):  # noqa: E501
        """User login  # noqa: E501

        User login  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Login login:
        :return: UserData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'login' in params:
            body_params = params['login']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_spectrum_data_post(self, **kwargs):  # noqa: E501
        """Send spectrum metadata  # noqa: E501

        Send spectrum metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_spectrum_data_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpectrumData spectrum_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_spectrum_data_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.send_spectrum_data_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def send_spectrum_data_post_with_http_info(self, **kwargs):  # noqa: E501
        """Send spectrum metadata  # noqa: E501

        Send spectrum metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_spectrum_data_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SpectrumData spectrum_data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spectrum_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_spectrum_data_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'spectrum_data' in params:
            body_params = params['spectrum_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sendSpectrumData', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_spectrum_img_post(self, **kwargs):  # noqa: E501
        """Send spectrum image file  # noqa: E501

        Send spectrum image file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_spectrum_img_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file spectrum_image:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_spectrum_img_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.send_spectrum_img_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def send_spectrum_img_post_with_http_info(self, **kwargs):  # noqa: E501
        """Send spectrum image file  # noqa: E501

        Send spectrum image file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_spectrum_img_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file spectrum_image:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['spectrum_image']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_spectrum_img_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'spectrum_image' in params:
            local_var_files['SpectrumImage'] = params['spectrum_image']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sendSpectrumImg', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
