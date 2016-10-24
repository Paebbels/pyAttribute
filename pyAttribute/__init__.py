# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
#
# =============================================================================
#                 _   _   _        _ _           _
#  _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___
# | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \
# | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|
# |_|    |___/
#
# =============================================================================
# Authors:						Patrick Lehmann
#
# Python package:	    pyAttribute Implementation
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
#
class Attribute():
	AttributesMemberName = "__attributes__"
	
	def __call__(self, func):
		# inherit attributes and append myself or create a new attributes list
		if (func.__dict__.__contains__(Attribute.AttributesMemberName)):
			func.__dict__[Attribute.AttributesMemberName].append(self)
		else:
			func.__setattr__(Attribute.AttributesMemberName, [self])
		return func
	
	def __str__(self):
		return self.__name__
	
	@classmethod
	def GetAttributes(self, method):
		if method.__dict__.__contains__(Attribute.AttributesMemberName):
			attributes = method.__dict__[Attribute.AttributesMemberName]
			if isinstance(attributes, list):
				return [attribute for attribute in attributes if isinstance(attribute, self)]
		return list()


class AttributeHelperMixin():
	def GetMethods(self):
		return {funcname: func
						for funcname, func in self.__class__.__dict__.items()
						if hasattr(func, '__dict__')
						}.items()
	
	def HasAttribute(self, method):
		if method.__dict__.__contains__(Attribute.AttributesMemberName):
			attributeList = method.__dict__[Attribute.AttributesMemberName]
			return (isinstance(attributeList, list) and (len(attributeList) != 0))
		else:
			return False
	
	def GetAttributes(self, method):
		if method.__dict__.__contains__(Attribute.AttributesMemberName):
			attributeList = method.__dict__[Attribute.AttributesMemberName]
			if isinstance(attributeList, list):
				return attributeList
		return list()
