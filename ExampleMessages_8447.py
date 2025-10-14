"""
==
== ExampleMessages.py
== For ESBox LT version: 8447
== 
== Copyright Saturn South Pty Ltd 2015
== 
== 
== Example Messages for Saturn South ESBox API
== Included API versions: 1.0, 1.1
==
"""

# All constants in this file should be read in reference to the provided SSMessages file.
import SSMessages_8447 as M




# ================================================================ Notes

# Weird Nomenclature:
# - 'server': when used in the context of ESBox API communications the server is the other party to the communication,
#   that is: not the ESBox. For the Pull API (ESBox talks first) the server is a server in the traditional sense in that
#   it listens for communication from the ESBox and responds. For the Push API however (server talks first) the ESBox is
#   the listener. We still call the other party the server in order to simplify the documentation however.
#   - The terms 'ESCo' and 'server' may be used interchangeably in this context.



# Notes on message description fields:
# - Cluster: this is the cluster of the message, it is defined by a manufacturer id-cluster id pair.
#   - This file uses named clusters - the numeric ids associated with these named clusters are provided in both
#     the example messages and the associated SSMessages file.
# - Message: this is the name of the message being described.
# - Message ID: this is the constant from SSMEssages, which defines the message id string.
# - Queue Type: TX messages (from the ESBox) are queued as they are 
#   created and sent during the next transmission to the ESCo. Messages 
#   can be appended to the ESBox's message queue in one of two modes:
#       - Normal: the message is appended to the queue as expected. Each
#                 message appended to the queue results in one message
#                 being popped from the queue and sent.
#       - Single: when the message is generated a flag is set marking
#                 the message as 'to be sent'. If the flag was already
#                 set (the message was already in the queue), the
#                 new message takes precedence (in the case where the 
#                 message has configuration options for example).
#   - In practice, this distinction does not usually affect an ESCo, but
#     it is worth noting nevertheless.
# - Versions: this field describes the versions for which the example applies. The versions are listed either:
#   - as a range - i.e. 1.0-1.3 (all versions between 1.0 and 1.3 inclusive) or 1.0-1.0 (only
#     version 1.0 is supported).
#   - as an open-ended range - i.e. 1.1+ (all version after and including 1.1 ).
#   or
#   - as a word: All (all versions)
# - Direction: this field describes which communication direction the message applies for.
#   - To ESBox (RX): the message is sent from the server to the ESBox.
#   - From ESBox (TX): the message is sent from the ESBox to the server.
# - Purpose: this field describes the purpose of the message.




# ===================================================== Wrapper Examples

# Message wrapper examples.
# - A wrapper is the highest level of the ESBox API's application layer.
# - Each wrapper contains information essential or highly useful to that API communication such as
#   information to identify the ESBox and key details about it.
# - Wrappers contain a field to include the actual messages being sent as part of the communication
#   protocol.
#   - At most one message may be sent by the server to the ESBox per wrapper.
#   - Any number of messages may be sent by the ESBox to the server per wrapper.



# Wrapper Example
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
ex_1_0__Misc__Wrapper_ESBox_to_Server = {
    
    # The version of the API protocol to use
    # - The version sent here must match the version of the messages used in the M.F.Gen.Messages field.
    # - The ESBox will always respond using the protocol version sent by the server if it is supported.
    # - If the version is not supported, the default version will be used (determined in user configuration settings).
    M.F.Gen.ProtocolVersion : "1.0", # Using API protocol version 1.0
    
    # A list containing the messages being sent to the ESBox
    # - Each list element represents one message.
    # - For details of messages that might appear here, see messages marked 'To ESBox (RX)'.
    # - Only a single message may be sent to an ESBox per wrapper in API version 1.0.
    M.F.Gen.Messages : [
        {
            # ... body of message ...
        }
    ]
}


# Wrapper Example
# Versions: 1.1+
# Direction: To ESBox (RX)
ex_1_1__Misc__Wrapper_ESBox_to_Server = {
    
    # The version of the API protocol to use
    # - The version sent here must match the version of the messages used in the M.F.Gen.Messages_1_1 field.
    # - The ESBox will always respond using the protocol version sent by the server if it is supported.
    # - If the version is not supported, the default version will be used (determined in user configuration settings).
    M.F.Gen.ProtocolVersion_1_1 : "1.1", # Using API protocol version 1.1
    
    # A list containing the messages being sent to the ESBox
    # - Each list element represents one message.
    # - For details of messages that might appear here, see messages marked 'To ESBox (RX)'.
    # - Only a single message may be sent to an ESBox per wrapper in API version 1.0.
    M.F.Gen.Messages_1_1 : [
        {
            # ... body of message ...
        }
    ]
}


# Wrapper Example
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
ex_1_0__Misc__Wrapper_ESBox_to_Server = {
    
    # The version of the API protocol in use
    # - The messages in M.F.Gen.Messages will match the version sent here.
    M.F.Gen.ProtocolVersion : "1.0", # Responding with API protocol version 1.0
    
    # The ESBox's version
    # - Note that this field may change from time to time (fields may be added).
    # - In future, this field may change to more usefully reflect the ESBox's version.
    # - At present, the string is made up of versions string separated by underscores in a consistent order.
    # - Each version string may contain any printable ascii character except '_', which is the separator.
    # - In order, those version strings are:
    #   - hardware version
    #   - esbox build version
    #   - zigbee build version
    #   - zigbee coordinator version
    #   - bootloader version (currently always ?)
    #   - webapp version (currently always ?)
    M.F.Gen.ESBoxVersion : "SS9002.1.2_8266_8258_5651_?_?",
    
    # The ESBox's identifying details
    # - 1st element: the ESBox's HAN address.
    # - 2nd element: the ESBox's link key.
    M.F.Gen.Auth : ["001BC502B0100359", "11111111111111111111111111111111"],
    
    # The current time according to the ESBox
    # - Value:
    #   - Seconds since 1 Jan 1970 (UTC).
    # - This field is new and was not in earlier version of the API version 1.0 specification.
    M.F.Dat.Time : 1425791274,
    
    # A list of messages sent by the ESBox
    # - Each list element represents one message.
    # - For details of messages that might appear here, see messages marked 'From ESBox (TX)'.
    M.F.Gen.Messages : [
        {
            # ... body of message ...
        },
        {
            # ... body of message ...
        }
    ]
}


# Wrapper Example
# Versions: 1.1+
# Direction: From ESBox (TX)
ex_1_1__Misc__Wrapper_ESBox_to_Server = {
    
    # The version of the API protocol in use
    # - The messages in M.F.Gen.Messages_1_1 will match the version sent here.
    M.F.Gen.ProtocolVersion_1_1 : "1.1", # Responding with API protocol version 1.1
    
    # The ESBox's version
    # - Note that this field may change from time to time (fields may be added).
    # - In future, this field may change to more usefully reflect the ESBox's version.
    # - At present, the string is made up of versions string separated by underscores in a consistent order.
    #   In order, those version strings are:
    #   - hardware version
    #   - esbox build version
    #   - zigbee build version
    #   - zigbee coordinator version
    #   - bootloader version (currently always ?)
    #   - webapp version (currently always ?)
    M.F.Gen.ESBoxVersion_1_1 : "SS9002.1.2_8266_8258_5651_?_?",
    
    # The ESBox's identifying details
    # - 1st element: the ESBox's HAN address.
    # - 2nd element: the ESBox's link key.
    M.F.Gen.Auth : ["001BC502B0100359", "11111111111111111111111111111111"],
    
    # The current time according to the ESBox
    # - Value:
    #   - Seconds since 1 Jan 1970 (UTC).
    M.F.Dat.Time_1_1 : 1425791274,
    
    # A list of messages sent by the ESBox
    # - Each list element represents one message.
    # - For details of messages that might appear here, see messages marked 'From ESBox (TX)'.
    M.F.Gen.Messages_1_1 : [
        {
            # ... body of message ...
        },
        {
            # ... body of message ...
        }
    ]
}



# ===================================================== Message Examples

# Message Examples.
# - Messages are categorised by their direction (either from or to the ESBox), their version (that being
#   the version(s) of the API protocol that supports them), their cluster and their message id.
# - The details of the message fields are provided here as well as example values and some description
#   explaining their meaning.



# ----------------------------------------------- Messages To ESBox (RX)

# Cluster: Common (accepted for any cluster)
# Message: ReadAttributes
# Message ID: M.Common.E.ReadAttributes
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Read the value of attributes on devices. The results end up in latest readings / stream database.
ex_1_0__Common_E_ReadAttributes = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.Common.E.ReadAttributes,
    
    # The cluster of the attributes to read
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 1794, M.F.Gen.ClusterManufacturer : 0 }, # Smart Metering Cluster (example, any cluster may be viable)

    # The HAN address of the device to read attributes from
    M.F.Nwk.DevIEEE : "001BC502B0000000",
    
    # The endpoint on the device to read attributes from
    M.F.Nwk.EndpointID : 10,
    
    # The attribute IDs to read
    M.F.Dat.Attributes : [
        57610,
        57628
    ]
}


# Cluster: Common (accepted for any cluster)
# Message: ReadAttributes_1_1
# Message ID: M.Common.E.ReadAttributes_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Read the value of attributes on devices. The results end up in latest readings / stream database.
ex_1_1__Common_E_ReadAttributes_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.Common.E.ReadAttributes_1_1,
    
    # The cluster of the attributes to read
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 1794, M.F.Gen.ClusterManufacturer_1_1 : 0 }, # Smart Metering Cluster (example, any cluster may be viable)
    
    # The HAN address of the device to read attributes from
    M.F.Nwk.HAN_1_1 : "001BC502B0000000",
    
    # The endpoint on the device to read attributes from
    M.F.Nwk.EndpointID_1_1 : 10,
    
    # The attribute IDs to read
    M.F.Dat.Attributes_1_1 : [
        57610,
        57628
    ]
}


# Cluster: Common (accepted for any cluster)
# Message: WriteAttributes
# Message ID: M.Common.E.WriteAttributes
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Set the value of attributes on devices.
ex_1_0__Common_E_WriteAttributes = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.Common.E.WriteAttributes,
    
    # The cluster of the attributes to write
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 1, M.F.Gen.ClusterManufacturer : 0 }, # Basic Cluster (example, any cluster may be viable)

    # The HAN address of the device to write attributes for
    M.F.Nwk.DevIEEE : "001BC502B0000000",
    
    # The endpoint on the device to write attributes for
    M.F.Nwk.EndpointID : 10,
    
    # The attribute IDs and corresponding values to write
    M.F.Dat.Attributes : [
        { M.F.Dat.AttributeID : 16, M.F.Dat.Value : "Hallway" },
        { M.F.Dat.AttributeID : 17, M.F.Dat.Value : 27 }
    ]
}


# Cluster: Common (accepted for any cluster)
# Message: WriteAttributes_1_1
# Message ID: M.Common.E.WriteAttributes_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Set the value of attributes on devices.
ex_1_1__Common_E_WriteAttributes_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.Common.E.WriteAttributes_1_1,
    
    # The cluster of the attributes to write
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 1, M.F.Gen.ClusterManufacturer_1_1 : 0 }, # Basic Cluster (example, any cluster may be viable)

    # The HAN address of the device to write attributes for
    M.F.Nwk.HAN_1_1 : "001BC502B0000000",
    
    # The endpoint on the device to write attributes for
    M.F.Nwk.EndpointID_1_1 : 10,
    
    # The attribute IDs and corresponding values to write
    M.F.Dat.Attributes_1_1 : [
        { M.F.Dat.AttributeID_1_1 : 16, M.F.Dat.Value_1_1 : "Hallway" },
        { M.F.Dat.AttributeID_1_1 : 17, M.F.Dat.Value_1_1 : 27 }
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: NoFurtherMessages
# Message ID: M.SS_ESB.E.NoFurtherMessages
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Indicate that the server has no more messages in its queue.
#          - Essentially this message allows the server to maintain a conversation with
#            the ESBox without saying anything, usually in order to 'clock-out' messages
#            still being sent by the ESBox.
#          - It is also used as part of the communication sequence that normally closes
#            the API connection.
ex_1_0__SS_ESB_E_NoFurtherMessages = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.NoFurtherMessages,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: NoFurtherMessages
# Message ID: M.SS_ESB.E.NoFurtherMessages_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Indicate that the server has no more messages in its queue.
#          - Essentially this message allows the server to maintain a conversation with
#            the ESBox without saying anything, usually in order to 'clock-out' messages
#            still being sent by the ESBox.
#          - It is also used as part of the communication sequence that normally closes
#            the API connection.
ex_1_1__SS_ESB_E_NoFurtherMessages_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.NoFurtherMessages_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: NotAuthenticated
# Message ID: M.SS_ESB.E.NotAuthenticated
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Indicate to the ESBox that it is not allowed to connect to this server at
#          the present time.
#          - This message closes the API connection.
ex_1_0__SS_ESB_E_NotAuthenticated = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.NotAuthenticated,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: NotAuthenticated_1_1
# Message ID: M.SS_ESB.E.NotAuthenticated_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Indicate to the ESBox that it is not allowed to connect to this server at
#          the present time.
#          - This message closes the API connection.
ex_1_1__SS_ESB_E_NotAuthenticated_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.NotAuthenticated_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: CloseConnection
# Message ID: M.SS_ESB.E.CloseConnection
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Request that the ESBox close the API connection immediately.
#          - This message closes the API connection.
ex_1_0__SS_ESB_E_CloseConnection = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.CloseConnection,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: CloseConnection_1_1
# Message ID: M.SS_ESB.E.CloseConnection_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request that the ESBox close the API connection immediately.
#          - This message closes the API connection.
ex_1_1__SS_ESB_E_CloseConnection_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.CloseConnection_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetSupportedVersions_1_1
# Message ID: M.SS_ESB.E.GetSupportedVersions_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request that the ESBox send an M.SS_ESB.E.SendSupportedVersions_1_1 message to determine what API versions the ESBox supports
#          - If a version 1.0-only ESBox encounters this message, no SendSupportedVersions message
#            will be returned, and so the ESBox should be assumed to support only version 1.0 of the API.
ex_1_1__SS_ESB_E_GetSupportedVersions_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetSupportedVersions_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 } # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendErrors
# Message ID: M.SS_ESB.E.SendErrors
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Allows the server to indicate that an error or errors occurred.
#          - This message is not fully implemented and has no effect.
#          - This message is not final and may change in the future.
ex_1_0__SS_ESB_E_SendErrors = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendErrors,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendErrors_1_1
# Message ID: M.SS_ESB.E.SendErrors_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Allows the server to indicate that an error or errors occurred.
#          - This message is not fully implemented and has no effect.
#          - This message is not final and may change in the future.
ex_1_1__SS_ESB_E_SendErrors_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendErrors_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetESBoxOptions
# Message ID: M.SS_ESB.E.GetESBoxOptions
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Request a SendESBoxOptions message.
ex_1_0__SS_ESB_E_GetESBoxOptions = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.GetESBoxOptions,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetESBoxOptions_1_1
# Message ID: M.SS_ESB.E.GetESBoxOptions_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request a SendESBoxOptions_1_1 message.
#       - This message is not final and may change in the future.
#           - Changes will be backwards compatible (additions only).
ex_1_1__SS_ESB_E_GetESBoxOptions_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetESBoxOptions_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SetESBoxOptions
# Message ID: M.SS_ESB.E.SetESBoxOptions
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Set ESBox option values.
ex_1_0__SS_ESB_E_SetESBoxOptions = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SetESBoxOptions,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # Define each ESBox option and its value to be set
    # The permissible values are any subset of the 'Read/Write' options
    M.F.ESB.Options : {
        M.F.S.ESBox.PrimaryESCoAddress : 'www.esco.com',
        M.F.S.ESBox.SecondaryESCoAddress : 'www.backup.com',
        M.F.S.ESBox.CurrentTime : 1234567890
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SetESBoxOptions_1_1
# Message ID: M.SS_ESB.E.SetESBoxOptions_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Set ESBox option values.
#       - This message is not final and may change in the future.
ex_1_1__SS_ESB_E_SetESBoxOptions_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SetESBoxOptions_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Define each ESBox option and its value to be set
    # The permissible values are any subset of the 'Read/Write' options
    M.F.ESB.Options_1_1 : {
        M.F.S.ESBox.PrimaryESCoAddress : 'www.esco.com',
        M.F.S.ESBox.SecondaryESCoAddress : 'www.backup.com',
        M.F.S.ESBox.CurrentTime : 1234567890
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: RestartESBox
# Message ID: M.SS_ESB.E.RestartESBox
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Reset the ESBox immediately (the connection will terminate).
ex_1_0__SS_ESB_E_RestartESBox = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.RestartESBox,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}

ex_1_1__SS_ESB_E_RestartESBox = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.RestartESBox,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendUpdateToken
# Message ID: M.SS_ESB.E.SendUpdateToken
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Send an update token to the ESBox. The update will be acted on immediately (the connection will terminate).
ex_1_0__SS_ESB_E_SendUpdateToken = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendUpdateToken,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # Provide the update token to use
    M.F.Upd.Token : "eyJhIjogIjU0LjY2LjEzOS4yMTIiLCAicCI6ID... truncated"
}

ex_1_1__SS_ESB_E_SendUpdateToken = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendUpdateToken,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Provide the update token to use
    M.F.Upd.Token_1_1 : "eyJhIjogIjU0LjY2LjEzOS4yMTIiLCAicCI6ID... truncated"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetUpdateStatus_1_1
# Message ID: M.SS_ESB.E.GetUpdateStatus_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request a SendUpdateStatus_1_1 message.
#          - This message is not fully implemented and some parts of it and
#           related messages may be buggy or inconsistent.
#          - This message is not final and may change in the future.
ex_1_1__SS_ESB_E_GetUpdateStatus_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetUpdateStatus_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose whether to receive information about current updates
    # - Optional
    # - Default: False
    # - If selected, this option will request information about updates currently in progress
    #   including OTA or coordinator updates in progress, bootloader updates in progress as
    #   well as information about the progress of updates currently being downloaded from
    #   a server.
    # - No information can be provided about userspace updates currently in progress (as the
    #   ESBox cannot communicate with the server while they are happening).
    M.F.ESB.Update.Current_1_1 : True,
    
    # Choose whether to receive information about registered OTA updates
    # - Optional
    # - Default: False
    # - If selected, this option will request information about OTA updates registered and
    #   and available on the ESBox. This includes coordinator updates.
    M.F.ESB.Update.OTARegistered_1_1 : True,
    
    # Choose whether to receive information about pending ESBox updates
    # - Optional
    # - Default: False
    # - If selected, this option will request information about pending filesystem, bootloader
    #   and userspace updates, as well as information about whether any retries or simliar are
    #   currently required/pending.
    # - This option is currently not implemented to any useful level
    M.F.ESB.Update.ESBoxAllPending_1_1 : True,
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetErrors
# Message ID: M.SS_ESB.E.GetErrors
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Requests that the ESBox send a SendErrors_* response.
#           - This message is not fully implemented.
#           - This message is not final and may change in the future.
ex_1_0__SS_ESB_E_GetErrors = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.GetErrors,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}

ex_1_1__SS_ESB_E_GetErrors_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetErrors,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetStatus_1_1
# Message ID: M.SS_ESB.E.GetStatus_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Requests that the ESBox send a SendStatus_1_1 response.
#          - This message is not fully implemented and has no effect.
#          - This message is not final and may change in the future.
ex_1_1__SS_ESB_E_GetStatus_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetStatus_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: ExecuteTerminalCommand_1_1
# Message ID: M.SS_ESB.E.ExecuteTerminalCommand_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Execute a command in the ESBox's shell.
#           - Executing commands using this message is exactly the same as typing them
#             into the terminal using the ESBox's webapp, except that the command itself
#             won't be echoed onto the terminal output buffer.
#           - This message is not completely finalised and may change in the future.
ex_1_1__SS_ESB_E_ExecuteTerminalCommand_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteTerminalCommand_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Either M.F.ESB.TermCommand_1_1 or M.F.ESB.TermCommandRaw_1_1 is required. If both are present, M.F.ESB.TermCommand_1_1 is used in preference.
    
    # The command string to execute, encoded in base64.
    # - This is the preferred method of passing the command to the API and if both TermCommand_1_1 and TermCommandRaw_1_1
    #   are present then TermCommand_1_1 will be used in preference.
    M.F.ESB.TermCommand_1_1 : "ZXNwbW9kdWxlIDwgY29vcmQtcmYgMjU1IDI1NQ==",
    
    # The command string to execute, not encoded.
    # - Note that receiving json escape sequences (such as \") isn't fully supported by the ESBox, so use of this
    #   method for sending the command string is discouraged in favour of TermCommand_1_1.
    M.F.ESB.TermCommandRaw_1_1 : "espmodule < coord-rf 255 255"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetTerminalOutput_1_1
# Message ID: M.SS_ESB.E.GetTerminalOutput_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request a SendTerminalOutput_1_1 message from the ESBox.
#           - This message is not completely finalised and may change in the future.
ex_1_1__SS_ESB_E_GetTerminalOutput_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetTerminalOutput_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The target UID to retrieve.
    # - Optional
    # - Default: 0
    # - See SendTerminalOutput_1_1 for details.
    M.F.ESB.TermUid_1_1 : 126
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetDir_1_1
# Message ID: M.SS_ESB.E.GetDir_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request a SendDir_1_1 message from the ESBox.
#           - This message is not completely finalised and may change in the future.
ex_1_1__SS_ESB_E_GetDir_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetDir_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The path of the directory to list
    # - Optional
    # - Default: use the current working directory
    # - The path is relative to the current working directory if the leading / is omitted
    # - The path is absolute if the leading / is included
    M.F.ESB.Filesystem.Path_1_1 : "/my/test/directory"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: ExecuteFilesystemOperation_1_1
# Message ID: M.SS_ESB.E.ExecuteFilesystemOperation_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Executes an operation to modify the filesystem or files on the ESBox.
#           - This message is not completely finalised and may change in the future.
# - This message always results in an M.SS_ESB.E.SendFilesystemOperationResult_1_1 message from the ESBox.

# - Example for M.F.Gen.Operation_1_1 == M.V.Filesystem.MakeDir_1_1:
ex_1_1__MakeDir__SS_ESB_E_ExecuteFilesystemOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteFilesystemOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteFilesystemOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Filesystem.MakeDir_1_1, # Create a directory
    
    
    # Operation-specific:
    
    # Choose whether to make the parent directories of the path or not
    # - Optional
    # - Default: False
    # - If False, the operation will fail if the parent path does not exist.
    M.F.ESB.Filesystem.MakeParents_1_1 : True,
    
    # The path of the directory to create
    # - The path is relative to the current working directory if the leading / is omitted
    # - The path is absolute if the leading / is included
    M.F.ESB.Filesystem.Path_1_1 : "/my/new/directory"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Filesystem.Remove_1_1:
ex_1_1__Remove__SS_ESB_E_ExecuteFilesystemOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteFilesystemOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteFilesystemOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Filesystem.Remove_1_1, # Remove a file or directory
    
    # Operation-specific:
    
    # Whether to recursively remove a directory or not. If removing a file, this has no effect.
    # - Optional
    # - Default: False
    # - If False, the operation will fail if the parent path does not exist.
    M.F.ESB.Filesystem.Recursive_1_1 : True,
    
    # Whether or not to force removal of the file or directory. Depending on the state of the filesystem
    #  this option may or may not successfully force removal (i.e. if a file is already open)
    # - Optional
    # - Default: False
    M.F.ESB.Filesystem.Force_1_1 : False,
    
    # The path of the file or directory to remove
    # - The path is relative to the current working directory if the leading / is omitted
    # - The path is absolute if the leading / is included
    M.F.ESB.Filesystem.Path_1_1 : "/remove/this/path"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Filesystem.MakeFile_1_1:
ex_1_1__MakeFile__SS_ESB_E_ExecuteFilesystemOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteFilesystemOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteFilesystemOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Filesystem.MakeFile_1_1, # Create a file
    
    # Operation-specific:
    
    # Whether to overwrite a file that exists at this path with a new empty one. This will not overwrite 
    #  a directory that exists at the target path. A directory at the target path must first be removed
    #  with the Remove operation.
    # - Optional
    # - Default: False
    # - If False, and a file exists at the target path, the operation will fail.
    # - The operation will fail if a directory exists at the target path.
    M.F.ESB.Filesystem.Overwrite_1_1 : True,
    
    # Whether to make the parent director(ies) as per the target path.
    # - Optional
    # - Default: False
    # - If False and the required path does not exist, the operation will fail
    # - If True and the path cannot be created, the operation will fail
    #  
    # - THIS OPTION IS CURRENTLY UNIMPLEMENTED!
    #   (create the required parent path manually)
    #
    M.F.ESB.Filesystem.MakeParents_1_1 : False,
    
    # The path of the file to create.
    # - The path is relative to the current working directory if the leading / is omitted
    # - The path is absolute if the leading / is included
    # - The path must be a valid path for a file.
    M.F.ESB.Filesystem.Path_1_1 : "/create/this/file"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Filesystem.WriteFile_1_1:
ex_1_1__WriteFile__SS_ESB_E_ExecuteFilesystemOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteFilesystemOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteFilesystemOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Filesystem.WriteFile_1_1, # Write data to a file
    
    # Operation-specific:
    
    # Whether the data to write should be written from the start of the file or appended to the end of the file.
    # - Optional
    # - Default: False
    # - If True: the file will not be truncated, and data will be appended at the end of the file.
    # - If False: the file will be truncated, and data will be written at the start of the file.
    M.F.ESB.Filesystem.Append_1_1 : False,
    
    # The data to write to the file.
    # - The data is a base64 encoded string.
    # - The length of the string should be relatively short.
    #   - The ESBox will try to accept strings of any length, but due to memory constraints certain length strings
    #     can cause issues or even in rare cases, crashes. The beta nature of the current release means that these
    #     issues are unlikely to cause crashes or errors in the future.
    #   - The recommended maximum length of this string is 1024 characters, encoded, or 768 decoded.
    #   - If you need to write a file longer than the maximum string length, split the data into multiple chunks and
    #     then use multiple WriteFile operations with the Append option set to True.
    M.F.Dat.Data_1_1 : "U2FtcGxlIGRhdGEgdG8gZ28gaW4gYSBmaWxlLg==",
    
    # The path of the file to write to.
    # - The path is relative to the current working directory if the leading / is omitted.
    # - The path is absolute if the leading / is included.
    # - The file will be created if it doesn't exist.
    # - If the file's path doesn't exist, it will not be created and the operation will fail.
    M.F.ESB.Filesystem.Path_1_1 : "/write/this/file"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Filesystem.WriteFileFromRemote_1_1:
ex_1_1__WriteFileFromRemote__SS_ESB_E_ExecuteFilesystemOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteFilesystemOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteFilesystemOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Filesystem.WriteFileFromRemote_1_1, # Write data to a file
    
    # Operation-specific:
    
    # - This operation is not currently implemented.
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetFile_1_1
# Message ID: M.SS_ESB.E.GetFile_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request a SendFile_1_1 message from the ESBox.
#           - This message is not completely finalised and may change in the future.
ex_1_1__SS_ESB_E_GetFile_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetFile_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The path of the file to get.
    # - The path is relative to the current working directory if the leading / is omitted.
    # - The path is absolute if the leading / is included.
    # - A file must exist on the specified path.
    M.F.ESB.Filesystem.Path_1_1 : "/get/this/file"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetDeviceList
# Message ID: M.SS_ESB.E.GetDeviceList
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Request a SendDeviceList message from the ESBox.
ex_1_0__SS_ESB_E_GetDeviceList = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.GetDeviceList,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # Whether to send detailed/extended parts of the device list in the corresponding SendDeviceList
    M.F.Nwk.Detailed : True
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetDeviceList_1_1
# Message ID: M.SS_ESB.E.GetDeviceList_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request a SendDeviceList_1_1 message from the ESBox.
ex_1_1__SS_ESB_E_GetDeviceList_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetDeviceList_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Whether to send detailed/extended parts of the device list in the corresponding SendDeviceList
    M.F.Nwk.Detailed_1_1 : True
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: RequestDeviceToLeave
# Message ID: M.SS_ESB.E.RequestDeviceToLeave
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Request that an end device leave the zigbee network.
#           - The function of this message is provided by M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1 from version 1.1 onwards.
ex_1_0__SS_ESB_E_RequestDeviceToLeave = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.RequestDeviceToLeave,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # The HAN address of the end device to request to leave.
    M.F.Nwk.DevIEEE : "001BC502B0000000"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: LocateDevice
# Message ID: M.SS_ESB.E.LocateDevice
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Locate an end device.
#           - The function of this message is provided by M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1 from version 1.1 onwards.
ex_1_0__SS_ESB_E_LocateDevice = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.LocateDevice,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # The HAN address of the end device to request to leave.
    # - Optional
    # - Default: locate all connected end devices.
    M.F.Nwk.DevIEEE : "001BC502B0000000"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: PermitJoining
# Message ID: M.SS_ESB.E.PermitJoining
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Locate an end device.
#           - The function of this message is provided by M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1 from version 1.1 onwards.
ex_1_0__SS_ESB_E_PermitJoining = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.PermitJoining,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # How long to permit joining for in seconds.
    # - If 0: disable permit joining if it is currently enabled.
    # - Maximum: 65535
    M.F.Dat.Duration : 60
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: ExecuteDeviceManagementOperation_1_1
# Message ID: M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Executes an operation to manage end devices or perform zigbee-network-related operations.
#           - This message is not completely finalised and may change in the future.
# - This message always results in an M.SS_ESB.E.SendDeviceManagementResult_1_1 message from the ESBox.

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.ScanDeviceList_1_1:
ex_1_1__ScanDeviceList__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.ScanDeviceList_1_1 # Trigger a scan of the device list
    
    # Operation-specific:
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.RebuildDeviceList_1_1:
ex_1_1__RebuildDeviceList__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.RebuildDeviceList_1_1, # Trigger a rebuild of the device list
    
    # Operation-specific:
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.PermitJoining_1_1:
ex_1_1__PermitJoining__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.PermitJoining_1_1, # Request the coordinator to permit joining
    
    # Operation-specific:
    
    # The duration to enable permit joining for in seconds.
    # - Optional
    # - Default: 120
    # - Applies if If Mode is TurnOn or Toggle (and permit joining is currently disabled)
    # - If 0: always disable permit joining
    M.F.Dat.Duration_1_1 : 60,
    
    # The mode in which to manipulate the coordinator's permit joining state.
    # - Choose from:
    #       - M.V.Nwk.PJ.TurnOff_1_1    -- always disable permit joining
    #       - M.V.Nwk.PJ.TurnOn_1_1     -- always enable permit joining
    #       - M.V.Nwk.PJ.Toggle_1_1     -- disable permit joining if currently enabled and enable permit joining if currently disabled
    M.F.Dat.Mode_1_1 : M.V.Nwk.PJ.TurnOn_1_1
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.ClearOTAUpdateRegistry_1_1:
ex_1_1__ClearOTAUpdateRegistry__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.ClearOTAUpdateRegistry_1_1, # Clear all registered OTA updates
    
    # Operation-specific:
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.ClearDeviceRegistry_1_1:
ex_1_1__ClearDeviceRegistry__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.ClearDeviceRegistry_1_1, # Clear the device list
    
    # Operation-specific:
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.FactoryReset_1_1:
ex_1_1__FactoryReset__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.FactoryReset_1_1, # Clear all registered OTA updates and the device list 
    
    # Operation-specific:
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.LocateEndDevice_1_1:
ex_1_1__LocateEndDevice__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.LocateEndDevice_1_1, # Locate an end device
    
    # Operation-specific:
    
    # The duration to locate the end device for.
    # - Optional
    # - Default: 7
    M.F.Dat.Duration_1_1 : 20,
    
    # The HAN address of the end device to locate.
    # - Optional
    # - Default: locate all connected end devices.
    M.F.Nwk.HAN_1_1 : "001BC502B0000000"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.LeaveEndDevice_1_1:
ex_1_1__LeaveEndDevice__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.LeaveEndDevice_1_1, # Request an end device to leave the network
    
    # Operation-specific:
    
    # The HAN address of the end device to request to leave the network.
    # - Optional
    # - Default: request all connected devices to leave the network.
    M.F.Nwk.HAN_1_1 : "001BC502B0000000"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.RebootEndDevice_1_1:
ex_1_1__RebootEndDevice__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.RebootEndDevice_1_1, # Request an end device to reboot
    
    # Operation-specific:
    
    # The HAN address of the end device to request to reboot.
    # - Optional
    # - Default: request all connected devices to reboot.
    M.F.Nwk.HAN_1_1 : "001BC502B0000000"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.RefreshEndDevice_1_1:
ex_1_1__RefreshEndDevice__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.RefreshEndDevice_1_1, # Request a refresh of an end device
    
    # Operation-specific:
    
    # The HAN address of the end device to refresh.
    # - Optional
    # - Default: request all connected devices to be refreshed.
    M.F.Nwk.HAN_1_1 : "001BC502B0000000"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.LQITestEndDevice_1_1:
ex_1_1__LQITestEndDevice__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.LQITestEndDevice_1_1, # Request an LQI test to be started for an end device
    
    # Operation-specific:
    
    # The duration to run the test for in seconds.
    # - Optional
    # - Default: 60
    M.F.Dat.Duration_1_1 : 120,
    
    # The interval at which to sample the LQI in seconds.
    # - Optional
    # - Default: 1
    M.F.Dat.Interval_1_1 : 2,
    
    # The HAN address of the end device to run the LQI test for.
    M.F.Nwk.HAN_1_1 : "001BC502B0000000"
}

# - Example for M.F.Gen.Operation_1_1 == M.V.Nwk.Op.OverrideReportInterval_1_1:
ex_1_1__OverrideReportInterval__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose the operation to perform:
    # - See the ex_1_1__*__SS_ESB_E_ExecuteDeviceManagementOperation_1_1 example messages for details of each operation
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.OverrideReportInterval_1_1, # Change the reporting interval for end devices
    
    # Operation-specific:
    
    # Enable reporting interval override for all devices.
    # - Optional
    # - Default: True
    M.F.Gen.Enable_1_1 : True,
    
    # The minimum reporting interval to use for all devices in seconds.
    # - Optional
    # - Default: no change from current setting
    M.F.Dat.MinimumValue_1_1 : 1,
    
    # The maximum reporting interval to use for all devices in seconds.
    # - Optional
    # - Default: no change from current setting
    M.F.Dat.MaximumValue_1_1 : 10
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetAvailableData
# Message ID: M.SS_ESB.E.GetAvailableData
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Not currently implemented.
ex_1_0__SS_ESB_E_GetAvailableData = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.GetAvailableData,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
}

ex_1_1__SS_ESB_E_GetAvailableData = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetAvailableData,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetData
# Message ID: M.SS_ESB.E.GetData
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Request an M.SS_ESB.E.SendData message from the ESBox.
ex_1_0__SS_ESB_E_GetData = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.GetData,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # Choose which source to get data for
    # - Optional
    # - Default: M.V.Dat.Source.Sdb
    # - Note: M.V.Dat.Source.Sdb is the only supported value
    M.F.Dat.Source : M.V.Dat.Source.Sdb, # Get data from stream database
    
    # Source-specific options:
    
    # The maximum number of cells to request the ESBox send
    # - Optional
    # - Default: 10
    # - A large value here may cause very long response times as the ESBox reads, processes and sends the data.
    M.F.Dat.Sdb.NCells : 20,
    
    # The FIFO to read the data from
    # - Optional
    # - Default: 0
    # - Values: 0-3:
    #   - 0 : 'ESCo' FIFO
    #   - 1 : 'Web-app' FIFO (web-app may use this FIFO, so it is not recommended for use)
    #   - 2 : 'User-1' FIFO
    #   - 3 : 'User-2' FIFO
    #   - N.b. these definitions will be added to SSMessages at a later date
    M.F.Dat.Sdb.Fifo : 2,
    
    # Should delta-HAN encoding be used (only include HAN in cell record if it changed)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-HAN encoding
    #   - 1: use delta-HAN encoding
    M.F.Dat.Sdb.DelIeee : 1,
    
    # Should delta-endpoint encoding be used (only include endpoint in cell record if it changed)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-endpoint encoding
    #   - 1: use delta-endpoint encoding
    M.F.Dat.Sdb.DelEP : 1,
    
    # Should delta-cluster encoding be used (only include cluster in cell record if it changed)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-cluster encoding
    #   - 1: use delta-cluster encoding
    M.F.Dat.Sdb.DelClu : 1,
    
    # Should delta-time encoding be used (only include full time in cell record for first record, and delta time for subsequent cells)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-time encoding
    #   - 1: use delta-time encoding
    M.F.Dat.Sdb.DelTime : 1
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetData_1_1
# Message ID: M.SS_ESB.E.GetData_1_1
# Versions: 1.1+
# Direction: To ESBox (RX)
# Purpose: Request an M.SS_ESB.E.SendData_1_1 message from the ESBox.
#       - This message is not final and may change.
#         In particular the constant values are likely to be made version 1.1 specific and more consistent.

# - Example for M.F.Dat.Source == M.V.Dat.Source.Sdb:
ex_1_1__Sdb__SS_ESB_E_GetData = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetData_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose which source to get data for
    # - Optional
    # - Default: M.V.Dat.Source.Sdb
    M.F.Dat.Source : M.V.Dat.Source.Sdb, # Get data from stream database
    
    # Source-specific options:
    
    # The maximum number of cells to request the ESBox send
    # - Optional
    # - Default: 10
    # - A large value here may cause very long response times as the ESBox reads, processes and sends the data.
    M.F.Dat.Sdb.NCells : 20,
    
    # The FIFO to read the data from
    # - Optional
    # - Default: 0
    # - Values: 0-3:
    #   - 0 : 'ESCo' FIFO
    #   - 1 : 'Web-app' FIFO (web-app may use this FIFO, so it is not recommended for use)
    #   - 2 : 'User-1' FIFO
    #   - 3 : 'User-2' FIFO
    #   - N.b. these definitions will be added to SSMessages at a later date
    M.F.Dat.Sdb.Fifo : 2,
    
    # Should delta-HAN encoding be used (only include HAN in cell record if it changed)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-HAN encoding
    #   - 1: use delta-HAN encoding
    M.F.Dat.Sdb.DelIeee : 1,
    
    # Should delta-endpoint encoding be used (only include endpoint in cell record if it changed)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-endpoint encoding
    #   - 1: use delta-endpoint encoding
    M.F.Dat.Sdb.DelEP : 1,
    
    # Should delta-cluster encoding be used (only include cluster in cell record if it changed)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-cluster encoding
    #   - 1: use delta-cluster encoding
    M.F.Dat.Sdb.DelClu : 1,
    
    # Should delta-time encoding be used (only include full time in cell record for first record, and delta time for subsequent cells)
    # - Optional
    # - Default: 1
    # - Values:
    #   - 0: do not use delta-time encoding
    #   - 1: use delta-time encoding
    M.F.Dat.Sdb.DelTime : 1
}

# - Example for M.F.Dat.Source == M.V.Dat.Source.LatestReadings_1_1:
ex_1_1__LatestReadings__SS_ESB_E_GetData = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.GetData_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Choose which source to get data for
    # - Optional
    # - Default: M.V.Dat.Source.Sdb
    M.F.Dat.Source : M.V.Dat.Source.LatestReadings_1_1, # Get data from latest readings (similar to GetLatestReadings in v1.0 API) 
    
    # Source-specific options:
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: GetLatestReadings
# Message ID: M.SS_ESB.E.GetLatestReadings
# Versions: 1.0-1.0
# Direction: To ESBox (RX)
# Purpose: Request an M.SS_ESB.E.SendLatestReadings message from the ESBox.
ex_1_0__SS_ESB_E_GetLatestReadings = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.GetLatestReadings,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 } # SS_ESB Cluster
}


# Cluster: Saturn South Load Control (SS_LC)
# Message: GetWaveform
# Message ID: M.SS_LC.E.GetWaveform
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Requests a waveform sample to be generated by an end device.
#          The waveform data can be retrieved from latest readings or the stream database.
#       - This message is newly implemented for version 1.0 of the API.
#       - This message may change for version 1.0 of the API.
#       - This message will likely have a specific version 1.1 API version added, changing this message to API version 1.0 only.
ex_1_0__SS_LC_E_GetWaveform = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_LC.E.GetWaveform,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 64784, M.F.Gen.ClusterManufacturer : 4278 }, # SS_LC Cluster
    
    # The HAN address of the end device from which to request the waveform sample
    M.F.Nwk.DevIEEE : "001BC502B0000000",
    
    # The endpoint of the end device to request the waveform sample from
    # - Optional
    # - Default: 0
    M.F.Nwk.EndpointID : 10,
    
    # The source of waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.Source.Voltage)
    # - Value:
    #   - M.V.Waveform.Source.Voltage               - sample voltage only
    #   - M.V.Waveform.Source.Current               - sample current only
    #   - M.V.Waveform.Source.VoltageAndCurrent     - sample voltage and current
    M.F.Dat.Waveform.Source : M.V.Waveform.Source.Voltage,
    
    # The trigger for the waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.Trigger.Random)
    # - Value:
    #   - M.V.Waveform.Trigger.Random               - trigger sample at random time
    #   - M.V.Waveform.Trigger.VoltageZeroCross     - trigger sample at voltage zero crossing
    #   - M.V.Waveform.Trigger.RelayStateChange     - trigger sample when relay changes state
    M.F.Dat.Waveform.Trigger : M.V.Waveform.Trigger.VoltageZeroCross,
    
    # The sample-rate for the waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.SampleRate.sr512)
    # - Value:
    #   - M.V.Waveform.SampleRate.sr512             - 512 samples per second (worst temporal resolution, longest sample duration)
    #   - M.V.Waveform.SampleRate.sr1024            - 1024 samples per second
    #   - M.V.Waveform.SampleRate.sr2048            - 2048 samples per second
    #   - M.V.Waveform.SampleRate.sr4096            - 4096 samples per second (best temporal resolution, shortest sample duration)
    M.F.Dat.Waveform.SampleRate : M.V.Waveform.SampleRate.sr2048,
    
    # The resolution of the waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.SampleResolution.eight)
    # - Value:
    #   - M.V.Waveform.SampleResolution.eight       - 8-bit sample resolution
    #   - M.V.Waveform.SampleResolution.sixteen     - 16-bit sample resolution
    M.F.Dat.Waveform.SampleResolution : M.V.Waveform.SampleResolution.sixteen
}

ex_1_1__SS_LC_E_GetWaveform = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_LC.E.GetWaveform,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 64784, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_LC Cluster
    
    # The HAN address of the end device from which to request the waveform sample
    M.F.Nwk.DevIEEE : "001BC502B0000000",
    
    # The endpoint of the end device to request the waveform sample from
    # - Optional
    # - Default: 0
    M.F.Nwk.EndpointID : 10,
    
    # The source of waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.Source.Voltage)
    # - Value:
    #   - M.V.Waveform.Source.Voltage               - sample voltage only
    #   - M.V.Waveform.Source.Current               - sample current only
    #   - M.V.Waveform.Source.VoltageAndCurrent     - sample voltage and current
    M.F.Dat.Waveform.Source : M.V.Waveform.Source.Voltage,
    
    # The trigger for the waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.Trigger.Random)
    # - Value:
    #   - M.V.Waveform.Trigger.Random               - trigger sample at random time
    #   - M.V.Waveform.Trigger.VoltageZeroCross     - trigger sample at voltage zero crossing
    #   - M.V.Waveform.Trigger.RelayStateChange     - trigger sample when relay changes state
    M.F.Dat.Waveform.Trigger : M.V.Waveform.Trigger.VoltageZeroCross,
    
    # The sample-rate for the waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.SampleRate.sr512)
    # - Value:
    #   - M.V.Waveform.SampleRate.sr512             - 512 samples per second (worst temporal resolution, longest sample duration)
    #   - M.V.Waveform.SampleRate.sr1024            - 1024 samples per second
    #   - M.V.Waveform.SampleRate.sr2048            - 2048 samples per second
    #   - M.V.Waveform.SampleRate.sr4096            - 4096 samples per second (best temporal resolution, shortest sample duration)
    M.F.Dat.Waveform.SampleRate : M.V.Waveform.SampleRate.sr2048,
    
    # The resolution of the waveform sample
    # - Optional
    # - Default: 0 (M.V.Waveform.SampleResolution.eight)
    # - Value:
    #   - M.V.Waveform.SampleResolution.eight       - 8-bit sample resolution
    #   - M.V.Waveform.SampleResolution.sixteen     - 16-bit sample resolution
    M.F.Dat.Waveform.SampleResolution : M.V.Waveform.SampleResolution.sixteen
}


# Cluster: Saturn South Load Control (SS_LC)
# Message: BroadcastDispatch
# Message ID: M.SS_LC.E.BroadcastDispatch
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Requests that a set of devices either 'revert' to their safe state or exit their safe state
#       - This message will likely have a specific version 1.1 API version added, changing this message to API version 1.0 only.
ex_1_0__SS_LC_E_BroadcastDispatch = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_LC.E.BroadcastDispatch,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 64784, M.F.Gen.ClusterManufacturer : 4278 }, # SS_LC Cluster
    
    # A list of the HAN addresses for the end devices that the request should be sent to
    # - Each list element represents an end device's HAN address.
    M.F.Nwk.Devices : [
        "001BC502B0000000",
        "001BC502B000001A",
        "001BC502B00003CF"
    ],
    
    # The target endpoint for each end device
    # - Optional
    # - Default: 0 (this is almost never correct)
    # - Value: 
    #   - typically 10 for single phase devices.
    #   - consult product documentation for the particular end device for more details.
    M.F.Nwk.EndpointID: 10,
    
    # Whether devices should be requested to revert or return to their original state
    # - Optional
    # - Default: 0
    # - Value:
    #   - 0: set all switches on the device to the opposite of their configured safe-state.
    #   - 1: revert all switches to their configured safe-state or no change if not already in safe-state.
    M.F.Nwk.Revert: 1
}

ex_1_1__SS_LC_E_BroadcastDispatch = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_LC.E.BroadcastDispatch,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 64784, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_LC Cluster
    
    # A list of the HAN addresses for the end devices that the request should be sent to
    # - Each list element represents an end device's HAN address.
    M.F.Nwk.Devices : [
        "001BC502B0000000",
        "001BC502B000001A",
        "001BC502B00003CF"
    ],
    
    # The target endpoint for each end device
    # - Optional
    # - Default: 0 (this is almost never correct)
    # - Value: 
    #   - typically 10 for single phase devices.
    #   - consult product documentation for the particular end device for more details.
    M.F.Nwk.EndpointID: 10,
    
    # Whether devices should be requested to revert or return to their original state
    # - Optional
    # - Default: 0
    # - Value:
    #   - 0: set all switches on the device to the opposite of their configured safe-state.
    #   - 1: revert all switches to their configured safe-state or no change if not already in safe-state.
    M.F.Nwk.Revert: 1
}


# Cluster: On-Off (OnOff)
# Message: SwitchState
# Message ID: M.OnOff.E.SwitchState
# Versions: 1.0+
# Direction: To ESBox (RX)
# Purpose: Change the switch state of an end device
#       - This message will likely have a specific version 1.1 API version added, changing this message to API version 1.0 only.
ex_1_0__OnOff_E_SwitchState = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.OnOff.E.SwitchState,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 6, M.F.Gen.ClusterManufacturer : 0 }, # OnOff Cluster
    
    # The HAN address of the end device for which to change switch state
    M.F.Nwk.DevIEEE : "001BC502B0000000",
    
    # The endpoint of the end device for which to change switch state
    # - Optional
    # - Default: 0
    M.F.Nwk.EndpointID : 10,
    
    # How to change switch state for the end device
    # - Value:
    #   - M.V.OnOff.On      - set the switch state to on.
    #   - M.V.OnOff.Off     - set the switch state to off.
    #   - M.V.OnOff.Toggle  - toggle the switch state.
    # - Default: M.V.OnOff.Toggle
    M.F.OnOff.Action: M.V.OnOff.On
}

ex_1_1__OnOff_E_SwitchState = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.OnOff.E.SwitchState, # n.b. M.OnOff.E.SwitchState is the correct constant
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 6, M.F.Gen.ClusterManufacturer_1_1 : 0 }, # OnOff Cluster
    
    # The HAN address of the end device for which to change switch state
    M.F.Nwk.DevIEEE : "001BC502B0000000", # n.b. M.F.Nwk.DevIEEE is the correct constant
    
    # The endpoint of the end device for which to change switch state
    # - Optional
    # - Default: 0
    M.F.Nwk.EndpointID : 10, # n.b. M.F.Nwk.EndpointID is the correct constant
    
    # How to change switch state for the end device
    # - Value:
    #   - M.V.OnOff.On      - set the switch state to on.
    #   - M.V.OnOff.Off     - set the switch state to off.
    #   - M.V.OnOff.Toggle  - toggle the switch state.
    # - Default: M.V.OnOff.Toggle
    M.F.OnOff.Action: M.V.OnOff.Off # n.b. M.F.OnOff.Action is the correct constant
}




# --------------------------------------------- Messages From ESBox (TX)

# Cluster: Saturn South ESBox (SS_ESB)
# Message: NoFurtherMessages
# Message ID: M.SS_ESB.E.NoFurtherMessages
# Queue Type: Single
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
# Purpose: Indicate that the ESBox has no more messages in its queue.
#          - Allows the ESBox to respond with a 'nothing' message in order that the server
#            be able to keep sending messages to the ESBox while maintaining a conversation.
#          - It is also used as part of the communication sequence that normally closes
#            the API connection.
ex_1_0__SS_ESB_E_NoFurtherMessages = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.NoFurtherMessages,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 } # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: NoFurtherMessages
# Message ID: M.SS_ESB.E.NoFurtherMessages_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Indicate that the ESBox has no more messages in its queue.
#          - Allows the ESBox to respond with a 'nothing' message in order that the server
#            be able to keep sending messages to the ESBox while maintaining a conversation.
#          - It is also used as part of the communication sequence that normally closes
#            the API connection.
ex_1_1__SS_ESB_E_NoFurtherMessages_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.NoFurtherMessages_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 } # SS_ESB Cluster
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendSupportedVersions_1_1
# Message ID: M.SS_ESB.E.SendSupportedVersions_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the API versions supported by the ESBox.
#       - This message is in beta and may change slightly in the future.
ex_1_1__SS_ESB_E_SendSupportedVersions_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendSupportedVersions_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    M.F.Gen.ProtocolVersions_1_1 : [
        "1.0",
        "1.1"
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendErrors
# Message ID: M.SS_ESB.E.SendErrors
# Queue Type: Single
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
# Purpose: Returns a summary of errors that have occurred or are currently occurring on the ESBox.
#       - This message is not finalised and may change in future.
#       - This message is not full implemented or tested.
#       - This message should not be used in production. The version 1.1 message should be used instead.
ex_1_0__SS_ESB_E_SendErrors = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendErrors,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # The current ESBox version
    # - This field should be ignored and may not be present in subsequent revisions of the version 1.0 API.
    M.F.Nwk.Version : "Value should be ignored",
    
    M.F.ESB.Status : {
        # The current status of the ESBox
        # - Values:
        #   - M.V.Status.AppOK          - ESBox is running normally
        #   - M.V.Status.AppUpdating    - ESBox is updating
        #   - M.V.Status.AppError       - ESBox is experiencing an error state
        M.F.ESB.AppStatus : M.V.Status.AppOK,
        
        # The current status of the ESBox's zigbee network stack
        # - Values:
        #   - M.V.Status.ZigbeeOK       - zigbee stack is running normally
        #   - M.V.Status.ZigbeePJ       - zigbee stack is running normally and joining is permitted
        #   - M.V.Status.ZigbeeStarting - zigbee stack is not running because it is currently starting up
        #   - M.V.Status.ZigbeeError    - zigbee stack is not running because it is experiencing an error
        M.F.ESB.ZigbeeStatus : M.V.Status.ZigbeeOK
    },
    
    M.F.ESB.Errors : [
        # File-system and disk errors
        0, # low level disk error
        0, # disk error, possibly not fatal
        0, # disk has hardware write-lock set
        0, # disk is not formatted
        0, # other critical file-system failure
        
        # RTC errors
        0, # RTC failed and is inoperable
        
        # Comms errors
        0, # ethernet not connected
        0, # ethernet suffered a fatal error
        0, # failed communicating with the ESCo / target communication platform
        
        # Zigbee errors
        0, # zigbee error
        
        # Internal errors
        0, # system ran out of heap
        0, # a fatal update failure occurred
        0, # an error occurred but there are no details for it
        
        # Application errors
        0, # filesystem (web-app) has diverged from its allowed parameters and needs replacing
        
        # Commissioning errors
        0, # HAN address hasn't been set and is currently the default
        #       - this is a special error and will set the whole error display to a be a slow red/green blinking mess
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendErrors_1_1
# Message ID: M.SS_ESB.E.SendErrors_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns a summary of errors that have occurred or are currently occurring on the ESBox.
#       - This message is not finalised and may change in future.
#       - This message is not full implemented or tested.
#       - This functionality of this message will likely be partially or totally shifted into SendStatus_1_1.
ex_1_1__SS_ESB_E_SendErrors_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendErrors_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The current ESBox version
    # - This field should be ignored and may not be present in subsequent revisions of the version 1.1 API.
    M.F.Nwk.Version_1_1 : "Value should be ignored",
    
    M.F.ESB.Status_1_1 : {
        # The current status of the ESBox
        # - Values:
        #   - M.V.Status.AppOK          - ESBox is running normally
        #   - M.V.Status.AppUpdating    - ESBox is updating
        #   - M.V.Status.AppError       - ESBox is experiencing an error state
        M.F.ESB.AppStatus : M.V.Status.AppOK,
        
        # The current status of the ESBox's zigbee network stack
        # - Values:
        #   - M.V.Status.ZigbeeOK       - zigbee stack is running normally
        #   - M.V.Status.ZigbeePJ       - zigbee stack is running normally and joining is permitted
        #   - M.V.Status.ZigbeeStarting - zigbee stack is not running because it is currently starting up
        #   - M.V.Status.ZigbeeError    - zigbee stack is not running because it is experiencing an error
        M.F.ESB.ZigbeeStatus_1_1 : M.V.Status.ZigbeeOK
    },
    
    M.F.ESB.Errors_1_1 : [
        # File-system and disk errors
        0, # low level disk error
        0, # disk error, possibly not fatal
        0, # disk has hardware write-lock set
        0, # disk is not formatted
        0, # other critical file-system failure
        
        # RTC errors
        0, # RTC failed and is inoperable
        
        # Comms errors
        0, # ethernet not connected
        0, # ethernet suffered a fatal error
        0, # failed communicating with the ESCo / target communication platform
        
        # Zigbee errors
        0, # zigbee error
        
        # Internal errors
        0, # system ran out of heap
        0, # a fatal update failure occurred
        0, # an error occurred but there are no details for it
        
        # Application errors
        0, # filesystem (web-app) has diverged from its allowed parameters and needs replacing
        
        # Commissioning errors
        0, # HAN address hasn't been set and is currently the default
        #       - this is a special error and will set the whole error display to a be a slow red/green blinking mess
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendESBoxOptions
# Message ID: M.SS_ESB.E.SendESBoxOptions
# Queue Type: Single
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
# Purpose: Returns a list of ESBox Options and their values
#       - The functionality of this message will be significantly improved in API version 1.1
ex_1_0__SS_ESB_E_SendESBoxOptions = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendESBoxOptions,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # The current ESBox version
    # - This field should be ignored and may not be present in subsequent revisions of the version 1.0 API.
    M.F.Nwk.Version : "Value should be ignored",
    
    # List of all ESBox Options
    # - See ESBox Options documentation for details of ESBox Options
    # - In future, new options may be added to this list
    # - In future, options may change string constant (names will remain the same), purpose or be removed
    # - Some messages may be included in the message, but not in this documentation. These values should be ignored.
    M.F.ESB.Options : {
        M.F.S.ESBox.PollESCoInterval : 30,                              # - ESCo poll interval, seconds (uint32)
        M.F.S.ESBox.ESCoTimeout : 30,                                   # - ESCo timeout, seconds (uint32)

        M.F.S.ESBox.PrimaryESCoAddress : "esco.example.com",            # - Primary ESCo address (string)
        M.F.S.ESBox.PrimaryESCoPath : "/esco/",                         # - Primary ESCo path (string)
        M.F.S.ESBox.PrimaryESCoPort : 443,                              # - Primary ESCo port (uint32, logical uint16)

        M.F.S.ESBox.SecondaryESCoAddress : "alternate.example.com",     # - Secondary ESCo address (string)
        M.F.S.ESBox.SecondaryESCoPath : "/esco-bak/",                   # - Secondary ESCo path (string)
        M.F.S.ESBox.SecondaryESCoPort : 80,                             # - Secondary ESCo port (uint32, logical uint16)

        M.F.S.ESBox.ProxyAddr : "",                                     # - ESCo Proxy address (string) - not currently used
        M.F.S.ESBox.ProxyPort : 0,                                      # - ESCo Proxy port (uint32, logical uint16) - not currently used
        M.F.S.ESBox.ProxyUsername : "",                                 # - ESCo Proxy username (string) - not currently used
        M.F.S.ESBox.ProxyPassword : "",                                 # - ESCo Proxy password (string) - not currently used

        M.F.S.ESBox.EnableAsynchronousContainers : 0,                   # - Enabled asynchronous containers (uint32, logical bool) - not currently used
        M.F.S.ESBox.AutomaticallySendLatestReadings : 0,                # - Automatically send latest readings (uint32, logical bool) - deprecated, will be removed in a later version
        M.F.S.ESBox.NoESCoCommsSafeStateTimeout : 120,                  # - No ESCo comms safe state timeout, seconds (uint32)

        M.F.S.ESBox.CurrentTime : 1423796378,                           # - Current time, seconds since epoch (1 Jan, 1970) (uint64)

        M.F.S.ESBox.DbMaxReportedEsboxTimeDiff : 30,                    # - Maximum reported-to-ESBox time difference (uint32 - not currently used
        M.F.S.ESBox.DbCreateNewFileThreshold : 3600,                    # - File creation threshold (uint32) - not currently used
        M.F.S.ESBox.DbWriteDiscardedDatapoints : 1,                     # - Write discarded datapoints (uint32, logical bool)

        # The following ESBox Options are read-only and cannot be modified:
        M.F.S.ESBox.TotalUptimeMs : 1987472,                            # - Total uptime, ms (uint64)
        M.F.S.ESBox.ThisUptimeMs : 29891,                               # - This uptime, ms (uint64)

        M.F.S.ESBox.LastGoodESCoAddress : "esco.example.com",           # - Last successfully contacted ESCo address (string)
        M.F.S.ESBox.LastGoodESCoPath : "/esco/",                        # - Last successfully contacted ESCo path (string)
        M.F.S.ESBox.LastGoodESCoPort : 443,                             # - Last successfully contacted ESCo port (uint32, logical uint16)
        M.F.S.ESBox.LastGoodProxyAddr : "",                             # - Last successfully contacted ESCo Proxy address (string) - not currently used
        M.F.S.ESBox.LastGoodProxyPort : 0,                              # - Last successfully contacted ESCo Proxy port (uint32, logical uint16) - not currently used

        # Some of the following counters can be inaccurate or non-functional at times
        M.F.S.ESBox.NumReboots : 208,                                   # - Number of times the ESBox has been restarted (uint32)
        M.F.S.ESBox.NumSoftReboots : 184,                               # - Number of times that the ESBox has been intentionally restarted in software (uint32)
        M.F.S.ESBox.NumWatchdogReboots : 3,                             # - Number of times that the ESBox has been restarted by the watchdog (uint32)
        M.F.S.ESBox.NumCmdsProcessed : 2572,                            # - Number of commands processed by the ESCo API on the ESBox (irrespective of the source)
        M.F.S.ESBox.NumCmdsFailed : 55,                                 # - Number of ESCo API commands failed to be processed by the ESBox (irrespective of the source)
        M.F.S.ESBox.NumCmdsUnrecognised : 0,                            # - Number of ESCo API commands unrecognised by the ESBox (irrespective of the source)
        M.F.S.ESBox.NumHTTPConnectionsFailed : 0,                       # - Number of times the ESBox has tried to contact an ESCo using HTTP and failed (including explicitly refused connections)
        M.F.S.ESBox.NumSSLConnectionsFailed : 0                         # - Number of times the ESBox has tried to contact an ESCo using HTTPS and failed (including explicitly refused connections)
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendESBoxOptions_1_1
# Message ID: M.SS_ESB.E.SendESBoxOptions_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns a list of ESBox Options and their values
#           - This function will be updated to include visibility of more and a greater variety of ESBox settings, options and configuration.
#           - The structure of this function will be upgraded in such a way that minimally, or does not impact backwards compatibility.
ex_1_1__SS_ESB_E_SendESBoxOptions_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendESBoxOptions_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The current ESBox version
    # - This field should be ignored and may not be present in subsequent revisions of the version 1.1 API.
    M.F.Nwk.Version_1_1 : "Value should be ignored",
    
    # List of all ESBox Options
    # - See ESBox Options documentation for details of ESBox Options
    # - In future, new options may be added to this list
    # - In future, options may change string constant (names will remain the same), purpose or be removed
    # - Some messages may be included in the message, but not in this documentation. These values should be ignored.
    # - These constants will likely be updated to _1_1 suffixes in the future.
    M.F.ESB.Options_1_1 : {
        M.F.S.ESBox.PollESCoInterval : 30,                              # - ESCo poll interval, seconds (uint32)
        M.F.S.ESBox.ESCoTimeout : 30,                                   # - ESCo timeout, seconds (uint32)

        M.F.S.ESBox.PrimaryESCoAddress : "esco.example.com",            # - Primary ESCo address (string)
        M.F.S.ESBox.PrimaryESCoPath : "/esco/",                         # - Primary ESCo path (string)
        M.F.S.ESBox.PrimaryESCoPort : 443,                              # - Primary ESCo port (uint32, logical uint16)

        M.F.S.ESBox.SecondaryESCoAddress : "alternate.example.com",     # - Secondary ESCo address (string)
        M.F.S.ESBox.SecondaryESCoPath : "/esco-bak/",                   # - Secondary ESCo path (string)
        M.F.S.ESBox.SecondaryESCoPort : 80,                             # - Secondary ESCo port (uint32, logical uint16)

        M.F.S.ESBox.ProxyAddr : "",                                     # - ESCo Proxy address (string) - not currently used
        M.F.S.ESBox.ProxyPort : 0,                                      # - ESCo Proxy port (uint32, logical uint16) - not currently used
        M.F.S.ESBox.ProxyUsername : "",                                 # - ESCo Proxy username (string) - not currently used
        M.F.S.ESBox.ProxyPassword : "",                                 # - ESCo Proxy password (string) - not currently used

        M.F.S.ESBox.EnableAsynchronousContainers : 0,                   # - Enabled asynchronous containers (uint32, logical bool) - not currently used
        M.F.S.ESBox.AutomaticallySendLatestReadings : 0,                # - Automatically send latest readings (uint32, logical bool) - deprecated, will be removed in a later version
        M.F.S.ESBox.NoESCoCommsSafeStateTimeout : 120,                  # - No ESCo comms safe state timeout, seconds (uint32)

        M.F.S.ESBox.CurrentTime : 1423796378,                           # - Current time, seconds since epoch (1 Jan, 1970) (uint64)

        M.F.S.ESBox.DbMaxReportedEsboxTimeDiff : 30,                    # - Maximum reported-to-ESBox time difference (uint32 - not currently used
        M.F.S.ESBox.DbCreateNewFileThreshold : 3600,                    # - File creation threshold (uint32) - not currently used
        M.F.S.ESBox.DbWriteDiscardedDatapoints : 1,                     # - Write discarded datapoints (uint32, logical bool)

        # The following ESBox Options are read-only and cannot be modified:
        M.F.S.ESBox.TotalUptimeMs : 1987472,                            # - Total uptime, ms (uint64)
        M.F.S.ESBox.ThisUptimeMs : 29891,                               # - This uptime, ms (uint64)

        M.F.S.ESBox.LastGoodESCoAddress : "esco.example.com",           # - Last successfully contacted ESCo address (string)
        M.F.S.ESBox.LastGoodESCoPath : "/esco/",                        # - Last successfully contacted ESCo path (string)
        M.F.S.ESBox.LastGoodESCoPort : 443,                             # - Last successfully contacted ESCo port (uint32, logical uint16)
        M.F.S.ESBox.LastGoodProxyAddr : "",                             # - Last successfully contacted ESCo Proxy address (string) - not currently used
        M.F.S.ESBox.LastGoodProxyPort : 0,                              # - Last successfully contacted ESCo Proxy port (uint32, logical uint16) - not currently used

        # Some of the following counters can be inaccurate or non-functional at times
        M.F.S.ESBox.NumReboots : 208,                                   # - Number of times the ESBox has been restarted (uint32)
        M.F.S.ESBox.NumSoftReboots : 184,                               # - Number of times that the ESBox has been intentionally restarted in software (uint32)
        M.F.S.ESBox.NumWatchdogReboots : 3,                             # - Number of times that the ESBox has been restarted by the watchdog (uint32)
        M.F.S.ESBox.NumCmdsProcessed : 2572,                            # - Number of commands processed by the ESCo API on the ESBox (irrespective of the source)
        M.F.S.ESBox.NumCmdsFailed : 55,                                 # - Number of ESCo API commands failed to be processed by the ESBox (irrespective of the source)
        M.F.S.ESBox.NumCmdsUnrecognised : 0,                            # - Number of ESCo API commands unrecognised by the ESBox (irrespective of the source)
        M.F.S.ESBox.NumHTTPConnectionsFailed : 0,                       # - Number of times the ESBox has tried to contact an ESCo using HTTP and failed (including explicitly refused connections)
        M.F.S.ESBox.NumSSLConnectionsFailed : 0                         # - Number of times the ESBox has tried to contact an ESCo using HTTPS and failed (including explicitly refused connections)
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendUpdateStatus_1_1
# Message ID: M.SS_ESB.E.SendUpdateStatus_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns a the current status of the ESBox updater and update progress
#           - This function will be updated to include more information, categories and improve the accuracy and presentation of the data included.
#           - The structure of this function will be upgraded in such a way that minimally, or does not impact backwards compatibility.
#           - At this time, it is suggested not to rely on this function not changing for production systems.
ex_1_1__SS_ESB_E_SendUpdateStatus_1_1 = {
    
    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendUpdateStatus_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Data about updates currently in progress
    # - This field is included if M.F.ESB.Update.Current_1_1 was True in the requesting GetUpdateStatus_1_1 message.
    M.F.ESB.Update.Current_1_1 : {
        
        # Data about the current OTA update occurring (including coordinator update)
        # - This field is included if an OTA update is currently in progress.
        M.F.ESB.Update.CurrentOTAUpdates_1_1 : {
        
            # The type of update:
            # - M.V.Upd.UpdateTypeCoord     : the coordinator is currently being updated via OTA
            # - M.V.Upd.UpdateTypeOTA       : an end device is currently being updated via OTA
            M.F.ESB.Update.OTAType_1_1 : M.V.Upd.UpdateTypeOTA,
            
            # Percentage completeness of the current update:
            # - 0 to 100 (percentage)
            M.F.ESB.Update.OTAPercentComplete_1_1 : 88,
            
            # Estimated number of seconds remaining until the update is complete:
            # - 0 to 32-bit uint (seconds)
            M.F.ESB.Update.OTAEstimatedSecondsRemaining_1_1 : 18,
            
            # The HAN address of the end device (or coordinator) currently being updated
            M.F.Nwk.HAN_1_1 : "001BC502B0000000"
        },
        
        # Bootloader update progress
        # - Currently unimplemented.
        
        # Update validation progress
        # - Currently unimplemented.
        
        # Update download progress
        # - This field is included if a file is currently being downloaded.
        # - More fields may be added to M.F.ESB.Update.CurrentDownloads_1_1 in future revisions of the version 1.1 API.
        M.F.ESB.Update.CurrentDownloads_1_1 : {
            
            # Status of the download
            # - The contents of this field is not final and will change.
            M.F.ESB.Update.DownloadStatus_1_1 : [
                # Integer representation of the download status
                # - The meaning of this value is currently 'black magic'.
                #   - Values will be standardised and documented in future revisions. Until then, if a clear meaning is required
                #     please contact Saturn South.
                6, 
                
                # Plain text representation of the download status
                # - The meaning of this value is currently 'black magic'.
                #   - Values will be standardised and documented in future revisions. Until then, if a clear meaning is required
                #     please contact Saturn South.
                "GET_FILE_RESP"
            ],
            
            # The name of the file being downloaded
            # - This field is included if it is relevant (i.e. if a file is being processed, or downloaded, but not if requesting a manifest for example)
            M.F.ESB.Update.DownloadFilename_1_1 : "my_update_file.zigbee",
            
            # The path that the file is being downloaded to
            # - This field is included if it is relevant (i.e. if a file is being processed, or downloaded, but not if requesting a manifest for example)
            M.F.ESB.Update.DownloadSavepath_1_1 : "/downloads/my_update_file.zigbee-1",
            
            # The MD5 hash of the file being downloaded as provided by the server
            # - This field is included if it is relevant and was provided by the server (i.e. if a file is being processed, or downloaded, but not if requesting a manifest for example)
            M.F.ESB.Update.DownloadMD5_1_1 : "ab512a78ec5ae24c40c491d0e750f1f3",
            
            # The size of the file being downloaded in bytes
            # - This field is included if it was provided by the server (otherwise -1)
            M.F.ESB.Update.DownloadSizeBytes_1_1 : 45036,
            
            # The number of bytes downloaded
            # - This field is included if it is relevant (i.e. if a file is being processed, or downloaded, but not if requesting a manifest for example)
            M.F.ESB.Update.DownloadDoneBytes_1_1 : 2404
        },
    },
    
    # Data about OTA updates registered on the ESBox
    # - This field is included if M.F.ESB.Update.OTARegistered_1_1 was True in the requesting GetUpdateStatus_1_1 message.
    M.F.ESB.Update.OTARegistered_1_1 : {
    
        # A list of all registered OTA updates (unordered)
        # - One list element per registered update
        # - More fields may be added to M.F.ESB.Update.CurrentDownloads_1_1 in future revisions of the version 1.1 API.
        M.F.ESB.Update.Updates_1_1 : [
            {
                # The path of the update on the ESBox's file system
                M.F.ESB.Update.Path_1_1 : "path/of/update_file.zigbee",
                
                # The expiry time of the update (seconds since Jan 1 1970)
                M.F.ESB.Update.ExpiryTime_1_1 : 1424570900,
                
                # The time that the update was added to the ESBox (seconds since Jan 1 1970)
                M.F.ESB.Update.AddedTime_1_1 : 1423966100
            },
            {
                M.F.ESB.Update.Path_1_1 : "path/of/other_update_file.zigbee",
                M.F.ESB.Update.ExpiryTime_1_1 : 1424570840,
                M.F.ESB.Update.AddedTime_1_1 : 1423966040
            }
        ],
    },
    
    # Data about pending ESBox updates
    # - This field is included if M.F.ESB.Update.ESBoxAllPending_1_1 was True in the requesting GetUpdateStatus_1_1 message.
    # - Not currently implemented
    M.F.ESB.Update.ESBoxAllPending_1_1 : {}
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendDeviceList
# Message ID: M.SS_ESB.E.SendDeviceList
# Queue Type: Single
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
# Purpose: Returns a summary of devices known to the ESBox and information about them.
#       - This message has been expanded from previous versions of API 1.0 in a backwards compatible way.
#           - The change concerns the action of the M.F.Nwk.Detailed field in M.SS_ESB.E.GetDeviceList, which triggers this message.
#           - The flag (M.F.Nwk.Detailed) is now supported, and if set, new fields not in previous versions of API 1.0 will be included.
ex_1_0__SS_ESB_E_SendDeviceList = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendDeviceList,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # A list of devices known to the ESBox
    # - Each element of the list is an object representing a single device.
    M.F.Nwk.DeviceList : [
        {
            # The device's HAN address
            M.F.Nwk.DevIEEE : "001BC502B0101C9C",
            
            # The device's Model ID
            M.F.Nwk.ModelID : "SS9007.2.0_6000_2290_SSHA_R",
            
            # The device's manufacturer's name
            M.F.Nwk.ManufacturerName : "Saturn South",
            
            # The device's location description
            M.F.Nwk.LocationDescription : "Kitchen",
            
            # The device's status
            # - Values:
            #   - M.V.Nwk.Online                - the device is online.
            #   - M.V.Nwk.Refresh               - information about the device is currently being refreshed.
            #   - M.V.Nwk.Offline               - the device is offline.
            #   - M.V.Nwk.Unknown               - the status of the device is not known.
            M.F.Nwk.OnlineStatus : M.V.Nwk.Online,
            
            # The device's type
            # - Values:
            #   - M.V.Nwk.ZigBeeCoordinator     - the device is a zigbee coordinator.
            #   - M.V.Nwk.ZigBeeRouter          - the device is a zigbee router.
            #   - M.V.Nwk.ZigBeeEndDevice       - the device is a zigbee end device.
            #   - M.V.Nwk.Unknown               - the type of device is unknown.
            M.F.Nwk.NodeType : M.V.Nwk.ZigBeeEndDevice,
            
            # When the device first joined the network (seconds since 1 Jan 1970)
            M.F.Nwk.JoinTime : 1424571239,
            
            # When the device last contacted the coordinator (seconds since 1 Jan 1970)
            M.F.Nwk.LastContact : 1424572421,
            
            # When the device last rejoined the network (seconds since 1 Jan 1970)
            M.F.Nwk.LastRejoinTime : 1424572282,
            
            # Whether this device is the ESBox's coordinator (i.e. the ESBox itself)
            # - Only present if 1.
            # - Value:
            #   - always 1 if present.
            # - This field uses a _1_1 suffix as it is 'technically' only available in API v1.1.
            #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
            M.F.Nwk.IsCoordForThisESBox_1_1 : 1,
            
            # Whether permit joining is enabled on the ESBox's coordinator
            # - Only present if this device is the ESBox's coordinator.
            # - Value:
            #   - 0         - not enabled.
            #   - 1         - enabled.
            # - This field uses a _1_1 suffix as it is 'technically' only available in API v1.1.
            #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
            M.F.Nwk.PermitJoiningEnabled_1_1 : 0,
                    
            # Information about an LQI test currently running with this end device
            # - This field is only present if an LQI test is currently running for this end device.
            # - This field is only present if the device is not the ESBox's coordinator.
            # - This field is new compared to previous API v1.0 versions of this message.
            M.F.Nwk.LQI : {
            
                # The latest tested link quality of the signal received by the coordinator from the end device
                # - The value provided here is the signal quality of the 'last hop' of the transmission in the case of multiple
                #   hops, such as if a router were relaying the signal instead of the end device communicating directly with the
                #   coordinator.
                #   - In the case that multiple hops are present in the signal path, this value therefore represents the quality
                #     of the signal from the router to the coordinator, and not the quality of the link from the end device.
                # - Value:
                #   - The integer provided is the raw LQI value.
                #   - To convert to dB use the formula: dB = ( raw_lqi / 3 ) - 100
                # - This field uses a _1_1 suffix as it is 'technically' only available in API v1.1.
                #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
                M.F.Nwk.CoordLQI_1_1 : 130,
                
                # The latest tested link quality of the signal received by the end device from the coordinator
                # - The value provided here is the signal quality of the 'last hop' of the transmission in the case of multiple
                #   hops, such as if a router were relaying the signal instead of the end device communicating directly with the
                #   coordinator.
                #   - In the case that multiple hops are present in the signal path, this value therefore represents the quality
                #     of the signal from the router to the end device, and not the quality of the link from the coordinator.
                #   - In the case that multiple hops are present in the signal path, this value will give the best indication of
                #     the link quality to the end device.
                # - Value:
                #   - The integer provided is the raw LQI value.
                #   - To convert to dB use the formula: dB = ( raw_lqi / 3 ) - 100
                # - This field uses a _1_1 suffix as it is 'technically' only available in API v1.1.
                #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
                M.F.Nwk.EndDeviceLQI_1_1 : 128
            },
            
            # Information about any updates currently running for this end device
            # - This field is only present if an update is currently running for this end device.
            # - This field is new compared to previous API v1.0 versions of this message.
            # - This field and its children use _1_1 suffixes as this field is 'technically' only available in API v1.1.
            #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
            M.F.ESB.Update.CurrentOTAUpdates_1_1 : {
            
                # Percentage completeness of the update
                M.F.ESB.Update.OTAPercentComplete_1_1 : 85,
                
                # Estimated number of seconds remaining before the update is complete
                M.F.ESB.Update.OTAEstimatedSecondsRemaining_1_1 : 17
            },
            
            # Detailed information about the device
            # - This field is included only if M.F.Nwk.Detailed was True in the triggering M.SS_ESB.E.GetDeviceList message.
            M.F.Nwk.Detailed : {
                
                # A list of neighbours for this device
                # - Each list element represents a single neighbour.
                # - This field and its children use _1_1 suffixes (except LQI) as this field is 'technically' only available in API v1.1.
                #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
                M.F.Nwk.Neighbours_1_1 : [
                    {
                        # The neighbour's PAN address
                        M.F.Nwk.PANAddr_1_1 : "001BC502B0100359",
                        
                        # The neighbour's HAN address
                        M.F.Nwk.DevIEEE : "001BC502B0100BE2",
                        
                        # The neighbour's network address
                        M.F.Nwk.NwkAddr_1_1 : "8A02",
                        
                        # The neighbour's device properties:
                        # - Bitfield (8 bits):
                        #   - Bits 0..1     - Device type.
                        #       - 0             - Zigbee coordinator.
                        #       - 1             - Zigbee router.
                        #       - 2             - Zigbee end device.
                        #   - Bit  2        - 1 if zigbee Receiver is always on.
                        #   - Bits 3..5     - Relationship.
                        #       - 0             - Is a parent.
                        #       - 1             - Is a child.
                        #       - 2             - Is a sibling.
                        #       - 3             - Reserved.
                        #       - 4             - Reserved.
                        #       - 5             - Reserved.
                        #       - 6             - Reserved.
                        #   - Bit 6         - Link Status.
                        #       - 0             - Link bad.
                        #       - 1             - Link ok.
                        #   - Bit 7         - Reserved.
                        # - This field may be changed/expanded to make it easier to parse in the future.
                        M.F.Nwk.DeviceProperties_1_1 : 37,
                        
                        # Is joining permitted by the neighbour?
                        # - Value:
                        #   - 0: no.
                        #   - 1: yes.
                        M.F.Nwk.PermitJoiningEnabled_1_1 : 0,
                        
                        # The neighbour's depth in the network
                        # - Value:
                        #   - normally this represents the depth away from the coordinator (in hops).
                        #   - 255: value is not available.
                        M.F.Nwk.Depth_1_1 : 255,
                        
                        # The link quality of the last signal received by the router (or coordinator) from this neighbour
                        # - Value:
                        #   - The integer provided is the raw LQI value.
                        #   - To convert to dB use the formula: dB = ( raw_lqi / 3 ) - 100
                        M.F.Nwk.LQI : 213
                    }
                ]
            }
        }
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendDeviceList_1_1
# Message ID: M.SS_ESB.E.SendDeviceList_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns a summary of devices known to the ESBox and information about them.
#       - The functionality of this message may be expanded in the future.
ex_1_1__SS_ESB_E_SendDeviceList_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendDeviceList_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # A list of devices known to the ESBox
    # - Each element of the list is an object representing a single device.
    M.F.Nwk.DeviceList_1_1 : [
        {
            # The device's HAN address
            M.F.Nwk.HAN_1_1 : "001BC502B0101C9C",
            
            # The device's Model ID
            M.F.Nwk.ModelID_1_1 : "SS9007.2.0_6000_2290_SSHA_R",
            
            # The device's manufacturer's name
            M.F.Nwk.ManufacturerName_1_1 : "Saturn South",
            
            # The device's location description
            M.F.Nwk.LocationDescription_1_1 : "Kitchen",
            
            # The device's status
            # - Values:
            #   - M.V.Nwk.Online                - the device is online.
            #   - M.V.Nwk.Refresh               - information about the device is currently being refreshed.
            #   - M.V.Nwk.Offline               - the device is offline.
            #   - M.V.Nwk.Unknown               - the status of the device is not known.
            M.F.Nwk.OnlineStatus_1_1 : M.V.Nwk.Online_1_1,
            
            # The device's type
            # - Values:
            #   - M.V.Nwk.ZigBeeCoordinator     - the device is a zigbee coordinator.
            #   - M.V.Nwk.ZigBeeRouter          - the device is a zigbee router.
            #   - M.V.Nwk.ZigBeeEndDevice       - the device is a zigbee end device.
            #   - M.V.Nwk.Unknown               - the type of device is unknown.
            M.F.Nwk.NodeType_1_1 : M.V.Nwk.ZigBeeEndDevice,
            
            # When the device first joined the network (seconds since 1 Jan 1970)
            M.F.Nwk.JoinTime_1_1 : 1424571239,
            
            # When the device last contacted the coordinator (seconds since 1 Jan 1970)
            M.F.Nwk.LastContact_1_1 : 1424572421,
            
            # When the device last rejoined the network (seconds since 1 Jan 1970)
            M.F.Nwk.LastRejoinTime_1_1 : 1424572282,
            
            # Whether this device is the ESBox's coordinator (i.e. the ESBox itself)
            # - Only present if 1.
            # - Value:
            #   - always 1 if present.
            M.F.Nwk.IsCoordForThisESBox_1_1 : 1,
            
            # Whether permit joining is enabled on the ESBox's coordinator
            # - Only present if this device is the ESBox's coordinator.
            # - Value:
            #   - 0         - not enabled.
            #   - 1         - enabled.
            M.F.Nwk.PermitJoiningEnabled_1_1 : 0,
            
            # Information about an LQI test currently running with this end device
            # - This field is only present if an LQI test is currently running for this end device.
            # - This field is only present if the device is not the ESBox's coordinator.
            # - This field is new compared to previous API v1.0 versions of this message.
            M.F.Nwk.LQI : {
            
                # The latest tested link quality of the signal received by the coordinator from the end device
                # - The value provided here is the signal quality of the 'last hop' of the transmission in the case of multiple
                #   hops, such as if a router were relaying the signal instead of the end device communicating directly with the
                #   coordinator.
                #   - In the case that multiple hops are present in the signal path, this value therefore represents the quality
                #     of the signal from the router to the coordinator, and not the quality of the link from the end device.
                # - Value:
                #   - The integer provided is the raw LQI value.
                #   - To convert to dB use the formula: dB = ( raw_lqi / 3 ) - 100
                # - This field uses a _1_1 suffix as it is 'technically' only available in API v1.1.
                #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
                M.F.Nwk.CoordLQI_1_1 : 130,
                
                # The latest tested link quality of the signal received by the end device from the coordinator
                # - The value provided here is the signal quality of the 'last hop' of the transmission in the case of multiple
                #   hops, such as if a router were relaying the signal instead of the end device communicating directly with the
                #   coordinator.
                #   - In the case that multiple hops are present in the signal path, this value therefore represents the quality
                #     of the signal from the router to the end device, and not the quality of the link from the coordinator.
                #   - In the case that multiple hops are present in the signal path, this value will give the best indication of
                #     the link quality to the end device.
                # - Value:
                #   - The integer provided is the raw LQI value.
                #   - To convert to dB use the formula: dB = ( raw_lqi / 3 ) - 100
                # - This field uses a _1_1 suffix as it is 'technically' only available in API v1.1.
                #   It's included here because it's useful and should be backwards compatible with compliant ESCo implementations.
                M.F.Nwk.EndDeviceLQI_1_1 : 128
            },
            
            # Information about any updates currently running for this end device
            # - This field is only present if an update is currently running for this end device.
            # - This field is new compared to previous API v1.0 versions of this message.
            M.F.ESB.Update.CurrentOTAUpdates_1_1 : {
            
                # Percentage completeness of the update
                M.F.ESB.Update.OTAPercentComplete_1_1 : 85,
                
                # Estimated number of seconds remaining before the update is complete
                M.F.ESB.Update.OTAEstimatedSecondsRemaining_1_1 : 17
            },
            
            # Detailed information about the device
            # - This field is included only if M.F.Nwk.Detailed_1_1 was True in the triggering M.SS_ESB.E.GetDeviceList_1_1 message.
            M.F.Nwk.Detailed_1_1 : {
                
                # A list of neighbours for this device
                # - Each list element represents a single neighbour.
                M.F.Nwk.Neighbours_1_1 : [
                    {
                        # The neighbour's PAN address
                        M.F.Nwk.PANAddr_1_1 : "001BC502B0100359",
                        
                        # The neighbour's HAN address
                        M.F.Nwk.HAN_1_1 : "001BC502B0100BE2",
                        
                        # The neighbour's network address
                        M.F.Nwk.NwkAddr_1_1 : "8A02",
                        
                        # The neighbour's device properties:
                        # - Bitfield (8 bits):
                        #   - Bits 0..1     - Device type.
                        #       - 0             - Zigbee coordinator.
                        #       - 1             - Zigbee router.
                        #       - 2             - Zigbee end device.
                        #   - Bit  2        - 1 if zigbee Receiver is always on.
                        #   - Bits 3..5     - Relationship.
                        #       - 0             - Is a parent.
                        #       - 1             - Is a child.
                        #       - 2             - Is a sibling.
                        #       - 3             - Reserved.
                        #       - 4             - Reserved.
                        #       - 5             - Reserved.
                        #       - 6             - Reserved.
                        #   - Bit 6         - Link Status.
                        #       - 0             - Link bad.
                        #       - 1             - Link ok.
                        #   - Bit 7         - Reserved.
                        # - This field may be changed/expanded to make it easier to parse in the future.
                        M.F.Nwk.DeviceProperties_1_1 : 37,
                        
                        # Is joining permitted by the neighbour?
                        # - Value:
                        #   - 0: no.
                        #   - 1: yes.
                        M.F.Nwk.PermitJoiningEnabled_1_1 : 0,
                        
                        # The neighbour's depth in the network
                        # - Value:
                        #   - normally this represents the depth away from the coordinator (in hops).
                        #   - 255: value is not available.
                        M.F.Nwk.Depth_1_1 : 255,
                        
                        # The link quality of the last signal received by the router (or coordinator) from this neighbour
                        # - Value:
                        #   - The integer provided is the raw LQI value.
                        #   - To convert to dB use the formula: dB = ( raw_lqi / 3 ) - 100
                        M.F.Nwk.LQI : 213
                    }
                ]
            }
        }
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendDeviceManagementResult_1_1
# Message ID: M.SS_ESB.E.SendDeviceManagementResult_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the result of a M.SS_ESB.E.ExecuteDeviceManagementOperation_1_1 message.
#       - The functionality of this message may be expanded in the future.
#       - This function may be merged into a unified 'result' function in the future.
ex_1_1__SS_ESB_E_SendDeviceManagementResult_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendDeviceManagementResult_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The result of the operation
    # - Value (integer):
    #   - M.V.Nwk.Op.Err.SUCCESS            - the operation succeeded.
    #   - M.V.Nwk.Op.Err.UNKNOWN_ERROR      - an unknown error occurred.
    #   - M.V.Nwk.Op.Err.NO_OP              - no operation was provided.
    #   - M.V.Nwk.Op.Err.BAD_OP             - the operation provided was invalid.
    #   - M.V.Nwk.Op.Err.OP_FAILED          - the operation failed.
    #   - other                             - an unknown error occurred.
    M.F.Gen.Result_1_1 : M.V.Nwk.Op.Err.SUCCESS,
    
    # The operation that was performed
    # - Only present if available (this should always be present except for rare errors).
    # - Value:
    #   - M.V.Nwk.Op.ScanDeviceList_1_1             - an operation to trigger a scan of the device list was requested.
    #   - M.V.Nwk.Op.RebuildDeviceList_1_1          - an operation to trigger a rebuild of the device list was requested.
    #   - M.V.Nwk.Op.PermitJoining_1_1              - an operation to request the coordinator to permit joining was requested.
    #   - M.V.Nwk.Op.ClearOTAUpdateRegistry_1_1     - an operation to clear all registered OTA updates was requested.
    #   - M.V.Nwk.Op.ClearDeviceRegistry_1_1        - an operation to clear the device list was requested.
    #   - M.V.Nwk.Op.FactoryReset_1_1               - an operation to clear all registered OTA updates and the device list  was requested.
    #   - M.V.Nwk.Op.LocateEndDevice_1_1            - an operation to locate an end device was requested.
    #   - M.V.Nwk.Op.LeaveEndDevice_1_1             - an operation to request an end device to leave the network was requested.
    #   - M.V.Nwk.Op.RebootEndDevice_1_1            - an operation to request an end device to reboot was requested.
    #   - M.V.Nwk.Op.RefreshEndDevice_1_1           - an operation to request a refresh of an end device was requested.
    #   - M.V.Nwk.Op.LQITestEndDevice_1_1           - an operation to request an LQI test to be started for an end device was requested.
    #   - M.V.Nwk.Op.OverrideReportInterval_1_1     - an operation to change the reporting interval for end devices was requested.
    #   - other                                     - an invalid operation was requested.
    M.F.Gen.Operation_1_1 : M.V.Nwk.Op.ScanDeviceList_1_1,
    
    # Details of the result as a human-readable string
    # - Only present if relevant for the result (typically not provided).
    M.F.Gen.Details_1_1 : "Ok",
    
    # Details of the error
    # - Only present if relevant for the result (typically not provided).
    M.F.ESB.Error_1_1 : "No error"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendStatus_1_1
# Message ID: M.SS_ESB.E.SendStatus_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the current status of the ESBox.
#       - Not implemented.
#       - Will be implemented in future.
#       - Intended functionality may be merged/split with M.SS_ESB.E.SendErrors_1_1.
ex_1_1__SS_ESB_E_SendStatus_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendStatus_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 } # SS_ESB Cluster
}
    

# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendTerminalOutput_1_1
# Message ID: M.SS_ESB.E.SendTerminalOutput_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the output of the ESBox's terminal.
ex_1_1__SS_ESB_E_SendTerminalOutput_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendTerminalOutput_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The terminal output data
    M.F.Dat.Data_1_1 : {
    
        # A list of lines from the terminal scrollback buffer in chronological order
        # - Each list element is one terminal line.
        # - The number of lines sent in the message may be limited and not represent all the remaining terminal lines.
        #
        # A quick explanation about the data returned:
        # - The terminal is arranged into lines, each line has a unique, sequential id (starting from 0 at ESBox startup).
        # - This message returns lines depending on the unique id provided by the value of the M.F.ESB.TermUid_1_1 field
        #   in the requesting M.SS.ESB_E.GetTerminalOutput_1_1 message and the current state of the terminal.
        # - Each line in the scrollback buffer will be checked and that line will be sent if:
        #   - (uid - 1) > newestline.uid
        #       - all lines will be sent in this case
        #   - uid <= line.uid
        #       - where uid is the uid sent by this request
        #       - line.uid is the uid of the line being tested for whether it should be sent
        #       - newestline.uid is the uid of the newest line in the scrollback buffer
        #
        # - This means that the intended general pattern to follow for reading the terminal is:
        #   1/ request uid == 0
        #   2/ request uid == largest uid received in SendTerminalOutput_1_1 + 1
        #           (usually this will yield no new lines)
        #   3/ if uid decreases, then the ESBox has likely reset
        #           (or there is extreme latency or load on the ESBox)
        #       - in this case, the ESBox will have sent its entire scrollback buffer
        #           (typically a maximum of 80 lines).
        #       - in this case, continue as normal with step 2 (the uid requested should also decrease)
        M.F.ESB.Term_1_1 : [
            {
                # The string that was printed to the terminal
                M.F.ESB.TermData_1_1 : "Sample terminal line",
                
                # The foreground colour for this line
                # - Value:
                #   - hex colour string, i.e. #RRGGBB or #RGB
                #   - empty: use default foreground colour.
                M.F.ESB.TermForegroundColor_1_1 : "",
                
                # The background colour for this line
                # - Value:
                #   - hex colour string, i.e. #RRGGBB or #RGB.
                #   - empty: use default background colour.
                M.F.ESB.TermBackgroundColor_1_1 : "",
                
                # Is this line bold?
                # - Value:
                #   - 1: yes.
                #   - 0: no.
                M.F.ESB.TermBold_1_1 : 0,
                
                # Is this line italic?
                # - Value:
                #   - 1: yes.
                #   - 0: no.
                M.F.ESB.TermItalic_1_1 : 0,
                
                # Leading character(s) to print before the line
                # - Value:
                #   - present: print this string before the line.
                #   - empty/missing: print the default string before the line.
                M.F.ESB.TermLeading_1_1 : "",
                
                # Is this line the start of a new logical line?
                # - If a line is printed and is too long to fit in the width of a line it is split up into multiple lines in memory
                #   (i.e. takes up multiple uids), but logically it is kept together by marking the logical start of each line with 
                #   a 1 in this field. Subsequent 'tails' of logical lines are marked with a 0.
                M.F.ESB.TermNewline_1_1 : 1,
                
                # Priority value for each line
                # - This value can be used for filtering as well as for setting the default style for each line.
                # - Value:
                #   - 0: normal priority.
                #   - 1: 'meta' priority.
                #       - used for passing non-printed commands to the terminal client i.e. the wedit open link
                #   - 2: debug priority.
                #   - 3: notification priority.
                #   - 4: warning priority.
                #   - 5: error priority.
                #   - 6: fatal error priority.
                M.F.ESB.TermPriority_1_1 : 2,
                
                # The unique ID of the line
                M.F.ESB.TermUid_1_1 : 283
            }
        ]
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendDir_1_1
# Message ID: M.SS_ESB.E.SendDir_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the contents of a directory.
#           - This message is not completely finalised and may change in the future.

# - Example for Error:
ex_1_1__Error__SS_ESB_E_SendDir_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendDir_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Directory list data
    M.F.ESB.Dir : {
        
        # The path that was requested to be listed
        M.F.ESB.Filesystem.Path_1_1 : "/dir/to/list",
        
        # The reason for the error as human-readable text
        # - This field is only present if there was an error.
        # - Value:
        #   - "MALLOC_FAILED":  Failed allocating memory
        #   - "OPEN_FAILED":    Failed reading the directory
        # - Note: these constants will be standardised in the future.
        M.F.ESB.Error_1_1 : "OPEN_FAILED",
        
        # Detail for M.F.ESB.Error_1_1 == "OPEN_FAILED"
        # - This field is only present if M.F.ESB.Error_1_1 == "OPEN_FAILED".
        # - Value:
        #   - See FatFS FRESULT
        M.F.ESB.Filesystem.Code_1_1 : 5
    }
}

# - Example for successful operation:
ex_1_1__Success__SS_ESB_E_SendDir_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendDir_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # Directory list data
    M.F.ESB.Dir : {
        
        # The path that was requested to be listed
        M.F.ESB.Filesystem.Path_1_1 : "/dir/to/list",
        
        # A list of all entries in the target directory
        # - Each list element is one entry in the target directory.
        # - The entries for the current and parent directory are not listed (. and .. respectively).
        M.F.ESB.Filesystem.List_1_1 : [
            {
                # Full example (this isn't actually possible in reality).
                
                # The name of the entry
                M.F.ESB.Filesystem.Name_1_1 : "full_example",
                
                # The time that the entry was last modified
                # - Value:
                #   - Bitfield (16-bit):
                #       - Bits 0..4     - Seconds/2 (0-29)
                #       - Bits 5..10    - Minutes   (0-59)
                #       - Hours 11..15  - Hours     (0-23)
                #       - E.g. 9441:
                #           - 00100 100111 00001
                #           -     4     39     1
                #           -           04:39:02
                M.F.ESB.Filesystem.Time_1_1 : 9441,
                
                # The date that the entry was last modified
                # - Value:
                #   - Bitfield (16-bit):
                #       - Bits 0..4     - Day (1-31)
                #       - Bits 5..8     - Month (1-12)
                #       - Bits 9..15    - Year (0 = 1980, 119 = 2099)
                #       - E.g. 17970:
                #           - 0100011 0001 10010
                #           -      35    1    18
                #           -    2015, Jan  18th
                M.F.ESB.Filesystem.Date_1_1 : 17970,
                
                # The following fields expose the attributes of the directory entry.
                # A good, quick summary of their meanings is available on wikipedia: http://en.wikipedia.org/wiki/Design_of_the_FAT_file_system#attributes
                
                # Is the entry read only?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsReadOnly_1_1 : 1,
                
                # Is the entry marked as hidden?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsHidden_1_1 : 1,
                
                # Is the entry marked as a system file?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsSystem_1_1 : 1,
                
                # Is the entry marked as a volume label?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsVolumeLabel_1_1 : 1,
                
                # Is the entry a long filename entry?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsLongFileNameEntry_1_1 : 1,
                
                # Is the entry a sub-directory?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsDirectory_1_1 : 1,
                
                # Is the entry an archive?
                # - Only present if value is 1
                # - Value:
                #   - Always 1
                M.F.ESB.Filesystem.IsArchive_1_1 : 1,
                
                # The size of the entry in bytes
                # - Only present if the entry has a size (files)
                M.F.ESB.Filesystem.Size_1_1 : 504329
            },
            {
            
                # Example of a directory.
                M.F.ESB.Filesystem.Name_1_1 : "example_dir",
                M.F.ESB.Filesystem.Time_1_1 : 9441,
                M.F.ESB.Filesystem.Date_1_1 : 17970,
                M.F.ESB.Filesystem.IsDirectory_1_1 : 1
            },
            {
            
                # Example of a file.
                M.F.ESB.Filesystem.Name_1_1 : "example.file",
                M.F.ESB.Filesystem.Time_1_1 : 3399,
                M.F.ESB.Filesystem.Date_1_1 : 17961,
                M.F.ESB.Filesystem.IsArchive_1_1 : 1,
                M.F.ESB.Filesystem.Size_1_1 : 504329
            }
        ]
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendFile_1_1
# Message ID: M.SS_ESB.E.SendFile_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the contents of a file.
#           - This message is not completely finalised and may change in the future.

# - Example for Error:
ex_1_1__Error__SS_ESB_E_SendFile_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendFile_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # File data
    M.F.ESB.File_1_1 : {
    
        # The requested path
        M.F.ESB.Filesystem.Path_1_1 : "/file/to/send",
        
        # The reason for the error as human-readable text
        # - This field is only present if there was an error.
        # - Value:
        #   - "INTERNAL_ERROR":     Internal failure (bad function argument, internal inconsistency etc.)
        #   - "MALLOC_FAILED":      Failed allocating memory
        #   - "DOES_NOT_EXIST":     The requested path does not exist
        #   - "LOCKED":             The requested file is currently locked and cannot be read
        #   - "OPEN_FAILED":        Failed opening the file
        # - Note: these constants will be standardised in the future.
        M.F.ESB.Error_1_1 : "OPEN_FAILED",
        
        # Detail for M.F.ESB.Error_1_1 == "OPEN_FAILED"
        # - This field is only present if M.F.ESB.Error_1_1 == "OPEN_FAILED".
        # - Value:
        #   - See FatFS FRESULT
        M.F.ESB.Filesystem.Code_1_1 : 5
    }
}

# - Example for successful operation:
ex_1_1__Success__SS_ESB_E_SendFile_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendDir_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster

    # File data
    M.F.ESB.File_1_1 : {
    
        # The requested path
        M.F.ESB.Filesystem.Path_1_1 : "/file/to/send",
        
        # Details about the file being sent
        # - See 'Full example' from ex_1_1__Success__SS_ESB_E_SendDir_1_1 -> M.F.ESB.Dir -> M.F.ESB.Filesystem.List_1_1 
        #   for details of this field.
        M.F.Gen.Details_1_1 : {
            M.F.ESB.Filesystem.Name_1_1 : "send",
            M.F.ESB.Filesystem.Time_1_1 : 3399,
            M.F.ESB.Filesystem.Date_1_1 : 17961,
            M.F.ESB.Filesystem.IsArchive_1_1 : 1,
            M.F.ESB.Filesystem.Size_1_1 : 504329
        },
        
        # The contents of the file
        # - The contents of this field is encoded in base64.
        M.F.ESB.Filesystem.Contents_1_1 : "dGhpcyBpcyBhIHRlc3QgOik="
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendFilesystemOperationResult_1_1
# Message ID: M.SS_ESB.E.SendFilesystemOperationResult_1_1
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns the result of a M.SS_ESB.E.ExecuteFilesystemOperation_1_1 message.
#       - The functionality of this message may be expanded in the future.
#       - This function may be merged into a unified 'result' function in the future.
ex_1_1__SS_ESB_E_SendFilesystemOperationResult_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendFilesystemOperationResult_1_1,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The result of the operation
    # - Value (integer):
    #   - See FatFS FRESULT
    M.F.Gen.Result_1_1 : 0,
    
    # The operation that was performed
    # - Only present if available (this should always be present except for rare errors).
    # - Value:
    #   - M.V.Filesystem.MakeDir_1_1                - an operation to create a directory was requested.
    #   - M.V.Filesystem.Remove_1_1                 - an operation to remove a file or directory was requested.
    #   - M.V.Filesystem.MakeFile_1_1               - an operation to create a file was requested.
    #   - M.V.Filesystem.WriteFile_1_1              - an operation to write to a file was requested.
    #   - M.V.Filesystem.WriteFileFromRemote_1_1    - an operation to write to a file from a remote server was requested.
    #   - other                                     - an invalid operation was requested.
    M.F.Gen.Operation_1_1 : M.V.Filesystem.MakeDir_1_1,
    
    # Details of the result as a human-readable string
    # - Only present if relevant for the result (typically not provided).
    M.F.Gen.Details_1_1 : "Ok",
    
    # Details of the error
    # - Only present if relevant for the result (typically not provided).
    M.F.ESB.Error_1_1 : "No error"
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendData
# Message ID: M.SS_ESB.E.SendData
# Queue Type: Single
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
# Purpose: Returns data as requested by M.SS_ESB.E.GetData

# - Example for M.F.Dat.Source == M.V.Dat.Source.Sdb:
ex_1_0__Sdb__SS_ESB_E_SendData = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendData,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster
    
    # The source of the data being sent
    # - Value:
    #   - M.V.Dat.Source.Sdb    - data is sourced from the stream database
    #   - other                 - not supported / not implemented in version 1.0
    M.F.Dat.Source : M.V.Dat.Source.Sdb,
    
    # The data being sent
    M.F.Dat.Data : {
    
        # The FIFO to that the data was read from
        # - Values: 0-3:
        #   - 0 : 'ESCo' FIFO
        #   - 1 : 'Web-app' FIFO (web-app may use this FIFO, so it is not recommended for use)
        #   - 2 : 'User-1' FIFO
        #   - 3 : 'User-2' FIFO
        #   - N.b. these definitions will be added to SSMessages at a later date
        M.F.Dat.Sdb.Fifo : 2,
        
        # A list of cells read from the stream database
        # - Each list element represents a single cell.
        # - Cells are returned in the order they are read, which is the order they were written.
        #   - Timestamps can be used to reconstruct the actual order of the cells in the rare case that they
        #     were logged out of order.
        # - When cells are read from a FIFO, that FIFO is advanced to ensure that that data can not be read again from that
        #   FIFO. That data may still be readable in another FIFO.
        # - In future, API version 1.1 functions may allow rewinding or skipping in FIFOs to some degree.
        #
        #
        # About the data sent back from the stream database:
        # - The stream database records data as it is received by the ESBox from end devices.
        # - Each time some attribute data is received from an end device the stream database may log those attributes.
        # - The attribute data is logged in the order it is received.
        # - Some attribute data may be discarded depending on stream database's settings (filtering settings and so on).
        # - When data is logged to the stream database, a number of attributes are logged at the same time. These attributes
        #   will share the same source device, endpoint, manufacturer and cluster. Those attributes are stored in a structure
        #   termed a 'cell'.
        # - When data is read and sent from the stream database, the base unit is a cell. Multiple cells can be sent per
        #   SendData message.
        # - When sending cells, in order to save bandwidth a basic encoding scheme can be employed depending on the settings
        #   used in the requesting GetData message.
        #
        #
        # Description of settings, their effects and how to properly read the Cells in order:
        #
        # - M.F.Dat.Sdb.NCells
        #   - The maximum number of cells to read. Fewer cells may be read.
        #
        # - M.F.Dat.Sdb.Fifo
        #   - Which FIFO to read from. See M.F.Dat.Sdb.Fifo documentation in this example message.
        #
        # - M.F.Dat.Sdb.DelIeee
        #   - If disabled:
        #       - print M.F.Nwk.Short.DevIEEE field in every cell.
        #   - If enabled:
        #       - print M.F.Nwk.Short.DevIEEE field in the first cell.
        #       and
        #       - print M.F.Nwk.Short.DevIEEE field in the each cell with a different source device to the previous cell.
        #   - See description of M.F.Nwk.Short.DevIEEE in the example cells.
        #
        # - M.F.Dat.Sdb.DelEP
        #   - If disabled:
        #       - print M.F.Nwk.Short.EndpointID field in every cell.
        #   - If enabled:
        #       - print M.F.Nwk.Short.EndpointID field in the first cell.
        #       and
        #       - print M.F.Nwk.Short.EndpointID field in the each cell with a different source endpoint to the previous cell.
        #   - See description of M.F.Nwk.Short.EndpointID in the example cells.
        #
        # - M.F.Dat.Sdb.DelClu
        #   - If disabled:
        #       - print M.F.Dat.DataClusterManufacturer and M.F.Dat.DataClusterId fields in every cell.
        #   - If enabled:
        #       - print M.F.Dat.DataClusterManufacturer and M.F.Dat.DataClusterId fields in the first cell.
        #       and
        #       - print M.F.Dat.DataClusterManufacturer and M.F.Dat.DataClusterId fields in the each cell with a different source cluster
        #         (id and/or manufacturer) to the previous cell.
        #   - See descriptions of M.F.Dat.DataClusterManufacturer and M.F.Dat.DataClusterId in the example cells.
        #
        # - M.F.Dat.Sdb.DelTime
        #   - If disabled:
        #       - print M.F.Dat.Time field in every cell.
        #   - If enabled:
        #       - print M.F.Dat.Time field in the first cell.
        #       and
        #       - print M.F.Dat.DeltaTime field in every other cell, except where the cell's time is the same as the previous cell's.
        #   - See descriptions of M.F.Dat.Time and M.F.Dat.DeltaTime in the example cells.
        M.F.Dat.Sdb.Cells : [
            {
                # The HAN address of the source device for this cell
                M.F.Nwk.Short.DevIEEE : "001BC502B0100314",
                
                # The source endpoint for this cell
                M.F.Nwk.Short.EndpointID : 10,
                
                # The source cluster manufacturer for this cell
                M.F.Dat.DataClusterManufacturer : 0,
                
                # The source cluster id for this cell
                M.F.Dat.DataClusterId : 1794,
                
                # The time that this cell was generated
                # Value:
                # - seconds since 1 Jan 1970
                M.F.Dat.Time : 1405705444,
                
                # The data, a list of the attribute IDs, values and types logged in this cell
                # - Each list element represents a single attribute description and value.
                M.F.Dat.Short.Attributes : [
                    {
                        # The ID of the attribute
                        # - This ID is specific to the manufacturer and id of the cluster.
                        # - Please consult the cluster's documentation for the meaning and
                        #   interpretation of the attribute's value.
                        M.F.Dat.Short.AttributeID : 57610,
                        
                        # The attribute's datatype
                        # - Attributes stored by the stream database are normalised into
                        #   a standard set of datatypes for storage. This does not necessarily
                        #   accurately reflect the datatype of the zigbee attribute as sent by the
                        #   end device.
                        # Value:
                        # - M.V.Dat.Type.Int            - the data is a signed integer (64-bit).
                        # - M.V.Dat.Type.Uint           - the data is an unsigned integer (64-bit).
                        # - M.V.Dat.Type.String         - the data is a string.
                        # - M.V.Dat.Type.Byte           - the data is a raw binary blob, it is encoded.
                        #                                 into a base64 and then sent as a string.
                        # - M.V.Dat.Type.Raw            - the data is a string (see M.V.Dat.Type.String).
                        # - M.V.Dat.Type.Timechange     - the data is a timechange: a record of the ESBox's
                        #                                 timebase being changed.
                        #                                   - at this time, timechange data is not
                        #                                     represented or stored by the stream database.
                        #                                   - the value will always be "TIMECHANGE".
                        M.F.Dat.Short.Type : M.V.Dat.Type.Uint,
                        
                        # The attribute's value
                        # - See the cluster's documentation for details on the meaning of the value.
                        # - See M.F.Dat.Short.Type for details on how to read the value.
                        M.F.Dat.Short.Value : 23791
                    }
                ]
            },
            {
                # The time that this cell was generated compared to the previous cell in the list
                # - This value is in seconds since the previous cell in the list.
                # - The value may be negative.
                # - Note that to get an absolute time for any particular cell, it is necessary to read
                #   all of the cells in sequence to calculate their absolute time.
                M.F.Dat.DeltaTime : 56,
                M.F.Dat.Short.Attributes : [
                    {
                        M.F.Dat.Short.AttributeID : 57610,
                        M.F.Dat.Short.Type : M.V.Dat.Type.Uint,
                        M.F.Dat.Short.Value : 23826
                    }
                ]
            }
        ]
    }
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendData(_1_1) 
# Message ID: M.SS_ESB.E.SendData(_1_1)
# Queue Type: Single
# Versions: 1.1+
# Direction: From ESBox (TX)
# Purpose: Returns data as requested by M.SS_ESB.E.GetData_1_1
#           - This message is not completely finalised and may change in the future.
#           - currently uses SendData constant, subsequent releases will use SendData_1_1.

# - Example for M.F.Dat.Source == M.V.Dat.Source.Sdb:
ex_1_1__Sdb__SS_ESB_E_SendData_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendData,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The source of the data being sent
    # - Value:
    #   - M.V.Dat.Source.Sdb                    - data is sourced from the stream database
    #   - M.V.Dat.Source.LatestReadings_1_1     - data is sourced from the latest readings buffer
    #   - other                                 - not supported / not implemented yet in version 1.1
    M.F.Dat.Source : M.V.Dat.Source.Sdb,
    
    # The data being sent
    M.F.Dat.Data_1_1 : {
    
        # The FIFO to that the data was read from
        # - Values: 0-3:
        #   - 0 : 'ESCo' FIFO
        #   - 1 : 'Web-app' FIFO (web-app may use this FIFO, so it is not recommended for use)
        #   - 2 : 'User-1' FIFO
        #   - 3 : 'User-2' FIFO
        #   - N.b. these definitions will be added to SSMessages at a later date
        M.F.Dat.Sdb.Fifo : 2,
    
        # A list of cells read from the stream database
        # - Each list element represents a single cell.
        # - See the documentation for the equivalent M.F.Dat.Sdb.Cells field in ex_1_0__Sdb__SS_ESB_E_SendData for a detailed
        #   description of this field. There are some differences, which are:
        #   - M.F.Dat.Sdb.DelIeee controls printing of the M.F.Nwk.HAN_1_1 instead of the M.F.Nwk.Short.DevIEEE field.
        #   - M.F.Dat.Sdb.DelEP controls printing of the M.F.Nwk.EndpointID_1_1 instead of the M.F.Nwk.Short.EndpointID field.
        #   - M.F.Dat.Sdb.DelClu controls printing of the M.F.Gen.Cluster_1_1 field instead of the M.F.Dat.DataClusterManufacturer and M.F.Dat.DataClusterId fields.
        #   - M.F.Dat.Sdb.DelTime controls printing of the M.F.Dat.Time_1_1 and M.F.Dat.DeltaTime_1_1 fields instead of the M.F.Dat.Time and M.F.Dat.DeltaTime fields.
        M.F.Dat.Sdb.Cells : [
            {
                # The HAN address of the source device for this cell
                M.F.Nwk.HAN_1_1 : "001BC502B0100314",
                
                # The source endpoint for this cell
                M.F.Nwk.EndpointID_1_1 : 10,
                
                # The source cluster for this cell
                M.F.Gen.Cluster_1_1 : {
                    # The source cluster manufacturer for this cell
                    M.F.Gen.ClusterManufacturer_1_1 : 0,
                    
                    # The source cluster id for this cell
                    M.F.Gen.ClusterID_1_1 : 1794
                },
                
                # The time that this cell was generated
                # Value:
                # - seconds since 1 Jan 1970
                M.F.Dat.Time_1_1 : 1405705444,
                
                # The data, a list of the attribute IDs, values and types logged in this cell
                # - Each list element represents a single attribute description and value.
                M.F.Dat.Attributes_1_1 : [
                    {
                        # The ID of the attribute
                        # - This ID is specific to the manufacturer and id of the cluster.
                        # - Please consult the cluster's documentation for the meaning and
                        #   interpretation of the attribute's value.
                        M.F.Dat.AttributeID_1_1 : 57610,
                        
                        # The attribute's datatype
                        # - Attributes stored by the stream database are normalised into
                        #   a standard set of datatypes for storage. This does not necessarily
                        #   accurately reflect the datatype of the zigbee attribute as sent by the
                        #   end device.
                        # Value:
                        # - M.V.Dat.Type.Int            - the data is a signed integer (64-bit).
                        # - M.V.Dat.Type.Uint           - the data is an unsigned integer (64-bit).
                        # - M.V.Dat.Type.String         - the data is a string.
                        # - M.V.Dat.Type.Byte           - the data is a raw binary blob, it is encoded.
                        #                                 into a base64 and then sent as a string.
                        # - M.V.Dat.Type.Raw            - the data is a string (see M.V.Dat.Type.String).
                        # - M.V.Dat.Type.Timechange     - the data is a timechange: a record of the ESBox's
                        #                                 timebase being changed.
                        #                                   - at this time, timechange data is not
                        #                                     represented or stored by the stream database.
                        #                                   - the value will always be "TIMECHANGE".
                        M.F.Dat.Type_1_1 : M.V.Dat.Type.Uint,
                        
                        # The attribute's value
                        # - See the cluster's documentation for details on the meaning of the value.
                        # - See M.F.Dat.Type_1_1 for details on how to read the value.
                        M.F.Dat.Value_1_1 : 23791
                    }
                ]
            },
            {
                # The time that this cell was generated compared to the previous cell in the list
                # - This value is in seconds since the previous cell in the list.
                # - The value may be negative.
                # - Note that to get an absolute time for any particular cell, it is necessary to read
                #   all of the cells in sequence to calculate their absolute time.
                M.F.Dat.DeltaTime_1_1 : 56,
                M.F.Dat.Attributes_1_1 : [
                    {
                        M.F.Dat.AttributeID_1_1 : 57610,
                        M.F.Dat.Type_1_1 : M.V.Dat.Type.Uint,
                        M.F.Dat.Value_1_1 : 23826
                    }
                ]
            }
        ]
    }
}

# - Example for M.F.Dat.Source == M.V.Dat.Source.LatestReadings_1_1:
#
# Notes on Latest Readings in API version 1.1 vs API version 1.0:
# - Data sent from the latest readings buffer using API version 1.1 is sent slightly differently to how it is sent using
#   SendLatestReadings in API version 1.0.
# - In API version 1.0, when latest readings were requested and sent, the latest readings would be popped from the buffer and
#   sent to the requester. This would leave no readings in the buffer until each entry was replaced with new data received from
#   an end device.
# - In API version 1.1 however, when latest readings are requested and sent, a copy is made of the current latest readings at
#   that moment in time. This means that a copy of the data is left for the next request.
# - In order to manage data stagnation, entries (unique on: attr id, endpoint, cluster id, cluster manufacturer, device HAN) 
#   in the latest readings buffer have a short lifetime. If an entry is not overwritten before it stagnates, that entry will 
#   no longer be available in latest readings. This means that entries that are regularly received - such as a regularly reported
#   voltage attribute will always be available and up to date in latest readings while the device is online, whereas a transient
#   attribute such as a waveform requested specifically one time will exist in latest readings for a short time (usrconf setting: 
#   Data.LrRetMinMs - default: 60000ms) before being made unavailable.
ex_1_1__LatestReadings__SS_ESB_E_SendData_1_1 = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_ESB.E.SendData,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 0, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_ESB Cluster
    
    # The source of the data being sent
    # - Value:
    #   - M.V.Dat.Source.Sdb                    - data is sourced from the stream database
    #   - M.V.Dat.Source.LatestReadings_1_1     - data is sourced from the latest readings buffer
    #   - other                                 - not supported / not implemented yet in version 1.1
    M.F.Dat.Source : M.V.Dat.Source.LatestReadings_1_1,
    
    # The data being sent
    # - Each element in the list represents a device-endpoint-pair that may have latest readings data associated with it.
    # - May be empty.
    M.F.Dat.Data_1_1 : [
        {
            # The HAN address of the device which is the source of the data in M.F.Dat.Clusters_1_1
            M.F.Nwk.HAN_1_1 : "001BC502B0100314",
            
            # The source endpoint of the data in M.F.Dat.Clusters_1_1 
            M.F.Nwk.EndpointID_1_1 : 10,
            
            # A list of clusters that may have latest readings data associated with them
            # - Each element in the list represents a cluster manufacturer-id-pair.
            # - May be empty.
            M.F.Dat.Clusters_1_1 : [
                {
                    # The source cluster of the data in M.F.Dat.Attributes_1_1
                    M.F.Gen.Cluster_1_1 : {
                    
                        # The cluster's manufacturer
                        M.F.Gen.ClusterManufacturer_1_1 : 0,
                        
                        # The cluster's id
                        M.F.Gen.ClusterID_1_1 : 1794
                    },
                    
                    # A list of attributes representing the latest readings data for the parent cluster, endpoint and device
                    # - Each list element represents a single attribute description and data.
                    # - May be empty.
                    M.F.Dat.Attributes_1_1 : [
                        {
                            # The ID of the attribute
                            # - This ID is specific to the manufacturer and id of the cluster.
                            # - Please consult the cluster's documentation for the meaning and
                            #   interpretation of the attribute's value.
                            M.F.Dat.AttributeID_1_1 : 57610,
                            
                            # The attribute's datatype
                            # - Attributes stored in the latest readings buffer are normalised into
                            #   a standard set of datatypes for storage. This does not necessarily
                            #   accurately reflect the datatype of the zigbee attribute as sent by the
                            #   end device.
                            # Value:
                            # - M.V.Dat.Type.Int            - the data is a signed integer (64-bit).
                            # - M.V.Dat.Type.Uint           - the data is an unsigned integer (64-bit).
                            # - M.V.Dat.Type.String         - the data is a string.
                            # - M.V.Dat.Type.Byte           - the data is a raw binary blob, it is encoded.
                            #                                 into a base64 and then sent as a string.
                            # - M.V.Dat.Type.Raw            - the data is a string (see M.V.Dat.Type.String).
                            # - M.V.Dat.Type.Timechange     - the data is a timechange: a record of the ESBox's
                            #                                 timebase being changed.
                            #                                   - at this time, timechange data is not
                            #                                     represented or stored by latest readings.
                            #                                   - the value will always be "<unprintable>".
                            M.F.Dat.Type_1_1 : M.V.Dat.Type.Uint,
                            
                            # The time that this attribute data was generated
                            # Value:
                            # - seconds since 1 Jan 1970
                            M.F.Dat.Time_1_1 : 1405705444,
                    
                            # The attribute's value
                            # - See the cluster's documentation for details on the meaning of the value.
                            # - See M.F.Dat.Type_1_1 for details on how to read the value.
                            #
                            # - NOTE: this field will be changing to Value_1_1 in future versions!
                            #   - ESCos wishing to implement this field now should read the value of this attribute as:
                            #       - Value_1_1 present?
                            #           - Yes: use value in Value_1_1
                            #           - No: is Data_1_1 present?
                            #               - Yes: use value in Data_1_1
                            #               - No: error
                            M.F.Dat.Data_1_1 : 23791
                        }
                    ]
                }
            ]
        }
    ]
}


# Cluster: Saturn South ESBox (SS_ESB)
# Message: SendLatestReadings
# Message ID: M.SS_ESB.E.SendLatestReadings
# Queue Type: Single
# Versions: 1.0-1.0
# Direction: From ESBox (TX)
# Purpose: Returns data as requested by M.SS_ESB.E.GetLatestReadings
ex_1_0__SS_ESB_E_SendLatestReadings = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_ESB.E.SendLatestReadings,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 0, M.F.Gen.ClusterManufacturer : 4278 }, # SS_ESB Cluster

    # The data being sent
    # - Each element in the list represents a device-endpoint-pair that may have latest readings data associated with it.
    # - May be empty.
    M.F.Nwk.Endpoints : [
        {
            # The HAN address of the device which is the source of the data in M.F.Dat.Clusters
            M.F.Nwk.DevIEEE : "001BC502B0100314",
            
            # The source endpoint of the data in M.F.Dat.Clusters
            M.F.Nwk.EndpointID : 10,
            
            # A list of clusters that may have latest readings data associated with them
            # - Each element in the list represents a cluster manufacturer-id-pair.
            # - May be empty.
            M.F.Dat.Clusters : [
                {
                    # The source cluster of the data in M.F.Dat.Attributes_1_1
                    M.F.Dat.DataCluster : {
                        M.F.Gen.ClusterID : 1794,
                        M.F.Gen.ClusterManufacturer : 0
                    },
                    
                    # A list of attributes representing the latest readings data for the parent cluster, endpoint and device
                    # - Each list element represents a single attribute description and data.
                    # - May be empty.
                    M.F.Dat.Attributes : [
                        {
                            # The time that this attribute data was generated
                            # Value:
                            # - seconds since 1 Jan 1970
                            M.F.Dat.DataTime : 1405705444,
                    
                            # The ID of the attribute
                            # - This ID is specific to the manufacturer and id of the cluster.
                            # - Please consult the cluster's documentation for the meaning and
                            #   interpretation of the attribute's value.
                            M.F.Dat.AttributeID : 57610,
                            
                            # The attribute's value
                            # - See the cluster's documentation for details on the meaning of the value.
                            # - The type of value that is sent depends on the attribute's datatype.
                            # - Attributes stored in the latest readings buffer are normalised into
                            #   a standard set of datatypes for storage. This does not necessarily
                            #   accurately reflect the datatype of the zigbee attribute as sent by the
                            #   end device. These datatypes include an integer, string and 'binary' type.
                            #   - The integer is sent as a json number.
                            #   - The string is sent as a json string.
                            #   - The binary type is sent as raw bytes, encoded as base64 and then sent as a json string.
                            # - Please consult the cluster's documentation for which datatype is expected.
                            # - If an explicit indication of datatype is required, please use API version 1.1. Please 
                            #   note though that API version 1.1 uses GetData and SendData instead of GetLatestReadings
                            #   and SendLatestReadings to handle transmission of latest readings from the ESBox.
                            M.F.Dat.Value : 23791
                        }
                    ]
                }
            ]
        }
    ]
}


# Cluster: Saturn South Load Control (SS_LC)
# Message: DispatchReport
# Message ID: M.SS_LC.E.DispatchReport
# Queue Type: Normal
# Versions: 1.0+
# Direction: From ESBox (TX)
# Purpose: Returns an indication that a device successfully executed a BroadcastDispatch command.
#       - This message may be sent unprompted by the ESBox.
#       - This message is not properly supported by the Push API.
ex_1_0__SS_LC_E_DispatchReport = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_LC.E.DispatchReport,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 64784, M.F.Gen.ClusterManufacturer : 4278 }, # SS_LC Cluster
    
    # The HAN address of the device
    M.F.Nwk.DevIEEE : "001BC502B0100314"
}

ex_1_1__SS_LC_E_DispatchReport = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_LC.E.DispatchReport,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 64784, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_LC Cluster
    
    # The HAN address of the device
    M.F.Nwk.HAN_1_1 : "001BC502B0100314"
}


# Cluster: Saturn South Load Control (SS_LC)
# Message: UFLSReport
# Message ID: M.SS_LC.E.UFLSReport
# Queue Type: Normal
# Versions: 1.0+
# Direction: From ESBox (TX)
# Purpose: Returns an indication that a device underwent an automatic revert to safe-state due to an UFLS (under 
#          frequency load shedding) event
#       - This message may be sent unprompted by the ESBox.
#       - This message is not properly supported by the Push API.
ex_1_0__SS_LC_E_UFLSReport = {

    # Set the ID of the message
    M.F.Gen.MsgID : M.SS_LC.E.UFLSReport,
    
    # Set the cluster of the message
    M.F.Gen.Cluster : { M.F.Gen.ClusterID : 64784, M.F.Gen.ClusterManufacturer : 4278 }, # SS_LC Cluster
    
    # The HAN address of the device that underwent the automatic revert
    M.F.Nwk.DevIEEE : "001BC502B0100314",

    # The mains frequency at time of disconnection
    # - Value:
    #   - Hz*100
    M.F.SSLC.FrequencyOfDisconnect : 4895
}

ex_1_1__SS_LC_E_UFLSReport = {

    # Set the ID of the message
    M.F.Gen.MsgID_1_1 : M.SS_LC.E.UFLSReport,
    
    # Set the cluster of the message
    M.F.Gen.Cluster_1_1 : { M.F.Gen.ClusterID_1_1 : 64784, M.F.Gen.ClusterManufacturer_1_1 : 4278 }, # SS_LC Cluster
    
    # The HAN address of the device that underwent the automatic revert
    M.F.Nwk.HAN_1_1 : "001BC502B0100314",

    # The mains frequency at time of disconnection
    # - Value:
    #   - Hz*100
    M.F.SSLC.FrequencyOfDisconnect_1_1 : 4895
}




# -------------------------------------------------------------- Other / Notes:

# FatFS FRESULT
# - The meaning of fresult values as returned by some filesystem operations.
# - These values will be made available in SSMessages in the near future.
fresult = {
    'FR_OK' : 0,                    # (0) Succeeded
    'FR_DISK_ERR' : 1,              # (1) A hard error occurred in the low level disk I/O layer */
    'FR_INT_ERR' : 2,               # (2) Assertion failed */
    'FR_NOT_READY' : 3,             # (3) The physical drive cannot work */
    'FR_NO_FILE' : 4,               # (4) Could not find the file */
    'FR_NO_PATH' : 5,               # (5) Could not find the path */
    'FR_INVALID_NAME' : 6,          # (6) The path name format is invalid */
    'FR_DENIED' : 7,                # (7) Access denied due to prohibited access or directory full */
    'FR_EXIST' : 8,                 # (8) Access denied due to prohibited access */
    'FR_INVALID_OBJECT' : 9,        # (9) The file/directory object is invalid */
    'FR_WRITE_PROTECTED' : 10,      # (10) The physical drive is write protected */
    'FR_INVALID_DRIVE' : 11,        # (11) The logical drive number is invalid */
    'FR_NOT_ENABLED' : 12,          # (12) The volume has no work area */
    'FR_NO_FILESYSTEM' : 13,        # (13) There is no valid FAT volume */
    'FR_MKFS_ABORTED' : 14,         # (14) The f_mkfs() aborted due to any parameter error */
    'FR_TIMEOUT' : 15,              # (15) Could not get a grant to access the volume within defined period */
    'FR_LOCKED' : 16,               # (16) The operation is rejected according to the file sharing policy */
    'FR_NOT_ENOUGH_CORE' : 17,      # (17) LFN working buffer could not be allocated */
    'FR_TOO_MANY_OPEN_FILES' : 18,  # (18) Number of open files > _FS_SHARE */
    'FR_INVALID_PARAMETER' : 19,    # (19) Given parameter is invalid */
    'FR_RECURSION_LIMIT' : 20,      # (20) SS Error, recursion limit was reached */
}





