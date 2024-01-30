#Given two dictionaries, merge them into a new dictionary, excluding any keys that start with an underscore.
di_1={'user':'_SunShine','password': '55Sun_93/shine','ID': '1235663'}
di_2={'name': 'Eva','status':'__sun__','age':'17'}
new_di=dict(di_1, **di_2)
di_filter={k:v for(k,v) in new_di.items() if not v.startswith("_")}
print(di_filter)