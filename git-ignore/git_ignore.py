#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Ciel, http://ciel.im
# Distributed under terms of the MIT license.

import sys
from git_ignore_add import git_ignore_add
from git_ignore_save import git_ignore_save
from git_ignore_list import git_ignore_list
from git_ignore_show import git_ignore_show

# cat ignores >> .gitignore
def add(languages):
	git_ignore_add(languages)

# save current .gitignore
def save(filenames):
	if len(filenames)<1:
		filename = ""
	else:
		filename = filenames[0]
	git_ignore_save(filename)

# list all user ignore files
def list():
	git_ignore_list()
	return

def delete(filenames):
	print "delete"
	return

# cat .gitignore file
def show(languages):
	git_ignore_show(languages)
		
# print usage
def usage():
	print "usage: git ignore <subcommand>"
	print
	print "Available subcommands are:"
	print "    add    <project type>    Add gitignore files. Try use 'git ignore add Python C'"
	print "    save   [project type]    Save current .gitignore file as a template"
	print "    list                     List all saved ignore files"
	print "    delete [ignore file]     Delete a ignore file"
	print "    show   [ignore type]     Cat .gitignore file or ignore file"
	print "    usage                    Show this help message and exit"
	print "    version                  Show version and exit"
	print
	print "http://github.com/imwithye/git-ignore"
	print "git ignore, copyright Ciel <imwithye@gmail.com>"

# print version
def version():
	print "git ignore, version 0.1."
	print
	print "http://github.com/imwithye/git-ignore"
	print "git ignore, copyright Ciel <imwithye@gmail.com>"

# subcommand router
def select(argv):
	if argv[1] == "add":
		add(argv[2:])
		exit()
	elif argv[1] == "save":
		save(argv[2:])
		exit()
	elif argv[1] == "list":
		list()
		exit()
	elif argv[1] == "delete":
		delete(argv[2:])
		exit()
	elif argv[1] == "show":
		show(argv[2:])
		exit()
	elif argv[1] == "help" or argv[1] == "usage":
		usage()
		exit()
	elif argv[1] == "version":
		version()
		exit()
	else:
		print "unknown subcommand"
		usage()
		exit()

if __name__ == "__main__":
	if len(sys.argv)==1:
		sys.argv.append("usage")
	select(sys.argv)
