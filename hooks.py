#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'


import os

def h(options, buildout):
    compile_dir=options["compile-directory"]
    cwd = os.getcwd()
    os.chdir(compile_dir)
    #os.system("cmake %s" % options["configure-options"])
    #fps = [os.path.join('core', 'sql', 'cmake_install.cmake'),
    # 'CMakeLists.txt']
    #for fp in fps:
    # f = open(fp).read()
    # content = f.replace('/usr/share/postlbs', '%s/share/postlbs' % options['location'])
    # open(fp, 'w').write(content)
    print "-> %s" % os.getcwd()
    print "Running cmake %s" % options["cmake-options"]
    #os.makedirs('bld')
    #os.chdir('bld')
    os.system("cmake %s" % options["cmake-options"])
    os.system('cmake -G "Unix Makefiles"')
    print "Building"
    #os.system("make")
    os.chdir(cwd)
    # vim:set et sts=4 ts=4 tw=80:
