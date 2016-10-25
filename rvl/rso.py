#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""RSO File Format (RVL Shared Object)

TODO
"""


class Info(object):
    """RSO Information

    0x00 (uint32)   - Next RSO Entry
    0x04 (uint32)   - Previous RSO Entry
    0x08 (uint32)   - Section Count
    0x0C (uint32)   - Section Table Offset
    0x10 (uint32)   - Name Offset
    0x14 (uint32)   - Name Size
    0x18 (uint32)   - Version
    0x1C (uint32)   - BSS Section Size
    """
    pass


class SectionInfo(object):
    """RSO Section Information

    0x20 (uint8)    - Has Prolog
    0x21 (uint8)    - Has Epilog
    0x22 (uint8)    - Has Unresolved
    0x23 (uint8)    - Has BSS
    0x24 (uint32)   - Prolog Offset
    0x28 (uint32)   - Epilog Offset
    0x2C (uint32)   - Unresolved Offset
    """
    pass


class RelocationTables(object):
    """RSO Relocation Table

    0x30 (uint32)   - Internals Relocation Table Offset
    0x34 (uint32)   - Internals Relocation Table Size
    0x38 (uint32)   - Externals Relocation Table Offset
    0x3C (uint32)   - Externals Relocation Table Size
    """
    pass


class Exports(object):
    """RSO Exports

    0x40 (uint32)   - Exports Offset
    0x44 (uint32)   - Exports Size
    0x48 (uint32)   - Exports Name Offset
    """
    pass


class Imports(object):
    """RSO Imports

    0x4C (uint32)   - Imports Offset
    0x50 (uint32)   - Imports Size
    0x54 (uint32)   - Imports Name Offset
    """
    pass


class RSO(object):
    """RSO File Format

    0x00~0x20       - Information
    0x20~0x30       - Section Information
    0x30~0x40       - Relocation Tables
    0x40~0x48       - Exports
    0x48~0x58       - Imports
    """
    pass


if __name__ == "__main__":
    pass
