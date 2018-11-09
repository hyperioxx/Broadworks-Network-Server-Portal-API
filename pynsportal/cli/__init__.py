"""
Library which runs the command line interface which is based off the
broadworks command line interface for ease of use

"""

import cmd
import cli
import servlets

__version__ = "0.1.0"



INTRO1 = """
8888888b.           888b    888          8888888b.                  888             888 
888   Y88b          8888b   888          888   Y88b                 888             888 
888    888          88888b  888          888    888                 888             888 
888   d88P 888  888 888Y88b 888 .d8888b  888   d88P .d88b.  888d888 888888  8888b.  888 
8888888P"  888  888 888 Y88b888 88K      8888888P" d88""88b 888P"   888        "88b 888 
888        888  888 888  Y88888 "Y8888b. 888       888  888 888     888    .d888888 888 
888        Y88b 888 888   Y8888      X88 888       Y88..88P 888     Y88b.  888  888 888 
888         "Y88888 888    Y888  88888P' 888        "Y88P"  888      "Y888 "Y888888 888 
                888                                                                     
           Y8b d88P                                                                     
            "Y88P" 
"""


INTRO = """
PyNsPortal Copyright (C) 2018  Aaron Kirk Parfitt 
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it 
under certain conditions; type `show c' for details.

======================================================================
PyNsPortal Command Line Interface
  Type help <command> for more information
======================================================================

"""

WARREANTY = """
   
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
"""

HOST = None


class BaseShell(cmd.Cmd):

    host = None

    def default(self, line):
        self.stdout.write('Invalid command\n\n')

    def do_help(self, arg):
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]] = 1
            names.sort()
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)
            self.stdout.write("%s\n" % str(self.doc_leader))
            self.print_topics(self.doc_header, cmds_doc, 15, 80)
            self.print_topics(self.misc_header, list(help.keys()), 15, 80)
            self.print_topics(self.undoc_header, cmds_undoc, 15, 80)


    def print_topics(self, header, cmds, cmdlen, maxcol):
        if header != None:
            if cmds:
                self.stdout.write("%s\n" % str(header))
                self.columnize(cmds, maxcol - 1)
                self.stdout.write("\n")

    def columnize(self, list, displaywidth=80):
        for index, item in enumerate(list):
            if item == "get":
                print "    " + str(index) + ") " + "{:>8}".format(item) + " " \
                                                                          ": show related attributes"
            elif item == "set":
                print "    " + str(index) + ") " + "{:>8}".format(item) + " " \
                                                                          ": modify related attributes"
            else:
                print "    "+str(index)+") "+"{:>30}".format(item) + " : go to " \
                                                                 "level {" \
                                                                 "}".format(item)

    def parse_commands(self,line):
        commands = {}
        try:
            for i in range(0, len(line), 2):
                chunk = line[i:i + 2]
                commands[chunk[0]] = chunk[1]
            return commands
        except IndexError:
            return None

    def do_version(self, c):
        print "PyNsPortal Version: " + __version__


    def do_exit(self, i):
        print("Exiting the CLI ...")
        return True

    def do_q(self, i):
        return True

    def do_comp(self, c):
        print self.completion_matches







class NsPortalShell(BaseShell):
    _prompt = "PYNS_CLI"
    prompt = _prompt + "> "
    host = "localhost"
    doc_header = "Commands:"
    intro = INTRO1 + INTRO
    undoc_header = None
    ruler = False
    connection = True


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.aliases = {'0': self.do_AuthorizeToken,
                   '1': self.do_Connect,
                   '2': self.do_GetAllHostingNeNodeAddresses,
                   '3': self.do_GetDeviceFileServingAS,
                   '4': self.do_GetHostNodeAddresses,
                   '5': self.do_GetHostingNEInfo,
                   '6': self.do_GetHostsForEnterprise,
                   '7': self.do_GetServingAS,
                   '8': self.do_GetWebServerPortal,
                   'conn':self.do_Connect,}

    def do_GetWebServerPortal(self,c):
        """
           This command returns a list of Web Servers running the specified
           software version.
        """
        name = "GetWebServerPortal"
        shell = cli.GetWebServerPortalShell()
        shell.prompt = NsPortalShell._prompt +"/"+name+"> "
        shell.cmdloop()


    def do_GetHostingNEInfo(self,c):
        """
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
        """
        name = "GetHostingNEInfo"
        shell = cli.GetHostingNEInfoShell()
        shell.prompt = NsPortalShell._prompt + "/" + name + "> "
        shell.cmdloop()

    def do_AuthorizeToken(self,c):
        """
            This command prepares a short-lived token that is used instead of a user
            ID/password, when redirecting to the Network Server login servlet.
            This command is used to prepare a pre-authenticated login to the Network
            Server, for instance for an enterprise administrator.  To prepare a pre
            -authenticated login to an Application Server, such as for an end user or
            group administrator, the equivalent command in the Application Server
            portal API can be used.  Alternatively, the Application Server can be set
            up to use an external authentication client (this applies to the Release
            10 External Authentication Support functionality)
        """
        name = "AuthorizeToken"
        shell = cli.GetHostingNEInfoShell()
        shell.prompt = NsPortalShell._prompt + "/" + name + "> "
        shell.cmdloop()

    def do_GetHostNodeAddresses(self,c):
        """
            This command returns the list of public or private addresses
            (IP addresses or host names) for the serving Application Server nodes
            associated with a given Application Server address or alias. Public
            addresses are also known as "Access" addresses, while private
            addresses are also known as "Signaling" addresses. "DualRouting"
            addresses are included in the resulting list regardless of the value of the
            private parameter, because those addresses are public and private at the
            same time. If the Application Server has an External Web Server (this
            applies to Release 10 External Web Server Support functionality), then the
            "public" address is the address of the external Web Server, that is,
            the server name of the External Web Server.  In this same scenario,
            the "private" address is the address (server name) of the collocated Web
            Server on the Application Server host
        """
        print "Test"

    def do_GetServingAS(self,c):
        """
            This command returns the list of public or private addresses
            (IP addresses or host names) for the serving hosting NE server associated
            with a given directory number, URL, or extension. For an extension,
            the group ID and hosting NE server address or alias is required.
            The returned list can contain addresses other than the serving hosting NE
            server, for instance when the serving hosting NE server is part of a
            replicated cluster; however, the addresses for the serving hosting NE
            server are listed first. Public addresses are also known as "Access"
            addresses, while private addresses are also known as "Signaling" addresses.
            "DualRouting" addresses are included in the resulting list regardless of
            the value of the private parameter, because these addresses are public
            and private at the same time. This command includes an optional parameter,
            returnCompatibleXSP, which when set to "true", queries the Network Server
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
            (DN) "15146987500", with the URL "user11@broadsoft.com", and with
            extension "1234" in group ID "North_as87".
        """
        print "Test"

    def do_GetHostsForEnterprise(self, c):
        """
            This command returns a list of hosting NEs that hosts a given enterprise.
        """
        print "Test"

    def do_GetAllHostingNeNodeAddresses(self, c):
        """
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
            However, if the requester's NE maintenance partition cannot be determined,
            then the returned list will contain the addresses as if the network
            was partition-less based.
        """
        print "Test"

    def do_GetDeviceFileServingAS(self, c):
        """
            This command returns the hosting NE server(s) where a device file can be
            located
        """
        print "Test"

    def do_show(self, option):
        if option == "w":
            print WARREANTY
        elif option == "c":
            print """ dsasdasda"""
        else:
            print """ *** unknown show command"""


    def do_Connect(self, c):
        """
          This command checks connection to the Network Server(s)
        """
        name = "Connect"
        shell = ConnectShell()
        shell.prompt = NsPortalShell._prompt + "/" + name + "> "
        shell.cmdloop()


    def precmd(self, line):
        if NsPortalShell.connection == None:
            try:
                if line.split()[0] not in ("Connect", "?", "help", "exit",
                                            "q", "show", "version"):
                    print "Not connected to Network Server\n"
                    self.lastcmd = ""
                    return ''
                else:
                    return line
            except IndexError:
                return line
        else:
            return line


    def ns_check(self):
        NsPortalShell.host

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.aliases:
            self.aliases[cmd](arg)
        else:
            print("Invalid command\n\n")




class GetWebServerPortalShell(BaseShell):
    undoc_header = None
    doc_header = "Commands:"

    def do_get(self, c):
        "Get Message"
        line = c.split()
        if len(line) > 0:
            parsed_commands = self.parse_commands(line)
            if parsed_commands == None:
                print "Invalid command\n\n"
            else:
                # TODO: fix me
                pass
        else:
            servlets.GetWebServerPortal(BaseShell.host)

    def precmd(self, line):
        if BaseShell.host == None:
            try:
                if line.split()[0] not in ("Connect", "?", "help", "exit",
                                            "q", "show", "version"):
                    print "Not connected to Network Server\n"
                    self.lastcmd = ""
                    return ''
                else:
                    return line
            except IndexError:
                return line
        else:
            return line

    def do_set(self, c):
        line = c.split()

    def do_test(self,l):
        print "Test"




class GetHostingNEInfoShell(BaseShell):
    undoc_header = None
    doc_header = "Commands:"

    def do_test(self):
        "Test Command"
        print("Test")

class ConnectShell(BaseShell):
    undoc_header = None
    doc_header = "Commands:"

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.aliases = {'0': self.do_get,
                        '1': self.do_set,}

    def do_get(self,c):
        "Get"
        try:
            print "host="+BaseShell.host
        except TypeError:
            print "host="

    def do_set(self,c):
        "Set"
        line = c.split()
        if len(line) > 0:
            parsed_commands = self.parse_commands(line)
            if parsed_commands == None:
                print "Invalid command\n\n"
            else:
                try:
                    BaseShell.host = parsed_commands['host']
                except KeyError:
                    print "Invalid command\n\n"
        else:
            print "Invalid command\n\n"

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.aliases:
            self.aliases[cmd](arg)
        else:
            print("Invalid command\n\n")