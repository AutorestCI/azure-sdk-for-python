# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service import LinkedService


class SftpServerLinkedService(LinkedService):
    """A linked service for an SSH File Transfer Protocol (SFTP) server. .

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param host: The SFTP server host name. Type: string (or Expression with
     resultType string).
    :type host: object
    :param port: The TCP port number that the SFTP server uses to listen for
     client connections. Default value is 22. Type: integer (or Expression with
     resultType integer), minimum: 0.
    :type port: object
    :param authentication_type: The authentication type to be used to connect
     to the FTP server. Possible values include: 'Basic', 'SshPublicKey'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.SftpAuthenticationType
    :param user_name: The username used to log on to the SFTP server. Type:
     string (or Expression with resultType string).
    :type user_name: object
    :param password: Password to logon the SFTP server for Basic
     authentication.
    :type password: ~azure.mgmt.datafactory.models.SecureString
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    :param private_key_path: The SSH private key file path for SshPublicKey
     authentication. Only valid for on-premises copy. For on-premises copy with
     SshPublicKey authentication, either PrivateKeyPath or PrivateKeyContent
     should be specified. SSH private key should be OpenSSH format. Type:
     string (or Expression with resultType string).
    :type private_key_path: object
    :param private_key_content: Base64 encoded SSH private key content for
     SshPublicKey authentication. For on-premises copy with SshPublicKey
     authentication, either PrivateKeyPath or PrivateKeyContent should be
     specified. SSH private key should be OpenSSH format.
    :type private_key_content: ~azure.mgmt.datafactory.models.SecureString
    :param pass_phrase: The password to decrypt the SSH private key if the SSH
     private key is encrypted.
    :type pass_phrase: ~azure.mgmt.datafactory.models.SecureString
    :param skip_host_key_validation: If true, skip the SSH host key
     validation. Default value is false. Type: boolean (or Expression with
     resultType boolean).
    :type skip_host_key_validation: object
    :param host_key_fingerprint: The host key finger-print of the SFTP server.
     When SkipHostKeyValidation is false, HostKeyFingerprint should be
     specified. Type: string (or Expression with resultType string).
    :type host_key_fingerprint: object
    """

    _validation = {
        'type': {'required': True},
        'host': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'host': {'key': 'typeProperties.host', 'type': 'object'},
        'port': {'key': 'typeProperties.port', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'user_name': {'key': 'typeProperties.userName', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecureString'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
        'private_key_path': {'key': 'typeProperties.privateKeyPath', 'type': 'object'},
        'private_key_content': {'key': 'typeProperties.privateKeyContent', 'type': 'SecureString'},
        'pass_phrase': {'key': 'typeProperties.passPhrase', 'type': 'SecureString'},
        'skip_host_key_validation': {'key': 'typeProperties.skipHostKeyValidation', 'type': 'object'},
        'host_key_fingerprint': {'key': 'typeProperties.hostKeyFingerprint', 'type': 'object'},
    }

    def __init__(self, host, additional_properties=None, connect_via=None, description=None, port=None, authentication_type=None, user_name=None, password=None, encrypted_credential=None, private_key_path=None, private_key_content=None, pass_phrase=None, skip_host_key_validation=None, host_key_fingerprint=None):
        super(SftpServerLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description)
        self.host = host
        self.port = port
        self.authentication_type = authentication_type
        self.user_name = user_name
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.private_key_path = private_key_path
        self.private_key_content = private_key_content
        self.pass_phrase = pass_phrase
        self.skip_host_key_validation = skip_host_key_validation
        self.host_key_fingerprint = host_key_fingerprint
        self.type = 'Sftp'