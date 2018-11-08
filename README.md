# PyNsPortal

Still working on documentation and the project itself

A python library/interactive shell to communicate with a Broaworks Network Server(s)  

## How to use in your project

```python
import pynsportal

```

## Using as an Interactive shell


If you have  

```

######        #     #        ######
#     # #   # ##    #  ####  #     #  ####  #####  #####   ##   #
#     #  # #  # #   # #      #     # #    # #    #   #    #  #  #
######    #   #  #  #  ####  ######  #    # #    #   #   #    # #
#         #   #   # #      # #       #    # #####    #   ###### #
#         #   #    ## #    # #       #    # #   #    #   #    # #
#         #   #     #  ####  #        ####  #    #   #   #    # ######

PyNsPortal Copyright (C) 2018  Aaron Kirk Parfitt
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.

======================================================================
PyNsPortal Command Line Interface
  Type help <command> for more information
======================================================================


PYNS_CLI>

 
```



## Broadworks Network Server Portal Overview


The Network Server portal application programming interface (API) constitutes 
a set of commands based on Hypertext Transfer Protocol(HTTP) requests, which
allows a portal server to communicate with the Network Server.  The interface 
consists of commands that are used to query the Network Server based on 
user information. The command interface is built upon the HTTP protocol.  
A client application sends an HTTP-based portal API requestto the BroadWorks
web portal running on the Network Server.

The Network Server Provisioning Server (PS) processes the request and returns 
the response to the BroadWorks web portal, which then returns an HTTP response 
to the client.
To prevent unauthorized portal API requests, the Network Server maintains an 
access control list that contains the only addresses from which portal API
requests are accepted. Support of the portal API over Hypertext Transfer 
Protocol Secure Sockets (HTTPS) is currently not offered


## API Commands

#### GetHostingNEInfo
This command returns the complete hosting NE information for a given
    user specified by its complete user ID (URL).  This includes the hosting
    cluster fully qualified domain name(FQDN) as well as the list of public
    addresses (IP addresses or host names) for each hosting NE server in the
    replicated cluster.  For each hosting NE server, its running software
    version is returned, as registered. This command includes an optional
    parameter, callPRequest, which specifies the list of servers of interest
    and indicates whether the list of call processing servers or the list of
    provisioning servers is returned in the portal API response.  If omitted,
    the list of provisioning servers is returned.In a hosting model composed
    only of Application Servers in primary-secondary mode, the portal API
    response is the same whether the request is for the list of call processing
    servers or provisioning servers. Therefore, in this case, the parameter
    value is irrelevant.
    In this model, the type of server (primary or secondary) is returned.

#### AuthorizeToken
This command prepares a short-lived token that is used instead of a user
    ID/password, when redirecting to the Network Server login servlet.
    This command is used to prepare a pre-authenticated login to the Network
    Server, for instance for an enterprise administrator.  To prepare a pre
    -authenticated login to an Application Server, such as for an end user or
    group administrator, the equivalent command in the Application Server
    portal API can be used.  Alternatively, the Application Server can be set
    up to use an external authentication client (this applies to the Release
    10 External Authentication Support functionality)
    
#### GetHostNodeAddresses
This command returns the list of public or private addresses
    (IP addresses or host names) for the serving Application Server nodes
    associated with a given Application Server address or alias. Public
    addresses are also known as “Access” addresses, while private
    addresses are also known as “Signaling” addresses. “DualRouting”
    addresses are included in the resulting list regardless of the value of the
    private parameter, because those addresses are public and private at the
    same time. If the Application Server has an External Web Server (this
    applies to Release 10 External Web Server Support functionality), then the
    “public” address is the address of the external Web Server, that is,
    the server name of the External Web Server.  In this same scenario,
    the “private” address is the address (server name) of the collocated Web
    Server on the Application Server host
    
#### GetServingAS
This command returns the list of public or private addresses
    (IP addresses or host names) for the serving hosting NE server associated
    with a given directory number, URL, or extension. For an extension,
    the group ID and hosting NE server address or alias is required.
    The returned list can contain addresses other than the serving hosting NE
    server, for instance when the serving hosting NE server is part of a
    replicated cluster; however, the addresses for the serving hosting NE
    server are listed first. Public addresses are also known as “Access”
    addresses, while private addresses are also known as “Signaling” addresses.
    “DualRouting” addresses are included in the resulting list regardless of
    the value of the private parameter, because these addresses are public
    and private at the same time. This command includes an optional parameter,
    returnCompatibleXSP, which when set to “true”, queries the Network Server
    for the list of valid Xtended Services Platforms corresponding to the
    hosting NE server where the user is located. This command includes an
    optional parameter, callPRequest, which specifies the list of servers of
    interest and indicates whether the list of call processing servers or the
    list of provisioning servers is returned in the portal API response.
    If omitted, the list of provisioning servers is returned. In a hosting
    model composed only of Application Servers in primary-secondary mode,
    the portal API response is the same whether the request is for the list
    of call processing servers or provisioning servers. Therefore,
    in this case, the parameter value is irrelevant.Note that the following
    examples assume that the dual-homed hosting NE server with the public IP
    address, 169.254.61.198, and private IP address, 192.168.8.215, exists
    on the Network Server system and is associated with the directory number
    (DN) “15146987500”, with the URL “user11@broadsoft.com”, and with
    extension “1234” in group ID “North_as87”.
    

#### GetAllHostingNeNodeAddresses
This command returns the list of addresses (IP addresses or host names)
    for the serving hosting NE server nodes. This command is capable of
    returning all nodes addresses from all hosting NEs at once
    within the selected NE maintenance partition, either the provisioning
    capable ones or the call processing capable ones. The requesting authority
    making this HTTP request has a major impact over the list of the returned
    nodes:  only those sharing the same NE maintenance partition from the
    requester will be returned. A requesting entity
    (the one from which originates the HTTP request) should only be
    interested in the nodes pertaining to his NE maintenance partition.
    However, if the requester’s NE maintenance partition cannot be determined,
    then the returned list will contain the addresses as if the network
    was partition-less based.

#### GetDeviceFileServingAS
This command returns the hosting NE server(s) where a device file can be
    located
    
#### GetHostsForEnterprise
This command returns a list of hosting NEs that hosts a given enterprise.

#### GetWebServerPortal
This command returns a list of Web Servers running the specified software version.

