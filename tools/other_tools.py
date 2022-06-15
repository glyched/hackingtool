# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection
from tools.others.android_attack import AndroidAttackTools
from tools.others.email_verifier import EmailVerifyTools
from tools.others.hash_crack import HashCrackingTools
from tools.others.homograph_attacks import IDNHomographAttackTools
from tools.others.mix_tools import MixTools
from tools.others.payload_injection import PayloadInjectorTools
from tools.others.socialmedia import SocialMediaBruteforceTools
from tools.others.socialmedia_finder import SocialMediaFinderTools
from tools.others.web_crawling import WebCrawlingTools
from tools.others.wifi_jamming import WifiJammingTools


class HatCloud(HackingTool):
    TITLE = "HatCloud(Bypass CloudFlare for IP)"
    DESCRIPTION = "HatCloud build in Ruby. It makes bypass in CloudFlare for " \
                  "discover real IP."
    INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://github.com/HatBashBR/HatCloud"

    def run(self):
        site = input("Enter Site >> ")
        os.chdir("HatCloud")
        subprocess.run(["sudo", "ruby", "hatcloud.rb", "-b", site])
class glyched_toolkit(HackingTool):
    TITLE = "glyched toolkit"
    DESCRIPTION = "glyched tools is a toolkit featuring 10 simple, yet powerful tools, written in python3"\
                  "--TOOLS--"\
                  "File encryption with fernet"\
                  "sherlocK:hunt down social media"\
                  "bulk-emailer"\
                  "MAC spoofer"\
                  "networkScanner(nmap is better)"\
                  "ARP-SPOOF:be the third wheel between the target and router!"\
                  "PacketSniffer:best-used with ARP-spoof"\
                  "DNS-Spoofer:makes it easy to rickroll!"\
                  "File-replacer:Replace the targets sketchy downloads with even sketchier ones!"
    INSTALL_COMMANDS = ["git clone https://github.com/glyched/glyched-tool"]
    PROJECT_URL = ["https://github.com/glyched/glyched-tool"]
                   

class OtherTools(HackingToolsCollection):
    TITLE = "Other tools"
    TOOLS = [
        SocialMediaBruteforceTools(),
        AndroidAttackTools(),
        HatCloud(),
        IDNHomographAttackTools(),
        EmailVerifyTools(),
        HashCrackingTools(),
        WifiJammingTools(),
        SocialMediaFinderTools(),
        PayloadInjectorTools(),
        WebCrawlingTools(),
        MixTools()
        glyched_toolkit()
    ]
