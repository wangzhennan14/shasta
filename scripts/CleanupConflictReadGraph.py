#!/usr/bin/python3

import shasta

a = shasta.Assembler()
a.accessConflictReadGraph()
a.cleanupConflictReadGraph()


