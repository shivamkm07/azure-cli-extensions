# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AclFailedEntry(msrest.serialization.Model):
    """AclFailedEntry.

    :param name:
    :type name: str
    :param type:
    :type type: str
    :param error_message:
    :type error_message: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
        error_message: Optional[str] = None,
        **kwargs
    ):
        super(AclFailedEntry, self).__init__(**kwargs)
        self.name = name
        self.type = type
        self.error_message = error_message


class BlobHierarchyListSegment(msrest.serialization.Model):
    """BlobHierarchyListSegment.

    All required parameters must be populated in order to send to Azure.

    :param blob_prefixes:
    :type blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
    :param blob_items: Required.
    :type blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
    """

    _validation = {
        'blob_items': {'required': True},
    }

    _attribute_map = {
        'blob_prefixes': {'key': 'BlobPrefixes', 'type': '[BlobPrefix]'},
        'blob_items': {'key': 'BlobItems', 'type': '[BlobItemInternal]'},
    }
    _xml_map = {
        'name': 'Blobs'
    }

    def __init__(
        self,
        *,
        blob_items: List["BlobItemInternal"],
        blob_prefixes: Optional[List["BlobPrefix"]] = None,
        **kwargs
    ):
        super(BlobHierarchyListSegment, self).__init__(**kwargs)
        self.blob_prefixes = blob_prefixes
        self.blob_items = blob_items


class BlobItemInternal(msrest.serialization.Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param deleted: Required.
    :type deleted: bool
    :param snapshot: Required.
    :type snapshot: str
    :param version_id:
    :type version_id: str
    :param is_current_version:
    :type is_current_version: bool
    :param properties: Required. Properties of a blob.
    :type properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
    :param deletion_id:
    :type deletion_id: str
    """

    _validation = {
        'name': {'required': True},
        'deleted': {'required': True},
        'snapshot': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'deleted': {'key': 'Deleted', 'type': 'bool'},
        'snapshot': {'key': 'Snapshot', 'type': 'str'},
        'version_id': {'key': 'VersionId', 'type': 'str'},
        'is_current_version': {'key': 'IsCurrentVersion', 'type': 'bool'},
        'properties': {'key': 'Properties', 'type': 'BlobPropertiesInternal'},
        'deletion_id': {'key': 'DeletionId', 'type': 'str'},
    }
    _xml_map = {
        'name': 'Blob'
    }

    def __init__(
        self,
        *,
        name: str,
        deleted: bool,
        snapshot: str,
        properties: "BlobPropertiesInternal",
        version_id: Optional[str] = None,
        is_current_version: Optional[bool] = None,
        deletion_id: Optional[str] = None,
        **kwargs
    ):
        super(BlobItemInternal, self).__init__(**kwargs)
        self.name = name
        self.deleted = deleted
        self.snapshot = snapshot
        self.version_id = version_id
        self.is_current_version = is_current_version
        self.properties = properties
        self.deletion_id = deletion_id


class BlobPrefix(msrest.serialization.Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(BlobPrefix, self).__init__(**kwargs)
        self.name = name


class BlobPropertiesInternal(msrest.serialization.Model):
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :param creation_time:
    :type creation_time: ~datetime.datetime
    :param last_modified: Required.
    :type last_modified: ~datetime.datetime
    :param etag: Required.
    :type etag: str
    :param content_length: Size in bytes.
    :type content_length: long
    :param content_type:
    :type content_type: str
    :param content_encoding:
    :type content_encoding: str
    :param content_language:
    :type content_language: str
    :param content_md5:
    :type content_md5: bytearray
    :param content_disposition:
    :type content_disposition: str
    :param cache_control:
    :type cache_control: str
    :param blob_sequence_number:
    :type blob_sequence_number: long
    :param copy_id:
    :type copy_id: str
    :param copy_source:
    :type copy_source: str
    :param copy_progress:
    :type copy_progress: str
    :param copy_completion_time:
    :type copy_completion_time: ~datetime.datetime
    :param copy_status_description:
    :type copy_status_description: str
    :param server_encrypted:
    :type server_encrypted: bool
    :param incremental_copy:
    :type incremental_copy: bool
    :param destination_snapshot:
    :type destination_snapshot: str
    :param deleted_time:
    :type deleted_time: ~datetime.datetime
    :param remaining_retention_days:
    :type remaining_retention_days: int
    :param access_tier_inferred:
    :type access_tier_inferred: bool
    :param customer_provided_key_sha256:
    :type customer_provided_key_sha256: str
    :param encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :type encryption_scope: str
    :param access_tier_change_time:
    :type access_tier_change_time: ~datetime.datetime
    :param tag_count:
    :type tag_count: int
    :param expires_on:
    :type expires_on: ~datetime.datetime
    :param is_sealed:
    :type is_sealed: bool
    :param last_accessed_on:
    :type last_accessed_on: ~datetime.datetime
    :param delete_time:
    :type delete_time: ~datetime.datetime
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'creation_time': {'key': 'Creation-Time', 'type': 'rfc-1123'},
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'content_length': {'key': 'Content-Length', 'type': 'long'},
        'content_type': {'key': 'Content-Type', 'type': 'str'},
        'content_encoding': {'key': 'Content-Encoding', 'type': 'str'},
        'content_language': {'key': 'Content-Language', 'type': 'str'},
        'content_md5': {'key': 'Content-MD5', 'type': 'bytearray'},
        'content_disposition': {'key': 'Content-Disposition', 'type': 'str'},
        'cache_control': {'key': 'Cache-Control', 'type': 'str'},
        'blob_sequence_number': {'key': 'x-ms-blob-sequence-number', 'type': 'long'},
        'copy_id': {'key': 'CopyId', 'type': 'str'},
        'copy_source': {'key': 'CopySource', 'type': 'str'},
        'copy_progress': {'key': 'CopyProgress', 'type': 'str'},
        'copy_completion_time': {'key': 'CopyCompletionTime', 'type': 'rfc-1123'},
        'copy_status_description': {'key': 'CopyStatusDescription', 'type': 'str'},
        'server_encrypted': {'key': 'ServerEncrypted', 'type': 'bool'},
        'incremental_copy': {'key': 'IncrementalCopy', 'type': 'bool'},
        'destination_snapshot': {'key': 'DestinationSnapshot', 'type': 'str'},
        'deleted_time': {'key': 'DeletedTime', 'type': 'rfc-1123'},
        'remaining_retention_days': {'key': 'RemainingRetentionDays', 'type': 'int'},
        'access_tier_inferred': {'key': 'AccessTierInferred', 'type': 'bool'},
        'customer_provided_key_sha256': {'key': 'CustomerProvidedKeySha256', 'type': 'str'},
        'encryption_scope': {'key': 'EncryptionScope', 'type': 'str'},
        'access_tier_change_time': {'key': 'AccessTierChangeTime', 'type': 'rfc-1123'},
        'tag_count': {'key': 'TagCount', 'type': 'int'},
        'expires_on': {'key': 'Expiry-Time', 'type': 'rfc-1123'},
        'is_sealed': {'key': 'Sealed', 'type': 'bool'},
        'last_accessed_on': {'key': 'LastAccessTime', 'type': 'rfc-1123'},
        'delete_time': {'key': 'DeleteTime', 'type': 'rfc-1123'},
    }
    _xml_map = {
        'name': 'Properties'
    }

    def __init__(
        self,
        *,
        last_modified: datetime.datetime,
        etag: str,
        creation_time: Optional[datetime.datetime] = None,
        content_length: Optional[int] = None,
        content_type: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_language: Optional[str] = None,
        content_md5: Optional[bytearray] = None,
        content_disposition: Optional[str] = None,
        cache_control: Optional[str] = None,
        blob_sequence_number: Optional[int] = None,
        copy_id: Optional[str] = None,
        copy_source: Optional[str] = None,
        copy_progress: Optional[str] = None,
        copy_completion_time: Optional[datetime.datetime] = None,
        copy_status_description: Optional[str] = None,
        server_encrypted: Optional[bool] = None,
        incremental_copy: Optional[bool] = None,
        destination_snapshot: Optional[str] = None,
        deleted_time: Optional[datetime.datetime] = None,
        remaining_retention_days: Optional[int] = None,
        access_tier_inferred: Optional[bool] = None,
        customer_provided_key_sha256: Optional[str] = None,
        encryption_scope: Optional[str] = None,
        access_tier_change_time: Optional[datetime.datetime] = None,
        tag_count: Optional[int] = None,
        expires_on: Optional[datetime.datetime] = None,
        is_sealed: Optional[bool] = None,
        last_accessed_on: Optional[datetime.datetime] = None,
        delete_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(BlobPropertiesInternal, self).__init__(**kwargs)
        self.creation_time = creation_time
        self.last_modified = last_modified
        self.etag = etag
        self.content_length = content_length
        self.content_type = content_type
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_md5 = content_md5
        self.content_disposition = content_disposition
        self.cache_control = cache_control
        self.blob_sequence_number = blob_sequence_number
        self.copy_id = copy_id
        self.copy_source = copy_source
        self.copy_progress = copy_progress
        self.copy_completion_time = copy_completion_time
        self.copy_status_description = copy_status_description
        self.server_encrypted = server_encrypted
        self.incremental_copy = incremental_copy
        self.destination_snapshot = destination_snapshot
        self.deleted_time = deleted_time
        self.remaining_retention_days = remaining_retention_days
        self.access_tier_inferred = access_tier_inferred
        self.customer_provided_key_sha256 = customer_provided_key_sha256
        self.encryption_scope = encryption_scope
        self.access_tier_change_time = access_tier_change_time
        self.tag_count = tag_count
        self.expires_on = expires_on
        self.is_sealed = is_sealed
        self.last_accessed_on = last_accessed_on
        self.delete_time = delete_time


class FileSystem(msrest.serialization.Model):
    """FileSystem.

    :param name:
    :type name: str
    :param last_modified:
    :type last_modified: str
    :param e_tag:
    :type e_tag: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        last_modified: Optional[str] = None,
        e_tag: Optional[str] = None,
        **kwargs
    ):
        super(FileSystem, self).__init__(**kwargs)
        self.name = name
        self.last_modified = last_modified
        self.e_tag = e_tag


class FileSystemList(msrest.serialization.Model):
    """FileSystemList.

    :param filesystems:
    :type filesystems: list[~azure.storage.filedatalake.models.FileSystem]
    """

    _attribute_map = {
        'filesystems': {'key': 'filesystems', 'type': '[FileSystem]'},
    }

    def __init__(
        self,
        *,
        filesystems: Optional[List["FileSystem"]] = None,
        **kwargs
    ):
        super(FileSystemList, self).__init__(**kwargs)
        self.filesystems = filesystems


class LeaseAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :param lease_id: If specified, the operation only succeeds if the resource's lease is active
     and matches this ID.
    :type lease_id: str
    """

    _attribute_map = {
        'lease_id': {'key': 'leaseId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        lease_id: Optional[str] = None,
        **kwargs
    ):
        super(LeaseAccessConditions, self).__init__(**kwargs)
        self.lease_id = lease_id


class ListBlobsHierarchySegmentResponse(msrest.serialization.Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param container_name: Required.
    :type container_name: str
    :param prefix:
    :type prefix: str
    :param marker:
    :type marker: str
    :param max_results:
    :type max_results: int
    :param delimiter:
    :type delimiter: str
    :param segment: Required.
    :type segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
    :param next_marker:
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'container_name': {'required': True},
        'segment': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'attr': True}},
        'container_name': {'key': 'ContainerName', 'type': 'str', 'xml': {'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'delimiter': {'key': 'Delimiter', 'type': 'str'},
        'segment': {'key': 'Segment', 'type': 'BlobHierarchyListSegment'},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(
        self,
        *,
        service_endpoint: str,
        container_name: str,
        segment: "BlobHierarchyListSegment",
        prefix: Optional[str] = None,
        marker: Optional[str] = None,
        max_results: Optional[int] = None,
        delimiter: Optional[str] = None,
        next_marker: Optional[str] = None,
        **kwargs
    ):
        super(ListBlobsHierarchySegmentResponse, self).__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.container_name = container_name
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.delimiter = delimiter
        self.segment = segment
        self.next_marker = next_marker


class ModifiedAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :param if_modified_since: Specify this header value to operate only on a blob if it has been
     modified since the specified date/time.
    :type if_modified_since: ~datetime.datetime
    :param if_unmodified_since: Specify this header value to operate only on a blob if it has not
     been modified since the specified date/time.
    :type if_unmodified_since: ~datetime.datetime
    :param if_match: Specify an ETag value to operate only on blobs with a matching value.
    :type if_match: str
    :param if_none_match: Specify an ETag value to operate only on blobs without a matching value.
    :type if_none_match: str
    """

    _attribute_map = {
        'if_modified_since': {'key': 'ifModifiedSince', 'type': 'rfc-1123'},
        'if_unmodified_since': {'key': 'ifUnmodifiedSince', 'type': 'rfc-1123'},
        'if_match': {'key': 'ifMatch', 'type': 'str'},
        'if_none_match': {'key': 'ifNoneMatch', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        if_modified_since: Optional[datetime.datetime] = None,
        if_unmodified_since: Optional[datetime.datetime] = None,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        **kwargs
    ):
        super(ModifiedAccessConditions, self).__init__(**kwargs)
        self.if_modified_since = if_modified_since
        self.if_unmodified_since = if_unmodified_since
        self.if_match = if_match
        self.if_none_match = if_none_match


class Path(msrest.serialization.Model):
    """Path.

    :param name:
    :type name: str
    :param is_directory:
    :type is_directory: bool
    :param last_modified:
    :type last_modified: str
    :param e_tag:
    :type e_tag: str
    :param content_length:
    :type content_length: long
    :param owner:
    :type owner: str
    :param group:
    :type group: str
    :param permissions:
    :type permissions: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_directory': {'key': 'isDirectory', 'type': 'bool'},
        'last_modified': {'key': 'lastModified', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'content_length': {'key': 'contentLength', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'str'},
        'group': {'key': 'group', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_directory: Optional[bool] = False,
        last_modified: Optional[str] = None,
        e_tag: Optional[str] = None,
        content_length: Optional[int] = None,
        owner: Optional[str] = None,
        group: Optional[str] = None,
        permissions: Optional[str] = None,
        **kwargs
    ):
        super(Path, self).__init__(**kwargs)
        self.name = name
        self.is_directory = is_directory
        self.last_modified = last_modified
        self.e_tag = e_tag
        self.content_length = content_length
        self.owner = owner
        self.group = group
        self.permissions = permissions


class PathHTTPHeaders(msrest.serialization.Model):
    """Parameter group.

    :param cache_control: Optional. Sets the blob's cache control. If specified, this property is
     stored with the blob and returned with a read request.
    :type cache_control: str
    :param content_encoding: Optional. Sets the blob's content encoding. If specified, this
     property is stored with the blob and returned with a read request.
    :type content_encoding: str
    :param content_language: Optional. Set the blob's content language. If specified, this property
     is stored with the blob and returned with a read request.
    :type content_language: str
    :param content_disposition: Optional. Sets the blob's Content-Disposition header.
    :type content_disposition: str
    :param content_type: Optional. Sets the blob's content type. If specified, this property is
     stored with the blob and returned with a read request.
    :type content_type: str
    :param content_md5: Specify the transactional md5 for the body, to be validated by the service.
    :type content_md5: bytearray
    :param transactional_content_hash: Specify the transactional md5 for the body, to be validated
     by the service.
    :type transactional_content_hash: bytearray
    """

    _attribute_map = {
        'cache_control': {'key': 'cacheControl', 'type': 'str'},
        'content_encoding': {'key': 'contentEncoding', 'type': 'str'},
        'content_language': {'key': 'contentLanguage', 'type': 'str'},
        'content_disposition': {'key': 'contentDisposition', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'content_md5': {'key': 'contentMD5', 'type': 'bytearray'},
        'transactional_content_hash': {'key': 'transactionalContentHash', 'type': 'bytearray'},
    }

    def __init__(
        self,
        *,
        cache_control: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_language: Optional[str] = None,
        content_disposition: Optional[str] = None,
        content_type: Optional[str] = None,
        content_md5: Optional[bytearray] = None,
        transactional_content_hash: Optional[bytearray] = None,
        **kwargs
    ):
        super(PathHTTPHeaders, self).__init__(**kwargs)
        self.cache_control = cache_control
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_disposition = content_disposition
        self.content_type = content_type
        self.content_md5 = content_md5
        self.transactional_content_hash = transactional_content_hash


class PathList(msrest.serialization.Model):
    """PathList.

    :param paths:
    :type paths: list[~azure.storage.filedatalake.models.Path]
    """

    _attribute_map = {
        'paths': {'key': 'paths', 'type': '[Path]'},
    }

    def __init__(
        self,
        *,
        paths: Optional[List["Path"]] = None,
        **kwargs
    ):
        super(PathList, self).__init__(**kwargs)
        self.paths = paths


class SetAccessControlRecursiveResponse(msrest.serialization.Model):
    """SetAccessControlRecursiveResponse.

    :param directories_successful:
    :type directories_successful: int
    :param files_successful:
    :type files_successful: int
    :param failure_count:
    :type failure_count: int
    :param failed_entries:
    :type failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
    """

    _attribute_map = {
        'directories_successful': {'key': 'directoriesSuccessful', 'type': 'int'},
        'files_successful': {'key': 'filesSuccessful', 'type': 'int'},
        'failure_count': {'key': 'failureCount', 'type': 'int'},
        'failed_entries': {'key': 'failedEntries', 'type': '[AclFailedEntry]'},
    }

    def __init__(
        self,
        *,
        directories_successful: Optional[int] = None,
        files_successful: Optional[int] = None,
        failure_count: Optional[int] = None,
        failed_entries: Optional[List["AclFailedEntry"]] = None,
        **kwargs
    ):
        super(SetAccessControlRecursiveResponse, self).__init__(**kwargs)
        self.directories_successful = directories_successful
        self.files_successful = files_successful
        self.failure_count = failure_count
        self.failed_entries = failed_entries


class SourceModifiedAccessConditions(msrest.serialization.Model):
    """Parameter group.

    :param source_if_match: Specify an ETag value to operate only on blobs with a matching value.
    :type source_if_match: str
    :param source_if_none_match: Specify an ETag value to operate only on blobs without a matching
     value.
    :type source_if_none_match: str
    :param source_if_modified_since: Specify this header value to operate only on a blob if it has
     been modified since the specified date/time.
    :type source_if_modified_since: ~datetime.datetime
    :param source_if_unmodified_since: Specify this header value to operate only on a blob if it
     has not been modified since the specified date/time.
    :type source_if_unmodified_since: ~datetime.datetime
    """

    _attribute_map = {
        'source_if_match': {'key': 'sourceIfMatch', 'type': 'str'},
        'source_if_none_match': {'key': 'sourceIfNoneMatch', 'type': 'str'},
        'source_if_modified_since': {'key': 'sourceIfModifiedSince', 'type': 'rfc-1123'},
        'source_if_unmodified_since': {'key': 'sourceIfUnmodifiedSince', 'type': 'rfc-1123'},
    }

    def __init__(
        self,
        *,
        source_if_match: Optional[str] = None,
        source_if_none_match: Optional[str] = None,
        source_if_modified_since: Optional[datetime.datetime] = None,
        source_if_unmodified_since: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(SourceModifiedAccessConditions, self).__init__(**kwargs)
        self.source_if_match = source_if_match
        self.source_if_none_match = source_if_none_match
        self.source_if_modified_since = source_if_modified_since
        self.source_if_unmodified_since = source_if_unmodified_since


class StorageError(msrest.serialization.Model):
    """StorageError.

    :param error: The service error response object.
    :type error: ~azure.storage.filedatalake.models.StorageErrorError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'StorageErrorError'},
    }

    def __init__(
        self,
        *,
        error: Optional["StorageErrorError"] = None,
        **kwargs
    ):
        super(StorageError, self).__init__(**kwargs)
        self.error = error


class StorageErrorError(msrest.serialization.Model):
    """The service error response object.

    :param code: The service error code.
    :type code: str
    :param message: The service error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'Code', 'type': 'str'},
        'message': {'key': 'Message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(StorageErrorError, self).__init__(**kwargs)
        self.code = code
        self.message = message
