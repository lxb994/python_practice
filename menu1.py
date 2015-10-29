#!/usr/bin/env python
import os
province=['hebei','henan','shanxi']
city={'hebei':['shijiazhuang','baoding','handan'],'henan':['zhengzhou','kaifeng'
,'luoyang'],'shanxi':['taiyuan','linfen','yangquan']}
country={'shijiazhuang':['jingxingxian','zhengding','luquan'],
'baoding':['111','112','113'],
'handan':['111','112','113'],
'zhengzhou':['111','112','113'],
'kaifeng':['111','112','113'],
'luoyang':['111','112','113'],
'taiyuan':['111','112','113'],
'linfen':['111','112','113'],
'yangquan':['111','112','113']}
def menu():
	print'''
	+++++++++++++++++++++++
	+   1.province select +
	+   2.city select     +
	+   3.eixt program    +
	+++++++++++++++++++++++	
	'''
	op=raw_input('please select on>>>')
	return op
def menu_exit():
	os._exit(0)
def menu_error():
	print 'Unkonw options,Please try again!'
def province_select():
	global province_input
	while 1:
		province_input=raw_input('please input province select in %s:' %province)
		if province_input in city:
			print city[province_input]
			while 1:
				city_input=raw_input('please input city select in %s:' %city[province_input])
				if city_input in country: 
					print country[city_input]
					main()
				else:
					print 'Please choose city again'
					continue
		else:
			print 'Please choose province again'
			continue
def city_select():
	if globals().has_key('province_input'):
		while 1:
			city_input=raw_input('please input city select in %s:' %city[province_input])
			if city_input in country:
				print country[city_input]
				break
			else:
				print 'Please choose city again'
				continue
	else:
		print 'Please select a province first'
ops={'1':province_select,
	'2':city_select,
	'3':menu_exit}
def main():
	while True:
		op = menu()
		ops.get(op,menu_error)()
main()
